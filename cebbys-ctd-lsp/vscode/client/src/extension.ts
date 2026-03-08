import * as path from "path";
import * as vscode from "vscode";
import {
    LanguageClient,
    LanguageClientOptions,
    ServerOptions,
    TransportKind,
} from "vscode-languageclient/node";

/**
 * One LanguageClient per workspace folder — mirrors the lsp-multi-server-sample approach.
 * Each client spawns its own Python server process scoped to that workspace folder.
 */
const clients: Map<string, LanguageClient> = new Map();

export function activate(context: vscode.ExtensionContext): void {
    // Start a server for every workspace folder that already exists
    for (const folder of vscode.workspace.workspaceFolders ?? []) {
        startClientForFolder(context, folder);
    }

    // React to workspace folder changes
    context.subscriptions.push(
        vscode.workspace.onDidChangeWorkspaceFolders((event) => {
            for (const folder of event.added) {
                startClientForFolder(context, folder);
            }
            for (const folder of event.removed) {
                stopClientForFolder(folder);
            }
        })
    );
}

export async function deactivate(): Promise<void> {
    const stops: Promise<void>[] = [];
    for (const client of clients.values()) {
        stops.push(client.stop());
    }
    await Promise.all(stops);
}

function startClientForFolder(
    context: vscode.ExtensionContext,
    folder: vscode.WorkspaceFolder
): void {
    if (clients.has(folder.uri.toString())) {
        return; // Already running for this folder
    }

    // Resolve the Python interpreter from the workspace virtual environment
    const pythonPath = resolvePythonPath(context);

    const serverOptions: ServerOptions = {
        command: pythonPath,
        args: ["-m", "lv.cebbys.languages.ctd.lsp"],
        transport: TransportKind.stdio,
        options: {
            cwd: folder.uri.fsPath,
        },
    };

    const clientOptions: LanguageClientOptions = {
        // Only activate for .ctd files within this specific workspace folder
        documentSelector: [
            {
                scheme: "file",
                language: "ctd",
                pattern: `${folder.uri.fsPath}/**/*`,
            },
        ],
        workspaceFolder: folder,
        synchronize: {
            fileEvents: vscode.workspace.createFileSystemWatcher(
                new vscode.RelativePattern(folder, "**/*.ctd")
            ),
        },
    };

    const client = new LanguageClient(
        `cebbys-ctd-lsp-${folder.name}`,
        `CTD Language Server (${folder.name})`,
        serverOptions,
        clientOptions
    );

    client.start();
    clients.set(folder.uri.toString(), client);
}

async function stopClientForFolder(folder: vscode.WorkspaceFolder): Promise<void> {
    const key = folder.uri.toString();
    const client = clients.get(key);
    if (client) {
        await client.stop();
        clients.delete(key);
    }
}

/**
 * Resolve the Python interpreter path.
 *
 * Priority:
 *   1. The workspace .venv (standard uv layout)
 *   2. Fall back to the Python interpreter from the Python extension
 *   3. Fall back to "python" on PATH
 */
function resolvePythonPath(context: vscode.ExtensionContext): string {
    // Try workspace-relative .venv first (works for uv workspaces)
    const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
    if (workspaceRoot) {
        const isWindows = process.platform === "win32";
        const venvPython = isWindows
            ? path.join(workspaceRoot, ".venv", "Scripts", "python.exe")
            : path.join(workspaceRoot, ".venv", "bin", "python");
        if (require("fs").existsSync(venvPython)) {
            return venvPython;
        }
    }

    // Fall back to the Python extension's selected interpreter
    const pythonExt = vscode.extensions.getExtension("ms-python.python");
    if (pythonExt?.isActive) {
        const interpreterPath: string | undefined =
            pythonExt.exports?.settings?.getExecutionDetails?.()?.execCommand?.[0];
        if (interpreterPath) {
            return interpreterPath;
        }
    }

    return "python";
}

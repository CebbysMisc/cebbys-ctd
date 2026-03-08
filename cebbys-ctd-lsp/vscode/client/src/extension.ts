import * as path from "path";
import * as fs from "fs";
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
 *   1. Project .venv — navigate up from the extension dir (cebbys-ctd-lsp/vscode → cebbys-ctd)
 *   2. Each workspace folder's .venv
 *   3. python.defaultInterpreterPath setting (if it's already an absolute path)
 *   4. "python" on PATH
 */
function resolvePythonPath(context: vscode.ExtensionContext): string {
    const isWindows = process.platform === "win32";
    const pythonBin = isWindows ? "python.exe" : "python";

    const candidates: string[] = [];

    // 1. Navigate from the extension install path back to the workspace root.
    //    Extension path: <workspace>/cebbys-ctd-lsp/vscode
    //    Project root:   <workspace>  (two levels up)
    const projectRoot = path.resolve(context.extensionPath, "..", "..");
    candidates.push(
        isWindows
            ? path.join(projectRoot, ".venv", "Scripts", pythonBin)
            : path.join(projectRoot, ".venv", "bin", pythonBin)
    );

    // 2. Each open workspace folder's .venv
    for (const folder of vscode.workspace.workspaceFolders ?? []) {
        candidates.push(
            isWindows
                ? path.join(folder.uri.fsPath, ".venv", "Scripts", pythonBin)
                : path.join(folder.uri.fsPath, ".venv", "bin", pythonBin)
        );
    }

    for (const candidate of candidates) {
        if (fs.existsSync(candidate)) {
            return candidate;
        }
    }

    // 3. python.defaultInterpreterPath (only if already resolved — no ${...} variables)
    const interpreterPath = vscode.workspace
        .getConfiguration("python")
        .get<string>("defaultInterpreterPath");
    if (interpreterPath && !interpreterPath.includes("${")) {
        return interpreterPath;
    }

    return "python";
}

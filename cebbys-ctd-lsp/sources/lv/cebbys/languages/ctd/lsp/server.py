"""CTD Language Server — diagnostics via pygls."""
from __future__ import annotations

import pathlib as Pathlib
import traceback as Traceback
from typing import Any

from pygls.lsp.server import LanguageServer
from lsprotocol import types as LspTypes

import lv.cebbys.languages.ctd.loader as Loader
import lv.cebbys.languages.ctd.utility.logging as Logging

LOGGER = Logging.get_logger(__name__)

SERVER_NAME = "cebbys-ctd-lsp"
SERVER_VERSION = "0.1.0"


def create_server():
    registry = LanguageServer(SERVER_NAME, SERVER_VERSION)

    
    def did_open(ls: LanguageServer, params: LspTypes.DidOpenTextDocumentParams):
        print(f"[{ls.name}|{ls.process_id}] Did open ({params})")
    registry.feature(LspTypes.TEXT_DOCUMENT_DID_OPEN)(did_open)

        
    def did_save(ls: LanguageServer, params: LspTypes.DidSaveTextDocumentParams):
        print(f"[{ls.name}|{ls.process_id}] Did save ({params})")
    registry.feature(LspTypes.TEXT_DOCUMENT_DID_SAVE)(did_save)

        
    def did_close(ls: LanguageServer, params: LspTypes.DidCloseTextDocumentParams):
        print(f"[{ls.name}|{ls.process_id}] Did close ({params})")
    registry.feature(LspTypes.TEXT_DOCUMENT_DID_CLOSE)(did_close)


    return registry


def _validate_workspace(ls: LanguageServer, document_uri: str) -> None:
    """Load all CTD files in the workspace folder that contains the given document,
    then publish diagnostics for any parse or resolution errors."""
    workspace_folder: LspTypes.WorkspaceFolder | None
    folder_path: Pathlib.Path
    diagnostics_by_uri: dict[str, list[LspTypes.Diagnostic]]

    workspace_folder = _find_workspace_folder(ls, document_uri)
    if workspace_folder is None:
        LOGGER.warning(f"No workspace folder found for: {document_uri}")
        return

    folder_path = Pathlib.Path(_uri_to_path(workspace_folder.uri))
    LOGGER.debug(f"Validating workspace: {folder_path}")

    diagnostics_by_uri = _collect_diagnostics(folder_path)

    # Ensure the active document is always published (even if no errors)
    if document_uri not in diagnostics_by_uri:
        diagnostics_by_uri[document_uri] = []

    for uri, diagnostics in diagnostics_by_uri.items():
        # ls.publish_diagnostics(uri, diagnostics)
        pass


def _collect_diagnostics(folder_path: Pathlib.Path) -> dict[str, list[LspTypes.Diagnostic]]:
    """Run CtdLoader over the workspace folder and convert errors to LSP diagnostics."""
    diagnostics: dict[str, list[LspTypes.Diagnostic]] = {}

    try:
        loader: Loader.CtdLoader = Loader.CtdLoader([folder_path])
        # If loading succeeds, clear all diagnostics
        # for ctd_file, *_ in loader.ctds:
        #     diagnostics[_path_to_uri(ctd_file)] = []
        pass
    except Exception as exc:
        LOGGER.error(f"Error loading workspace: {exc}")
        # Attempt to attribute the error to a specific file
        tb: str = Traceback.format_exc()
        file_uri, line, message = _extract_error_location(tb, exc, folder_path)
        diagnostic: LspTypes.Diagnostic = LspTypes.Diagnostic(
            range=LspTypes.Range(
                start=LspTypes.Position(line=max(0, line - 1), character=0),
                end=LspTypes.Position(line=max(0, line - 1), character=256),
            ),
            message=message,
            severity=LspTypes.DiagnosticSeverity.Error,
            source=SERVER_NAME,
        )
        diagnostics.setdefault(file_uri, []).append(diagnostic)

    return diagnostics


def _extract_error_location(
    traceback_str: str,
    exc: Exception,
    folder_path: Pathlib.Path,
) -> tuple[str, int, str]:
    """Best-effort extraction of file/line from exception traceback.

    Returns (file_uri, line_number, message).
    Falls back to line 1 of the first CTD file in the folder.
    """
    file_uri: str = ""
    line: int = 1
    message: str = str(exc)

    # Walk traceback lines looking for a .ctd file reference
    for tb_line in traceback_str.splitlines():
        tb_line = tb_line.strip()
        if tb_line.startswith("File ") and ".ctd" in tb_line:
            parts = tb_line.split(", line ")
            if len(parts) >= 2:
                path_part = parts[0].removeprefix('File "').removesuffix('"')
                try:
                    line = int(parts[1].split(",")[0])
                    file_uri = _path_to_uri(Pathlib.Path(path_part))
                    break
                except ValueError:
                    pass

    if not file_uri:
        # Fall back to first CTD file found
        ctd_files: list[Pathlib.Path] = list(folder_path.rglob("*.ctd"))
        if ctd_files:
            file_uri = _path_to_uri(ctd_files[0])

    return file_uri, line, message


def _find_workspace_folder(
    ls: LanguageServer, document_uri: str
) -> LspTypes.WorkspaceFolder | None:
    """Return the workspace folder that is the closest ancestor of the document."""
    # workspace: Any = ls.workspace
    # folders: list[LspTypes.WorkspaceFolder] = list(
    #     (workspace.folders or {}).values()
    # ) if workspace else []

    # best: LspTypes.WorkspaceFolder | None = None
    # for folder in folders:
    #     if document_uri.startswith(folder.uri):
    #         if best is None or len(folder.uri) > len(best.uri):
    #             best = folder
    # return best
    pass

def _uri_to_path(uri: str) -> str:
    """Convert a file:// URI to a local filesystem path string."""
    if uri.startswith("file:///"):
        path = uri[len("file:///"):]
        # On Windows, restore the drive letter colon
        if len(path) >= 2 and path[1] == ":":
            return path
        # Unix-style: re-add leading slash
        return "/" + path
    return uri


def _path_to_uri(path: Pathlib.Path) -> str:
    """Convert a local path to a file:// URI."""
    return path.as_uri()

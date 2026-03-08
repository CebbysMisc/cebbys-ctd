"""Entry point for the CTD Language Server process.

Launched by the VSCode extension client as a subprocess communicating over stdio.
"""
import sys as Sys
from lv.cebbys.languages.ctd.lsp.server import create_server


def main() -> None:
    server = create_server()
    server.start_io()


if __name__ == "__main__":
    main()

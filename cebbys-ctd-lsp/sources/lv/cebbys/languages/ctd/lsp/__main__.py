"""Entry point for the CTD Language Server process.

Launched by the VSCode extension client as a subprocess communicating over stdio.
"""
from lv.cebbys.languages.ctd.lsp import main

if __name__ == "__main__":
    main()

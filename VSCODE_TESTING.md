# VSCode Test Integration for cebbys-ctd

## ⚠️ Workspace-Only Project

**This project must ONLY be opened via the workspace file.**

Opening as a folder (File → Open Folder) is not supported and will not work correctly.

## Multi-Root Workspace Configuration

This workspace uses a **multi-root workspace** setup to enable proper test discovery across all modules.

## How to Use

### Step 1: Open the Workspace File

Instead of opening the folder directly, open the workspace file:

1. **File → Open Workspace from File...**
2. Select `cebbys-ctd.code-workspace`

Alternatively, from command line:
```bash
code cebbys-ctd.code-workspace
```

### Step 2: Verify Python Interpreter

Make sure the shared `.venv` interpreter is selected:
- Check the bottom-right status bar
- Should show: `Python 3.13.11 ('.venv': venv)`
- If not, press `Ctrl+Shift+P` → "Python: Select Interpreter" → Choose `.venv/Scripts/python.exe`

### Step 3: Discover Tests

1. Click the **Testing** icon in the left sidebar (beaker icon)
2. Tests should automatically discover for **module folders only**:
   - 📦 antlr4
   - 📦 meta
   - 📦 resolver  
   - 📦 loader
3. The 🏠 Workspace Root folder will **not** show tests (by design - it only contains shared configuration)

Each module is now treated as a separate workspace folder with independent test discovery.

## Features You Get

✅ **Test Explorer** - All tests visible in sidebar, organized by module  
✅ **Run Individual Tests** - Click the play button next to any test  
✅ **Debug Tests** - Set breakpoints and debug with F5  
✅ **Inline Results** - See test results directly in your test files  
✅ **Filter by Status** - Show only failed/passed tests  
✅ **Re-run Failed** - Quickly re-run tests that failed  

## Why Multi-Root Workspace?

The project has multiple independent modules, each with their own `tests/conftest.py`. When running pytest from the workspace root, these files conflict (all import as `tests.conftest`).

The multi-root workspace solves this by:
- Treating each module as an independent workspace folder
- Running pytest separately from each module's root directory
- Avoiding conftest naming conflicts
- Maintaining a shared `.venv` across all modules
- **Excluding the workspace root from test discovery** (only modules have tests enabled)

## Folder Structure

```
📁 cebbys-ctd/
├── 📁 🏠 Workspace Root (root folder with shared .venv)
├── 📁 📦 antlr4 (cebbys-ctd-antlr4)
│   └── .vscode/settings.json (pytest config for this module)
├── 📁 📦 meta (cebbys-ctd-meta)
│   └── .vscode/settings.json (pytest config for this module)
├── 📁 📦 resolver (cebbys-ctd-resolver)
│   └── .vscode/settings.json (pytest config for this module)
├── 📁 📦 loader (cebbys-ctd-loader)
│   └── .vscode/settings.json (pytest config for this module)
└── cebbys-ctd.code-workspace (multi-root workspace configuration)
```

## Running Tests

### Via Test Explorer (Recommended)
- Click tests in the sidebar and use the play/debug buttons

### Via Tasks (Still Available)
- `Ctrl+Shift+P` → "Tasks: Run Task"
- Select the module's test task

### Via Terminal
```bash
# Test specific module
uv run pytest cebbys-ctd-antlr4/tests -v
uv run pytest cebbys-ctd-meta/tests -v

# Test all modules (from workspace root)
uv run pytest cebbys-ctd-antlr4/tests cebbys-ctd-meta/tests -v
```

## Troubleshooting

### Tests Don't Appear
1. Make sure you opened the `.code-workspace` file (not just the folder)
2. Verify the Python interpreter is selected (`.venv`)
3. Click the "Refresh Tests" button in the Testing sidebar
4. Check Output → Python Test Log for errors

### "Unknown Python Environment category 'UvWorkspace'"
This warning is harmless - VSCode doesn't recognize uv workspaces yet, but it still works.

### Conftest Conflicts
If you still see conftest errors, ensure:
- You opened via the workspace file (not folder)
- Each module has its own `.vscode/settings.json`
- Tests are being discovered per-module (check the Testing sidebar - you should see module names as folder roots)

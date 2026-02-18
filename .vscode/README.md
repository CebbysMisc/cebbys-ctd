# ⚠️ Open as Workspace

**This project must be opened as a workspace, not as a folder.**

## How to Open

### Option 1: From Command Line
```bash
code cebbys-ctd.code-workspace
```

### Option 2: From VSCode
1. **File → Open Workspace from File...**
2. Select `cebbys-ctd.code-workspace`

### Option 3: Double-Click
Simply double-click `cebbys-ctd.code-workspace` in your file explorer.

## Why Workspace-Only?

This is a **multi-module Python workspace** with:
- Multiple independent modules (antlr4, meta, resolver, loader, types)
- Shared `.venv` across all modules
- Per-module test discovery to avoid conftest conflicts
- Centralized configuration in the workspace file

Opening as a folder will not work correctly because:
- ❌ Test discovery will fail (conftest naming conflicts)
- ❌ Settings won't be applied properly
- ❌ Multi-root workspace features unavailable

## What You Get with Workspace

✅ **Test Explorer** - Tests for each module separately  
✅ **Shared Environment** - Single `.venv` for all modules  
✅ **Proper IntelliSense** - All import paths configured  
✅ **ANTLR4 Integration** - Grammar generation configured  
✅ **Organized Structure** - Each module as independent folder  

---

**Always use**: `cebbys-ctd.code-workspace` 🎯

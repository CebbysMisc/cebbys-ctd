# Development Instructions

## Project Overview

cebbys-ctd is a custom type definition language project that uses ANTLR4 to parse custom language files and Python to interpret, instantiate, and link the resulting objects.

## Project Structure

```
cebbys-ctd/
├── sources/          # Source code root directory
├── tests/            # Tests directory with subdirectories as test modules
├── resources/        # Resources directory containing ANTLR4 grammar files
└── hints/            # Type hints directory (not a source root)
    └── antlr4/       # ANTLR4 type stubs (.pyi files only)
```

### Directory Guidelines

- **sources/**: Main source code directory. This is the source root for the Python project.
- **tests/**: Test files organized in subdirectories as modules containing multiple tests.
- **resources/**: Contains ANTLR4 grammar files (`.g4`) and other project resources.
- **hints/**: Type hint stubs directory. Not a source root, but subdirectories within it are added to Python's extra paths.

## Development Environment

This project is developed using **Visual Studio Code** with the following configuration:

- Python analysis and autocomplete paths include `sources` and subdirectories of `hints/`
- pytest is configured for testing with tests located in the `tests/` directory

## Development Workflow

1. **Define grammar**: Create/modify ANTLR4 grammar files in `resources/`
2. **Generate parsers**: Use ANTLR4 to generate Python parser code
3. **Implement interpreters**: Write Python code in `sources/` to interpret parsed AST
4. **Create objects**: Instantiate Python objects from parsed definitions
5. **Link objects**: Implement linking logic to connect related objects
6. **Test**: Write tests in `tests/` directory organized by module

## Technology Stack

- ANTLR4 for grammar definition and parsing
- Python for runtime interpretation and object management
- VSCode as the development environment

## Branching Strategy

**REQUIRED**: Follow this Git branching workflow:

### Release Branch

- **Branch name**: `release/{version}` (e.g., `release/1.0.0`)
- **Protection**: No direct commits allowed
- **Updates**: Only via Pull Requests from feature branches

### Feature Branches

- **Branch name template**: `feature/{short-description-for-the-feature}`
- **Examples**:
  - `feature/add-parser-support`
  - `feature/implement-type-checker`
  - `feature/fix-namespace-resolution`

### Workflow

1. **Create feature branch** from latest release branch:
   ```bash
   git checkout release/1.0.0
   git pull
   git checkout -b feature/my-new-feature
   ```

2. **Develop and commit** changes on feature branch:
   ```bash
   git add .
   git commit -m "Your commit message"
   ```

3. **Push feature branch** and create Pull Request:
   ```bash
   git push origin feature/my-new-feature
   ```

4. **Merge via PR** after review and approval

5. **Delete feature branch** after successful merge

### Branch Protection Rules

- Release branches must be protected
- All changes require PR approval
- No force pushes to release branches

## Adding Type Hint Modules

The `hints/` directory contains type stub modules (`.pyi` files) for external libraries that may lack type hints. To add a new hint module:

1. **Create a subdirectory** under `hints/` with the module name:
   ```
   mkdir hints/<module_name>
   ```

2. **Add type stub files** (`.pyi` files) to the new directory. These files should contain type definitions for the external library.

3. **Update VSCode settings** in `.vscode/settings.json` to include the new module in the Python extra paths:
   ```json
   {
       "python.analysis.extraPaths": [
           "${workspaceFolder}/sources",
           "${workspaceFolder}/hints/antlr4",
           "${workspaceFolder}/hints/<module_name>"
       ],
       "python.autoComplete.extraPaths": [
           "${workspaceFolder}/sources",
           "${workspaceFolder}/hints/antlr4",
           "${workspaceFolder}/hints/<module_name>"
       ]
   }
   ```

**Note**: The `hints/` directory itself is NOT a source root. Only the subdirectories within `hints/` are added to the Python path.

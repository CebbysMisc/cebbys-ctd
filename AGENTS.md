# cebbys-ctd

Custom Type Definition Language - A domain-specific language for defining custom datatypes.

## Documentation Requirements

**IMPORTANT**: This file must be kept up to date. Whenever the project structure changes or new requirements are introduced, this document must be updated to reflect those changes. This includes:

- Changes to module organization or directory structure
- New modules or packages added to the workspace
- New conventions or coding standards
- Changes to build, test, or deployment commands
- New dependencies or tooling requirements

## Project Structure

The project uses a **uv workspace** with 5 independent modules sharing a single `.venv`:

```
cebbys-ctd/                               # Workspace root
├── pyproject.toml                        # Workspace configuration
├── conftest.py                           # Shared test fixtures and utilities
├── uv.lock                               # Lockfile for all workspace dependencies
├── .venv/                                # Shared virtual environment
│
├── cebbys-ctd-antlr4/                    # ANTLR4 parser module
│   ├── pyproject.toml
│   ├── sources/lv/cebbys/languages/ctd/antlr4/
│   │   ├── __init__.py                   # Re-exports ANTLR4 and generated classes
│   │   └── __generated__/                # Generated parser files
│   │       ├── CtdLexer.py
│   │       ├── CtdParser.py
│   │       └── CtdVisitor.py
│   └── tests/
│
├── cebbys-ctd-types/                     # Type definitions module
│   ├── pyproject.toml
│   └── sources/lv/cebbys/languages/ctd/types/
│       ├── __init__.py
│       ├── ctd/                          # Resolved CTD definition types (active)
│       └── meta/                         # Metadata types (pre-resolution)
│           ├── __init__.py
│           ├── __api__.py               # Meta base class, ModulePath
│           ├── decorator.py             # DecoratorMeta
│           ├── typedef.py               # TypedefMeta
│           ├── alias.py                 # AliasMeta
│           ├── enum.py                  # EnumMeta, EnumMemberMeta
│           ├── flag.py                  # FlagMeta, FlagMemberMeta
│           ├── structure.py             # StructureMeta, StructureMemberMeta
│           ├── interface.py             # InterfaceMeta
│           ├── function.py              # FunctionMeta, ParameterMeta
│           └── collection.py            # DefinitionCollectionMeta
│
├── cebbys-ctd-meta/                      # Meta loading module
│   ├── pyproject.toml
│   ├── sources/lv/cebbys/languages/ctd/meta/
│   │   ├── __init__.py                  # Exports MetaLoader, MetaVisitor
│   │   ├── loader.py                    # MetaLoader - orchestrates file parsing
│   │   └── visitor.py                   # MetaVisitor - ANTLR4 visitor
│   ├── resources/test/ctd/              # Test CTD files
│   └── tests/                           # Stage 1 tests (meta loading)
│
├── cebbys-ctd-resolver/                  # Type resolution module
│   ├── pyproject.toml
│   ├── sources/lv/cebbys/languages/ctd/resolver/
│   │   ├── __init__.py                  # Exports CtdMetaResolver
│   │   ├── resolver.py                  # CtdMetaResolver - main entry point
│   │   ├── constructor/                 # Stage 2: declaration construction
│   │   ├── linker/                      # Stage 3: reference linking
│   │   ├── manager/                     # Resolution manager
│   │   ├── storage/                     # Type cache / storage
│   │   └── event/                       # Resolution events
│   ├── resources/test/ctd/              # Test CTD files
│   └── tests/                           # Stage 2-3 tests (construction & resolution)
│
├── cebbys-ctd-loader/                    # Main loader module (public API)
│   ├── pyproject.toml
│   ├── sources/lv/cebbys/languages/ctd/
│   │   ├── __init__.py
│   │   └── loader.py                    # CtdLoader - main entry point
│   └── resources/ctd/                   # Sample CTD files
│
└── hints/                                # Type stubs for external libraries
    └── antlr4/
```

## Module Dependencies

```
cebbys-ctd-antlr4     (no internal deps, depends on antlr4-python3-runtime)
       ↓
cebbys-ctd-types      (no internal deps)
       ↓
cebbys-ctd-meta       (depends on: antlr4, types)
       ↓
cebbys-ctd-resolver   (depends on: meta, types)
       ↓
cebbys-ctd-loader     (depends on: resolver, meta, types)
```

## Workspace Configuration

All modules use `workspace = true` for inter-module dependencies:

```toml
# In each module's pyproject.toml
[tool.uv.sources]
cebbys-ctd-antlr4 = { workspace = true }
cebbys-ctd-types = { workspace = true }
# ... etc
```

The root `pyproject.toml` defines workspace members:

```toml
[tool.uv.workspace]
members = [
    "cebbys-ctd-antlr4",
    "cebbys-ctd-types",
    "cebbys-ctd-meta",
    "cebbys-ctd-resolver",
    "cebbys-ctd-loader",
]
```

## Module Organization Conventions

### Module Structure Pattern

Each package follows a consistent organization:

```
package/
├── __init__.py    # Imports and re-exports all public classes
├── __api__.py     # Common/base classes shared across the package
├── typedef.py     # TypedefDefinition (or TypedefMeta, TypedefResolver)
├── enum.py        # EnumDefinition, EnumMemberDefinition
├── flag.py        # FlagDefinition, FlagMemberDefinition
├── structure.py   # StructureDefinition, StructureMemberDefinition
├── interface.py   # InterfaceDefinition
├── function.py    # FunctionDefinition, ParameterDefinition
└── collection.py  # Collection class (if applicable)
```

### Rules

1. **One definition model per script**: Each type (typedef, enum, flag, structure, function) has its own dedicated script file.

2. **Common code in `__api__.py`**: Base classes, shared types, and common utilities are defined in `__api__.py`.

3. **Package exports in `__init__.py`**: All public classes are imported and re-exported in `__init__.py`:
   ```python
   from package.__api__ import *
   from package.typedef import *
   from package.enum import *
   # ... etc

   __all__ = ['BaseClass', 'TypedefDefinition', 'EnumDefinition', ...]
   ```

4. **Import convention**: External code imports from the package, not individual modules:
   ```python
   # Correct
   import lv.cebbys.languages.ctd.types.ctd as Ctd

   # Avoid
   import lv.cebbys.languages.ctd.types.ctd.typedef as Typedef
   ```

## Architecture

The project consists of 3 processing stages forming a pipeline:

### Stage 1: Meta Loading (`cebbys-ctd-meta`)

Parses CTD files and constructs metadata objects.

- **Input**: CTD source files (`.ctd`)
- **Output**: `DefinitionCollectionMeta` containing unresolved `*Meta` objects
- **Components**:
  - `MetaLoader` - Orchestrates file discovery and parsing
  - `MetaVisitor` - ANTLR4 visitor that transforms parse tree to Meta objects
  - `*Meta` classes - Lightweight metadata containers (strings, not resolved references)

### Stage 2: Declaration Construction (`cebbys-ctd-resolver` - Constructor Phase)

Remaps metadata to declaration objects and constructs type singletons.

- **Input**: `DefinitionCollectionMeta`
- **Output**: Type cache populated with `Declaration` singleton instances (`types/ctd/`)
- **Process**:
  - `constructor/` subpackage instantiates declarations from meta objects
  - Declarations are cached by qualified name (e.g., `std::lib::Int4`)
  - No type resolution occurs - references remain unresolved

### Stage 3: Reference Resolution (`cebbys-ctd-resolver` - Linker Phase)

Resolves all type references and establishes relationships between declarations.

- **Input**: Type cache with unresolved declarations
- **Output**: `Module` collection with fully resolved, immutable declarations
- **Process**:
  - `linker/` subpackage resolves type references
  - `Reference` objects link to cached declaration singletons
  - Namespace resolution applies (`use` declarations, qualified names)

### Pipeline Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              CTD Processing Pipeline                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CTD Files ──► Stage 1 ──► Stage 2 ──► Stage 3 ──► Module (collection)      │
│               (Loading)  (Constructor) (Linker)                             │
│                                                                             │
│  *.ctd    ──► *Meta     ──► Declaration ──► Resolved  ──► Immutable         │
│  files        objects       singletons      references    module            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Why Three Stages?

The separation enables:
- **Circular references**: Types can reference each other (e.g., linked list nodes)
- **Singleton guarantee**: Each type exists exactly once in memory
- **Clean resolution**: All types exist before any references are resolved

## Commands

```bash
# Sync workspace (install all dependencies)
uv sync --all-packages

# Run all tests from workspace root
uv run pytest -v

# Run tests for specific module
uv run pytest cebbys-ctd-antlr4/tests -v
uv run pytest cebbys-ctd-meta/tests -v
uv run pytest cebbys-ctd-resolver/tests -v

# Add dependency to specific package
uv add <package> --package cebbys-ctd-meta

# Regenerate ANTLR4 parser (requires antlr4-tools)
antlr4 -Dlanguage=Python3 -visitor resources/grammar/Ctd.g4 -o cebbys-ctd-antlr4/sources/lv/cebbys/languages/ctd/antlr4/__generated__
```

## Test Organization

Tests are organized by module and stage:

```
cebbys-ctd/
├── conftest.py                           # Shared fixtures (parse_ctd_file, TestLogger, etc.)
├── cebbys-ctd-antlr4/tests/             # ANTLR4 import tests
├── cebbys-ctd-meta/tests/               # Stage 1: Meta loading tests
│   ├── test_alias.py
│   ├── test_enum.py
│   ├── test_flag.py
│   ├── test_function.py
│   ├── test_interface.py
│   ├── test_structure.py
│   └── test_typedef.py
└── cebbys-ctd-resolver/tests/           # Stage 2-3: Construction & resolution tests
    ├── test_definition_creation.py      # Stage 2 tests
    └── test_type_resolution.py          # Stage 3 tests
```

### Test Imports

All tests import from the root `conftest.py`:

```python
from conftest import parse_ctd_file, TestLogger, get_resource_path
```

### Test Resources

Each module with tests has its own `resources/test/ctd/` directory with test CTD files.

## Git Workflow

### Pre-Commit Requirements

**IMPORTANT**: Always run tests before committing changes:

```bash
# Run all tests - MUST pass before commit
uv run pytest -v

# Only if ALL tests pass, proceed with commit
git add <files>
git commit -m "message"
```

**Never commit if tests are failing.** Fix the failing tests first.

### Git Notes

- Use `/dev/null` in Git Bash, not `nul`
- Commit changes after completing a task (per CLAUDE.md instructions)

## Implementation Guidelines

When implementing new language features, follow this incremental approach:

1. **Implement in order**: Meta Loading → Definition Construction → Reference Resolution
2. **Test each stage independently** before proceeding to the next
3. **Maintain module boundaries** so each step can be tested in isolation

**Example workflow for adding a new type (e.g., `union`)**:

1. **Step 1 - Meta Types** (`cebbys-ctd-types`):
   - Add `UnionMeta` class to `types/meta/union.py`
   - Update `types/meta/__init__.py` to export it

2. **Step 2 - Meta Loading** (`cebbys-ctd-meta`):
   - Update `visitor.py` to parse union declarations
   - Update `DefinitionCollectionMeta` to store unions
   - **Test**: Verify CTD files parse correctly

3. **Step 3 - Definition Types** (`cebbys-ctd-types`):
   - Add `Union` class to `types/ctd/union.py`
   - Update `types/ctd/__init__.py` to export it

4. **Step 4 - Resolver** (`cebbys-ctd-resolver`):
   - Add `UnionResolver` to `resolver/union.py`
   - Update `MetaResolver` to use it
   - **Test**: Verify definitions are created and resolved

5. **Step 5 - Module** (`cebbys-ctd-types`):
   - Update `Module` in `types/ctd/` to include unions

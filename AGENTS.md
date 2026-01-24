# cebbys-ctd

Custom Type Definition Language - A domain-specific language for defining custom datatypes.

## Project Structure

```
cebbys-ctd/
├── sources/                              # Source code root
│   └── lv/cebbys/languages/ctd/
│       ├── __api__.py                    # Common API types (FilePath, ModulePath)
│       ├── __init__.py                   # Package exports
│       ├── loader.py                     # Main CtdLoader entry point
│       ├── visitor.py                    # ANTLR4 visitor for parsing CTD files
│       │
│       ├── antlr4/                       # ANTLR4 generated parser
│       │   ├── __init__.py
│       │   ├── GtdLexer.py              # Generated lexer
│       │   ├── GtdParser.py             # Generated parser
│       │   ├── GtdListener.py           # Generated listener
│       │   └── GtdVisitor.py            # Generated visitor base
│       │
│       ├── define/                       # Resolved definition types
│       │   ├── __init__.py              # Package exports
│       │   ├── __api__.py               # Base classes (BaseDefinition, TypeSpec, etc.)
│       │   ├── typedef.py               # TypedefDefinition
│       │   ├── enum.py                  # EnumDefinition, EnumMemberDefinition
│       │   ├── flag.py                  # FlagDefinition, FlagMemberDefinition
│       │   ├── structure.py             # StructureDefinition, StructureMemberDefinition
│       │   ├── function.py              # FunctionDefinition, ParameterDefinition
│       │   └── collection.py            # DefinitionCollection
│       │
│       └── meta/                         # Metadata layer (pre-resolution)
│           ├── __init__.py              # Package exports (re-exports from loader/)
│           │
│           ├── loader/                   # Meta types and loader
│           │   ├── __init__.py          # Package exports
│           │   ├── __api__.py           # Common types (ModulePath)
│           │   ├── typedef.py           # TypedefMeta
│           │   ├── enum.py              # EnumMeta, EnumMemberMeta
│           │   ├── flag.py              # FlagMeta, FlagMemberMeta
│           │   ├── structure.py         # StructureMeta, StructureMemberMeta
│           │   ├── function.py          # FunctionMeta, ParameterMeta
│           │   ├── collection.py        # DefinitionCollectionMeta
│           │   └── loader.py            # MetaLoader for parsing files
│           │
│           └── resolver/                 # Type resolution
│               ├── __init__.py          # MetaResolver orchestrator
│               ├── __api__.py           # BaseResolver, ResolverContext
│               ├── typedef.py           # TypedefResolver
│               ├── enum.py              # EnumResolver
│               ├── flag.py              # FlagResolver
│               ├── structure.py         # StructureResolver
│               └── function.py          # FunctionResolver
│
├── tests/                                # Test files
│   ├── resources/ctd/                   # Test CTD files
│   └── test_*.py                        # Test modules
│
├── resources/                            # Resources
│   ├── grammar/Gtd.g4                   # ANTLR4 grammar definition
│   ├── ctd/                             # Sample CTD definition files
│   └── documents/                       # Documentation
│       └── ctd-language-syntax.md       # Language specification
│
└── hints/                                # Type stubs for external libraries
    └── antlr4/                          # ANTLR4 type hints
```

## Module Organization Conventions

The following packages follow a consistent module organization pattern:
- `define/` - Resolved definition types
- `meta/loader/` - Metadata types and file loader
- `meta/resolver/` - Type resolvers

### Module Structure Pattern

```
package/
├── __init__.py    # Imports and re-exports all public classes
├── __api__.py     # Common/base classes shared across the package
├── typedef.py     # TypedefDefinition (or TypedefMeta, TypedefResolver)
├── enum.py        # EnumDefinition, EnumMemberDefinition
├── flag.py        # FlagDefinition, FlagMemberDefinition
├── structure.py   # StructureDefinition, StructureMemberDefinition
├── function.py    # FunctionDefinition, ParameterDefinition
└── collection.py  # Collection class (if applicable)
```

### Rules

1. **One definition model per script**: Each type (typedef, enum, flag, structure, function) has its own dedicated script file.

2. **Common code in `__api__.py`**: Base classes, shared types, and common utilities are defined in `__api__.py`:
   - `define/__api__.py`: `BaseDefinition`, `BaseType`, `PrimitiveType`, `TypeReference`, `TypeSpec`
   - `meta/loader/__api__.py`: `ModulePath` (type alias)
   - `meta/resolver/__api__.py`: `BaseResolver`, `ResolverContext`, `ResolutionError`

3. **Package exports in `__init__.py`**: All public classes from individual scripts are imported and re-exported in `__init__.py` for convenient access:
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
   import lv.cebbys.languages.ctd.define as Define

   # Avoid
   import lv.cebbys.languages.ctd.define.typedef as Typedef
   ```

## Architecture

The project consists of 3 core modules that form a processing pipeline:

### Module 1: Meta Loading (`meta/loader/`)

Parses CTD files and constructs metadata objects.

- **Input**: CTD source files (`.ctd`)
- **Output**: `DefinitionCollectionMeta` containing unresolved `*Meta` objects
- **Components**:
  - `MetaLoader` - Orchestrates file discovery and parsing
  - `MetaVisitor` (in `visitor.py`) - ANTLR4 visitor that transforms parse tree to Meta objects
  - `*Meta` classes - Lightweight metadata containers (strings, not resolved references)

### Module 2: Definition Construction (`meta/resolver/` - Create Phase)

Remaps metadata to definition objects and constructs type singletons.

- **Input**: `DefinitionCollectionMeta`
- **Output**: Type cache populated with `*Definition` singleton instances
- **Process**:
  - Each resolver's `create_instances()` method instantiates definitions
  - Definitions are cached by qualified name (e.g., `std::lib::Int4`)
  - No type resolution occurs - references remain unresolved

### Module 3: Reference Resolution (`meta/resolver/` - Resolve Phase)

Resolves all type references and establishes relationships between definitions.

- **Input**: Type cache with unresolved definitions
- **Output**: `DefinitionCollection` with fully resolved, immutable definitions
- **Process**:
  - Each resolver's `resolve_instances()` method resolves type references
  - `TypeReference` objects link to cached definition singletons
  - Namespace resolution applies (`use` declarations, qualified names)

### Pipeline Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              CTD Processing Pipeline                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CTD Files ──► Module 1 ──► Module 2 ──► Module 3 ──► DefinitionCollection  │
│               (Loading)    (Construction) (Resolution)                      │
│                                                                             │
│  *.ctd    ──► *Meta     ──► *Definition ──► Resolved  ──► Immutable         │
│  files        objects       singletons      references    collection        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Why Three Modules?

The separation enables:
- **Circular references**: Types can reference each other (e.g., linked list nodes)
- **Singleton guarantee**: Each type exists exactly once in memory
- **Clean resolution**: All types exist before any references are resolved

### Implementation Guidelines

When implementing new language features, follow this incremental approach:

1. **Implement in order**: Meta Loading → Definition Construction → Reference Resolution
2. **Test each module independently** before proceeding to the next
3. **Maintain module boundaries** so each step can be tested in isolation

**Module Dependencies**:

```
Module 1 (Loading)       → Can be tested standalone
Module 2 (Construction)  → Requires Module 1
Module 3 (Resolution)    → Requires Module 1 + Module 2
```

**Example workflow for adding a new type (e.g., `interface`)**:

1. **Step 1 - Meta Loading**:
   - Add `InterfaceMeta` class to `meta/loader/interface.py`
   - Update `visitor.py` to parse interface declarations
   - Update `DefinitionCollectionMeta` to store interfaces
   - **Test**: Verify CTD files parse correctly and `InterfaceMeta` objects are created

2. **Step 2 - Definition Construction**:
   - Add `InterfaceDefinition` class to `define/interface.py`
   - Add `InterfaceResolver.create_instances()` to `meta/resolver/interface.py`
   - **Test**: Verify `InterfaceDefinition` singletons are created and cached

3. **Step 3 - Reference Resolution**:
   - Implement `InterfaceResolver.resolve_instances()`
   - Update `DefinitionCollection` to include interfaces
   - **Test**: Verify type references resolve correctly

## Commands

```bash
# Run all tests
python -m pytest tests/ -v

# Run tests by stage
python -m pytest tests/test_meta_loader/ -v     # Stage 1: Meta loading tests
python -m pytest tests/test_meta_parser/ -v     # Stage 2: Definition construction tests
python -m pytest tests/test_meta_resolver/ -v   # Stage 3: Type resolution tests

# Regenerate ANTLR4 parser (requires antlr4-tools)
antlr4 -Dlanguage=Python3 -visitor resources/grammar/Gtd.g4 -o sources/lv/cebbys/languages/ctd/antlr4
```

## Test Organization

Tests are organized into three stages matching the processing pipeline:

```
tests/
├── test_meta_loader/        # Stage 1: CTD file parsing → Meta objects
│   └── test_*.py
├── test_meta_parser/        # Stage 2: Meta objects → Definition instances
│   └── test_*.py            # (alias types resolved and removed at this stage)
├── test_meta_resolver/      # Stage 3: Definition resolution → Final collection
│   └── test_*.py
├── conftest.py              # Shared fixtures
└── test_utils.py            # Test utilities
```

### Stage 1: Meta Loading (`test_meta_loader/`)
Tests that CTD files are correctly parsed into `*Meta` objects:
- Grammar rules parse correctly
- `MetaVisitor` creates proper meta instances
- `DefinitionCollectionMeta` contains expected types
- All declaration types: typedef, alias, enum, flag, structure, interface, function

### Stage 2: Definition Construction (`test_meta_parser/`)
Tests that meta objects are correctly transformed into `*Definition` instances:
- `create_instances()` creates definition singletons
- Type cache is properly populated
- **Alias types are resolved and removed** (aliases become transparent references to target types)
- Definition objects exist but type references are not yet resolved

### Stage 3: Type Resolution (`test_meta_resolver/`)
Tests that type references are correctly resolved:
- `resolve_instances()` resolves all type references
- `TypeReference` objects point to correct singletons
- Namespace resolution works (use declarations, qualified names)
- `DefinitionCollection` is immutable and complete

## Git Workflow

### Pre-Commit Requirements

**IMPORTANT**: Always run tests before committing changes:

```bash
# Run all tests - MUST pass before commit
python -m pytest tests/ -v

# Only if ALL tests pass, proceed with commit
git add <files>
git commit -m "message"
```

**Never commit if tests are failing.** Fix the failing tests first.

### Git Notes

- Use `/dev/null` in Git Bash, not `nul`

# cebbys-ctd

Custom Type Definition Language - A domain-specific language for defining custom datatypes that can be loaded and instantiated as Python objects.

## Project Overview

This project implements a custom language for defining datatypes, which are parsed and interpreted into Python objects. The workflow consists of:

1. **Custom Language Definition**: Define datatypes using a custom DSL syntax
2. **Parsing with ANTLR4**: Parse the custom language files using ANTLR4 grammar
3. **Python Interpretation**: Interpret the parsed AST and instantiate Python objects
4. **Object Linking**: Link related objects and expose them for use in Python applications

## Technology Stack

- **ANTLR4**: Grammar definition and parsing
- **Python**: Runtime interpretation, instantiation, and object management
- **VSCode**: Development environment

## Project Structure

```
cebbys-ctd/
├── sources/                    # Source code root directory
│   └── lv/cebbys/languages/ctd/
│       ├── meta/              # Metadata types, loader, and resolver
│       │   ├── types.py       # Metadata model classes
│       │   ├── loader.py      # MetaLoader for parsing GTD files
│       │   └── resolver.py    # MetaResolver for type resolution
│       ├── define/            # Definition types (resolved)
│       │   └── types.py       # Definition model classes
│       ├── antlr4/            # ANTLR4 generated parser files
│       ├── loader.py          # Main CtdLoader
│       └── visitor.py         # ANTLR4 visitor implementation
├── tests/                      # Tests directory with subdirectories as test modules
├── resources/                  # Resources directory
│   ├── grammar/               # ANTLR4 grammar files (.g4)
│   └── ctd/                   # Custom type definition files (.gtd)
└── hints/                      # Type hints directory (not a source root)
    └── antlr4/                # ANTLR4 type stubs (.pyi files only)
```

## Architecture

### Module Organization

The project follows a structured architecture with clear separation of concerns:

- **meta/**: Contains metadata types and logic for loading and resolving GTD files
  - `types.py`: Model classes for parsed metadata (TypedefMeta, EnumMeta, FlagMeta, etc.)
  - `loader.py`: MetaLoader class for parsing GTD files into metadata
  - `resolver.py`: MetaResolver class for resolving type references into definitions

- **define/**: Contains resolved definition types
  - `types.py`: Model classes for resolved definitions (TypedefDefinition, EnumDefinition, etc.)

### Python Development Guidelines

1. **Import Statements**:
   - All imports must be defined at the top of the script file
   - Imports cannot be placed inside functions or methods
   - Follow standard import ordering:
     - Standard library imports (e.g., `import typing`, `import types`)
     - Third-party imports (e.g., `import antlr4`)
     - Local application imports (e.g., `import lv.cebbys.languages.ctd.meta`)
   - Use `as` aliases consistently (e.g., `import typing as Typing`)

2. **Model Classes Organization**:
   - Model classes shall reside in `{subdirectory}/types.py`
   - Example: `meta/types.py` for metadata models, `define/types.py` for definition models

3. **Package Structure**:
   - Each subdirectory with types should have an `__init__.py` that exports public API
   - Use relative imports within the same package
   - Use absolute imports from other packages

4. **Null Safety**:
   - If attributes can be `None`, it is necessary to verify they are not before use
   - Add null checks to avoid `AttributeError` exceptions when accessing optional attributes
   - Example:
     ```python
     if self._optional_attribute is None:
         raise SomeError("Attribute not initialized")
     # Safe to use self._optional_attribute here
     ```

5. **Source Roots**:
   - `sources/`: Primary source root for Python modules
   - `hints/`: Contains type stub modules (`.pyi` files only, not a source root)

6. **Testing**:
   - Tests organized in `tests/` directory
   - Each test file may contain multiple test functions
   - Use pytest for testing framework

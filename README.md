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
├── sources/          # Source code root directory
├── tests/            # Tests directory with subdirectories as test modules
├── resources/        # Resources directory containing ANTLR4 grammar files
└── hints/            # Type hints directory (not a source root)
    └── antlr4/       # ANTLR4 type stubs (.pyi files only)
```

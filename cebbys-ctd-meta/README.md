# CTD Meta Parser Module

This module provides context parsers that transform ANTLR4 parse tree contexts into CTD metadata objects.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Parser Module Architecture                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ANTLR4 Context ──► CtdContextParser ──► Meta Object                        │
│                                                                             │
│  ModuleDeclarationContext ──► CtdModuleContextParser ──► ModuleMeta         │
│  NamespaceDeclarationContext ──► CtdNamespaceContextParser ──► NamespaceMeta│
│  ImportDeclarationContext ──► CtdIncludeContextParser ──► IncludeMeta       │
│  TypedefDeclarationContext ──► CtdTypedefContextParser ──► TypedefMeta      │
│  TypeSpecContext ──► CtdTypeSpecContextParser ──► str                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Base Classes (`__api__.py`)

### ParserBase

Base class extending `CtdVisitor` with helper methods for navigating ANTLR4 parse trees:

| Method | Description |
|--------|-------------|
| `rules(ctx, look)` | Get all typed child rules of a specific type |
| `rule(ctx, look, index)` | Get a required typed child rule (raises if not found) |
| `optional_rule(ctx, look, index)` | Get an optional typed child rule (returns None if not found) |
| `tokens(ctx, token)` | Get all terminal nodes of a specific token type |
| `token(ctx, token, index)` | Get a required terminal node (raises if not found) |
| `optional_token(ctx, token, index)` | Get an optional terminal node (returns None if not found) |
| `text(ctx)` | Get text content (raises if not available) |
| `optional_text(ctx)` | Get optional text content (returns None if not available) |
| `qualified_name(ctx)` | Extract qualified name as `ns1::ns2::name` string |

### Parser Interfaces

```python
class CtdContextParser(Generic[R, O]):
    """Parser interface for context-to-output transformation."""

    @staticmethod
    def instance() -> CtdContextParser[R, O]: ...

    def parse(self, ctx: R) -> O: ...


class CtdDeclaractionContextParser(Generic[R, O]):
    """Parser interface for declarations that require namespace context."""

    @staticmethod
    def instance() -> CtdDeclaractionContextParser[R, O]: ...

    def parse(self, namespace: str, ctx: R) -> O: ...
```

### Implementation Base Classes

- `CtdContextParserBase[R, O]` - Combines `ParserBase` + `CtdContextParser[R, O]`
- `CtdDeclaractionContextParserBase[R, O]` - Combines `ParserBase` + `CtdDeclaractionContextParser[R, O]`

## Singleton Pattern

Each parser implementation uses a module-level singleton instance:

```python
class CtdTypedefContextParser(CtdDeclaractionContextParserBase[...]):
    @staticmethod
    def instance() -> CtdDeclaractionContextParser[...]:
        return INSTANCE

    def parse(self, namespace: str, ctx: ...) -> TypedefMeta:
        ...

INSTANCE = CtdTypedefContextParser()
```

Access parsers via the `instance()` static method:

```python
parser = CtdTypedefContextParser.instance()
result = parser.parse(namespace, ctx)
```

## Parser Implementations

### CtdModuleContextParser (`module.py`)

Root parser for `ModuleDeclarationContext`. Orchestrates parsing of the entire module:

- Delegates import declarations to `CtdIncludeContextParser`
- Delegates namespace declarations to `CtdNamespaceContextParser`
- Returns `ModuleMeta` containing all parsed includes and namespaces

### CtdNamespaceContextParser (`namespace.py`)

Parses `NamespaceDeclarationContext` with configurable declaration mappers:

```python
INSTANCE = CtdNamespaceContextParser({
    CtdParser.TypedefDeclarationContext: (
        CtdTypedefContextParser,
        lambda namespace: namespace.add_typedef
    )
})
```

The mapper dictionary maps:
- **Key**: ANTLR4 context type to match
- **Value**: Tuple of (parser class, consumer function factory)

This design allows easy extension for new declaration types (enum, flag, structure, etc.).

### CtdIncludeContextParser (`include.py`)

Parses `ImportDeclarationContext` to `IncludeMeta`:
- Extracts the import path from the string literal
- Returns configured `IncludeMeta` object

### CtdTypedefContextParser (`typedef.py`)

Parses `TypedefDeclarationContext` to `TypedefMeta`:
- Extracts typedef name from IDENTIFIER token
- Delegates type specification to `CtdTypeSpecContextParser`
- Returns `TypedefMeta` with name, typespec, and namespace

### CtdTypeSpecContextParser (`typespec.py`)

Parses `TypeSpecContext` to a string representation:
- Handles sign modifiers (`signed`, `unsigned`)
- Handles primitive types (`int`, `char`, etc.)
- Handles type references with qualified names
- Handles array modifiers (`[N]`)
- Handles pointer modifiers (`*`, `**`)

## Composition Pattern

Parsers compose by delegating to child parsers:

```
CtdModuleContextParser
├── CtdIncludeContextParser
└── CtdNamespaceContextParser
    └── CtdTypedefContextParser
        └── CtdTypeSpecContextParser
```

## Adding New Declaration Parsers

To add support for a new declaration type (e.g., `enum`):

1. Create `enum.py` with `CtdEnumContextParser`:
   ```python
   class CtdEnumContextParser(CtdDeclaractionContextParserBase[...]):
       @staticmethod
       def instance() -> ...: return INSTANCE

       def parse(self, namespace: str, ctx: ...) -> EnumMeta:
           ...

   INSTANCE = CtdEnumContextParser()
   ```

2. Register in `namespace.py`:
   ```python
   INSTANCE = CtdNamespaceContextParser({
       CtdParser.TypedefDeclarationContext: (
           CtdTypedefContextParser,
           lambda namespace: namespace.add_typedef
       ),
       CtdParser.EnumDeclarationContext: (
           CtdEnumContextParser,
           lambda namespace: namespace.add_enum
       )
   })
   ```

3. Export from `__init__.py` if needed for external access.

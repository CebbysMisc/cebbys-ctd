---
applyFor: "**/*.py, **/*.pyi"
---
# Python Development Instructions

## Python Project Configuration

### Source Roots

- **sources/**: Primary source root for Python modules
- **hints/<module_name>/**: Type stub directories for external libraries (contains `.pyi` files only)

The `hints/` directory itself is NOT a source root, but subdirectories within it (e.g., `hints/antlr4/`) are included in Python's extra paths.

### VSCode Python Settings

The project uses the following VSCode Python configuration (add all hint module subdirectories):

```json
{
    "python.analysis.extraPaths": [
        "${workspaceFolder}/sources",
        "${workspaceFolder}/hints/antlr4",
        "${workspaceFolder}/hints/<additional_module>"
    ],
    "python.autoComplete.extraPaths": [
        "${workspaceFolder}/sources",
        "${workspaceFolder}/hints/antlr4",
        "${workspaceFolder}/hints/<additional_module>"
    ]
}
```

## Testing

### Test Framework

- **Framework**: pytest
- **Test Location**: `tests/` directory
- **Organization**: Tests are organized in subdirectories as modules

### VSCode Test Configuration

```json
{
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests"],
    "python.testing.cwd": "${workspaceFolder}"
}
```

## Code Organization

### Design Principles

**REQUIRED**: Code must be highly object-oriented with strict adherence to Single Responsibility Principle (SRP):

- **One Class, One Task**: Each class should perform only one specific, well-defined task
- **Clear Responsibilities**: Class names should reflect their single responsibility
- **Encapsulation**: Group related data and behavior together in classes
- **Composition over Inheritance**: Prefer composing classes over deep inheritance hierarchies

**Examples**:
```python
# ✓ Good - Each class has a single responsibility
class DataParser:
    """Parses raw data into structured format."""
    def parse(self, raw_data: str) -> dict[str, Typing.Any]:
        pass

class DataValidator:
    """Validates parsed data against schema."""
    def validate(self, data: dict[str, Typing.Any]) -> bool:
        pass

class DataTransformer:
    """Transforms validated data into target format."""
    def transform(self, data: dict[str, Typing.Any]) -> dict[str, Typing.Any]:
        pass

class DataProcessor:
    """Orchestrates the data processing pipeline."""
    def __init__(self, parser: DataParser, validator: DataValidator, transformer: DataTransformer):
        self._parser = parser
        self._validator = validator
        self._transformer = transformer
    
    def process(self, raw_data: str) -> dict[str, Typing.Any]:
        parsed = self._parser.parse(raw_data)
        if not self._validator.validate(parsed):
            raise ValueError("Invalid data")
        return self._transformer.transform(parsed)

# ✗ Bad - Class doing multiple unrelated tasks
class DataHandler:
    """Anti-pattern: handles parsing, validation, transformation, and storage."""
    def parse(self, raw_data: str) -> dict[str, Typing.Any]:
        pass
    def validate(self, data: dict[str, Typing.Any]) -> bool:
        pass
    def transform(self, data: dict[str, Typing.Any]) -> dict[str, Typing.Any]:
        pass
    def save_to_database(self, data: dict[str, Typing.Any]) -> None:
        pass
```

### Module Structure

**REQUIRED**: Python modules must follow this specific structure:

#### Module Naming and Organization

**Module path convention**: `{namespace}/{path}/{or}/{full}/{group}/{path}/{module}/{name}`

Modules are organized hierarchically where each path segment represents a namespace or grouping, with the final segment being the module name.

**Project namespace**: `lv/cebbys/languages`

**Examples**:
```
sources/
├── lv/cebbys/languages/ctd/parser/           # Group: lv.cebbys.languages, Module: ctd.parser
├── lv/cebbys/languages/ctd/interpreter/      # Group: lv.cebbys.languages, Module: ctd.interpreter
└── lv/cebbys/languages/ctd/objects/types/    # Group: lv.cebbys.languages, Module: ctd.objects.types
```

#### File Organization

1. **`__init__.py`**: Module entry point
   - Imports all exposed code from module scripts
   - Defines `__all__` list with all exported symbols

2. **`__api__.py`**: Internal module API
   - Contains common API definitions shared across module scripts
   - Imported by script files within the same module

3. **Script files**: Implementation files
   - **Naming convention**: Place scripts directly in module directory or subdirectories
   - **NOT**: `the_awesome_script.py` (underscore-separated file names within paths)
   - Each script implements specific functionality following SRP

**Example structure**:
```
sources/
└── lv/
    └── cebbys/
        └── languages/
            └── ctd/
                └── dataprocessing/
                    ├── __init__.py       # Module entry point
                    ├── __api__.py        # Internal module API
                    ├── parser.py         # Implementation script
                    ├── validator.py      # Implementation script
                    └── transformer.py    # Implementation script
```

**`__init__.py` example**:
```python
# sources/lv/cebbys/languages/ctd/dataprocessing/__init__.py
import lv.cebbys.languages.ctd.dataprocessing.parser as Parser
import lv.cebbys.languages.ctd.dataprocessing.validator as Validator
import lv.cebbys.languages.ctd.dataprocessing.transformer as Transformer

__all__ = [
    'Parser',
    'Validator',
    'Transformer'
]
```

**`__api__.py` example**:
```python
# sources/lv/cebbys/languages/ctd/dataprocessing/__api__.py
import typing as Typing

# Common types used across the module
DataDict = dict[str, Typing.Any]
ValidationResult = tuple[bool, str]

# Common constants
MAX_RECORDS = 1000
```

**Script file example**:
```python
# sources/lv/cebbys/languages/ctd/dataprocessing/parser.py
import typing as Typing
import lv.cebbys.languages.ctd.dataprocessing.__api__ as Api

__all__ = ['DataParser']

class DataParser:
    """Parses raw data into structured format."""
    def parse(self, raw_data: str) -> Api.DataDict:
        result: Api.DataDict
        result = {}
        # Implementation
        return result
```

#### General Guidelines

- Place all application code in `sources/`
- Keep ANTLR4-generated code separate from custom implementation code
- Use directory hierarchy naturally with forward-slash style script naming

### Type Hints

- Use type hints throughout the codebase
- Type stubs for external libraries go in `hints/<module_name>/` as `.pyi` files
- Follow PEP 484 type hinting conventions
- Use built-in types (`list`, `dict`, `type`) instead of `Typing.List`, `Typing.Dict`, etc.

### Generic Type Parameters

**PREFERRED**: Use PEP 695 syntax for generic functions:

```python
def get_first[T](items: list[T]) -> T:
    return items[0]

def map_values[K, V](data: dict[K, V], func: Typing.Callable[[V], V]) -> dict[K, V]:
    return {k: func(v) for k, v in data.items()}
```

**USE TypeVar ONLY** when the type parameter needs to be bound or constrained:

```python
import typing as Typing

# Constrained TypeVar - only use when necessary
T = Typing.TypeVar('T', int, str)  # T can only be int or str

def process_value(value: T) -> T:
    return value

# Bound TypeVar - only use when necessary
Comparable = Typing.TypeVar('Comparable', bound=Typing.Protocol)

def get_max(a: Comparable, b: Comparable) -> Comparable:
    return a if a > b else b
```

### Type Annotations for Variables

**REQUIRED**: All variables must have type annotations when the type cannot be implicitly interpreted.

**Rules**:
- ✓ **Skip annotation** when assigning from a function return (type is inferred)
- ✓ **Add annotation** for local variables where type cannot be inferred
- ✓ **Declare at function start** using type decorators when possible
- ✗ **Exception**: Same variable name used for multiple datatypes (use inline annotations)

**Examples**:
```python
# mymodule.py
import typing as Typing

def process_data(data: str) -> int:
    # Local variable type annotations declared at start
    result: int
    temp_value: str
    items: list[str]
    
    # No annotation needed - inferred from function return
    length = len(data)
    
    # Explicit annotation for local variable
    result = 0
    temp_value = data.strip()
    items = temp_value.split(',')
    
    # Process items
    for item in items:
        result += int(item)
    
    return result

def mixed_types(flag: bool) -> Typing.Any:
    # Exception: variable used for different types - inline annotation
    # Note: This function requires a .pyi file because return type varies by input
    if flag:
        value: int = 42
    else:
        value: str = "text"
    return value
```

```python
# mymodule.pyi
import typing as Typing

@Typing.overload
def mixed_types(flag: Typing.Literal[True]) -> int: ...

@Typing.overload
def mixed_types(flag: Typing.Literal[False]) -> str: ...

@Typing.overload
def mixed_types(flag: bool) -> int | str: ...
```

## ANTLR4 Integration

### Generated Code Location

- Generated parser/lexer code should be placed in `sources/` (or a subdirectory)
- Keep generated code separate from hand-written code

### Grammar Files

- Store ANTLR4 grammar files (`.g4`) in `resources/`
- Document grammar changes in comments

## Coding Standards

### Import Style

**REQUIRED**: All imports must follow this template:

**In `.py` files**:
```python
import module as Module
```

**In `.pyi` files** (stub files):
```python
import module as _Module
```

The underscore prefix in `.pyi` files prevents the imported module from being re-exported.

**PROHIBITED**: Do NOT use `from module import A` style imports.

**Examples**:
```python
# ✓ Correct - .py file
import typing as Typing
import collections as Collections

# ✓ Correct - .pyi file
import typing as _Typing
import collections as _Collections

# ✗ Incorrect
from typing import List, Dict
from collections import defaultdict
```

### Module Exports

**REQUIRED**: Every script must define `__all__` to explicitly declare exported members:

```python
__all__ = ['MyClass', 'my_function', 'CONSTANT']
```

This controls what is exposed when the module is imported.

### Callback Type Definitions

**REQUIRED**: When a function accepts a callback as an argument, define the callback type using `Typing.Callable` at the top of the `.py` or `.pyi` file.

**Examples**:
```python
# mymodule.py
import typing as Typing

# Define callback types at the top of the file
ProcessCallback = Typing.Callable[[str, int], bool]
ErrorHandler = Typing.Callable[[Exception], None]
OperationCallback = Typing.Callable[[], None]
DataTransform = Typing.Callable[[dict[str, Typing.Any]], dict[str, Typing.Any]]

def process_items(items: list[str], callback: ProcessCallback) -> None:
    """Process items using the provided callback."""
    for index, item in enumerate(items):
        if not callback(item, index):
            break

def handle_errors(operation: OperationCallback, on_error: ErrorHandler) -> None:
    """Execute operation with error handling."""
    try:
        operation()
    except Exception as e:
        on_error(e)

def transform_data(data: list[dict[str, Typing.Any]], transformer: DataTransform) -> list[dict[str, Typing.Any]]:
    """Apply transformation to each data item."""
    result: list[dict[str, Typing.Any]]
    result = []
    for item in data:
        result.append(transformer(item))
    return result
```

### Function Overloads

When a function has multiple signatures (overloads), follow this pattern:

1. **Create a `.pyi` stub file** alongside the `.py` file with `@overload` decorators:

```python
# mymodule.pyi
import typing as _Typing

@_Typing.overload
def fun(x: int) -> str: ...

@_Typing.overload
def fun(x: int, y: int) -> str: ...

@_Typing.overload
def fun(x: str, y: str) -> str: ...
```

2. **In the `.py` file**, define the function with generic signature and runtime dispatch:

```python
# mymodule.py
import typing as Typing

def fun(*arguments: Typing.Any) -> Typing.Any:
    # Declare local variable types at function start
    length: int
    x: int | str
    y: int | str
    arg_types: tuple[type, ...]
    
    length = len(arguments)
    if length == 1 and isinstance(arguments[0], int):
        # Overload: fun(x: int)
        x = arguments[0]
        return str(x)
    elif length == 2 and isinstance(arguments[0], int) and isinstance(arguments[1], int):
        # Overload: fun(x: int, y: int)
        x, y = arguments[0], arguments[1]
        return str(x + y)
    elif length == 2 and isinstance(arguments[0], str) and isinstance(arguments[1], str):
        # Overload: fun(x: str, y: str)
        x, y = arguments[0], arguments[1]
        return x + y
    
    # No matching overload found
    arg_types = tuple(type(arg) for arg in arguments)
    raise TypeError(f"Function implementation not found for {arg_types}")
```

**Key requirements for overload validation**:
- When multiple overloads have the same argument count, check argument types explicitly
- If no overload matches, raise `TypeError` at the end with message: `Function implementation not found for {arg_types}`
- Always report all argument types in the error message, regardless of error type
- Use `isinstance()` to validate argument types at runtime

## Best Practices

1. **Imports**: Use absolute imports from the `sources/` root with `import module as Module` style
2. **Exports**: Always define `__all__` to control module interface
3. **Testing**: Write tests for all interpreter and linking logic
4. **Type Safety**: Leverage type hints and stubs for better IDE support
5. **Overloads**: Use `.pyi` files for overloaded functions with runtime dispatch in `.py` files
6. **Documentation**: Document complex parsing and interpretation logic
7. **Separation**: Keep parsing (ANTLR4) separate from interpretation (Python)

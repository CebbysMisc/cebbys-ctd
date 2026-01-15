# GTD Language Specification

## Overview

GTD (Generic Type Definition) is a custom domain-specific language for defining datatypes. Files use the `.gtd` extension and contain type definitions organized within namespaces.

## File Structure

### Namespace Declaration

Files are organized using namespace declarations with double-colon (`::`​) separators:

```gtd
namespace lv::cebbys::types {
    // Type definitions go here
}
```

### Type Definitions

#### typedef Statement

The `typedef` keyword defines type aliases mapping source types to target type names.

**Syntax**:
```
typedef <source_type> <target_name>
```

**Example from `cebbys-types.gtd`**:
```gtd
namespace lv::cebbys::types {
    typedef signed char     Snt1
    typedef signed short    Snt2
    typedef signed int      Snt4
    typedef signed long     Snt8

    typedef unsigned char   Unt1
    typedef unsigned short  Unt2
    typedef unsigned int    Unt4
    typedef unsigned long   Unt8

    typedef void            Void
}
```

## Language Elements

### Keywords

- `namespace` - Declares a namespace scope
- `typedef` - Defines a type alias

### Type Modifiers

- `signed` - Indicates a signed numeric type
- `unsigned` - Indicates an unsigned numeric type

### Primitive Types

- `char` - Character type (1 byte)
- `short` - Short integer type (2 bytes)
- `int` - Integer type (4 bytes)
- `long` - Long integer type (8 bytes)
- `void` - Void type (no value)

### Namespace Separator

- `::` - Separates namespace path components

## Naming Conventions

Type names follow specific patterns:
- **Signed types**: `Snt<N>` where N is byte size (1, 2, 4, 8)
- **Unsigned types**: `Unt<N>` where N is byte size (1, 2, 4, 8)
- **Special types**: `Void` for void type

## File: cebbys-types.gtd

This file defines fundamental numeric and void type aliases under the `lv::cebbys::types` namespace:

| Type Name | Source Type      | Size  | Description           |
|-----------|------------------|-------|-----------------------|
| Snt1      | signed char      | 1 byte | Signed 8-bit integer |
| Snt2      | signed short     | 2 bytes| Signed 16-bit integer|
| Snt4      | signed int       | 4 bytes| Signed 32-bit integer|
| Snt8      | signed long      | 8 bytes| Signed 64-bit integer|
| Unt1      | unsigned char    | 1 byte | Unsigned 8-bit integer|
| Unt2      | unsigned short   | 2 bytes| Unsigned 16-bit integer|
| Unt4      | unsigned int     | 4 bytes| Unsigned 32-bit integer|
| Unt8      | unsigned long    | 8 bytes| Unsigned 64-bit integer|
| Void      | void             | -      | Void type            |

## Purpose

These type definitions provide a consistent, platform-independent naming scheme for fundamental datatypes that can be parsed by ANTLR4 and instantiated as Python objects.

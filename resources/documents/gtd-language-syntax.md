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
typedef <type_reference> <target_name>
```

**Examples**:
```gtd
namespace lv::cebbys::types {
    // With sign modifiers
    typedef signed char     Snt1
    typedef unsigned int    Unt4
    
    // Without sign modifiers (defaults to signed)
    typedef char            Int1
    typedef int             Int4
    
    // Void type
    typedef void            Void
    
    // Pointer types
    typedef Void*           Any
}
```

#### enum Statement

The `enum` keyword defines enumeration types with named constant values.

**Syntax**:
```
enum <name> : <underlying_type> {
    <member> = <value>
    <member> = <value>
}
```

Note: Enum members are separated by newlines, not commas.

**Example**:
```gtd
namespace lv::cebbys::types {
    enum Null : Int4 {
        NULL = 0
    }
}
```

## Language Elements

### Keywords

- `namespace` - Declares a namespace scope
- `typedef` - Defines a type alias
- `enum` - Defines an enumeration type

### Type Modifiers

- `signed` - Indicates a signed numeric type (optional, default for primitive types)
- `unsigned` - Indicates an unsigned numeric type
- `*` - Pointer modifier (suffix)

### Primitive Types

- `char` - Character type (1 byte)
- `short` - Short integer type (2 bytes)
- `int` - Integer type (4 bytes)
- `long` - Long integer type (8 bytes)
- `void` - Void type (no value)

### Type References

Previously defined types can be referenced by name:
```gtd
typedef Void*           Any      // References the Void type
enum Null : Int4 { ... }        // References the Int4 type
```

### Namespace Separator

- `::` - Separates namespace path components

## Namespace Resolution

### Type Reference Resolution Rules

When a type is referenced in a GTD file, it is resolved using the following priority order:

1. **Current Namespace** - Types defined in the same namespace as the reference
2. **Used Namespaces** - Types from namespaces explicitly imported with `use` declarations
3. **Fully Qualified Names** - Types referenced with their complete namespace path

**IMPORTANT**: Global type search is NOT supported. Types from other namespaces MUST be:
- Explicitly imported with a `use` declaration, OR
- Referenced with their fully qualified name

### Use Declaration

The `use` keyword imports types from another namespace into the current scope:

**Syntax**:
```
use <qualified_namespace>
```

**Examples**:
```gtd
namespace com::example::app {
    use com::example::lib
    use com::example::utils

    // Now can reference types from com::example::lib and com::example::utils
    // without qualification
}
```

### Type Reference Examples

#### Example 1: Same Namespace (Always Works)
```gtd
namespace com::example::lib {
    typedef int Int4
    typedef Int4 Integer  // ✓ Works - Int4 is in same namespace
}
```

#### Example 2: Different Namespace Without Use (Fails)
```gtd
namespace com::example::lib {
    structure Adapter {
        int vtable
    }
}

namespace com::example::app {
    // ✗ FAILS - Adapter is not in current namespace or used namespaces
    structure Config {
        Adapter adapter
    }
}
```

#### Example 3: Different Namespace With Use Declaration (Works)
```gtd
namespace com::example::lib {
    structure Adapter {
        int vtable
    }
}

namespace com::example::app {
    use com::example::lib

    // ✓ Works - com::example::lib is imported via use
    structure Config {
        Adapter adapter
    }
}
```

#### Example 4: Different Namespace With Qualified Name (Works)
```gtd
namespace com::example::lib {
    structure Adapter {
        int vtable
    }
}

namespace com::example::app {
    // ✓ Works - Fully qualified name used
    structure Config {
        com::example::lib::Adapter adapter
    }
}
```

### Import vs Use

GTD distinguishes between file imports and namespace usage:

- **`import "filename"`** - Includes another GTD file for parsing
- **`use namespace::path`** - Makes types from a namespace available in current scope

**Example**:
```gtd
import "std-types"  // Include the std-types.gtd file

namespace com::example::app {
    use std::lib  // Make std::lib types available without qualification

    typedef Unt4 UnsignedInt  // ✓ Works - std::lib imported via use
}
```

## Naming Conventions

Type names follow specific patterns:
- **Signed types**: `Snt<N>` where N is byte size (1, 2, 4, 8)
- **Unsigned types**: `Unt<N>` where N is byte size (1, 2, 4, 8)
- **Plain integer types**: `Int<N>` where N is byte size (1, 2, 4, 8)
- **Special types**: `Void` for void type, `Any` for void pointer
- **Enum types**: PascalCase naming (e.g., `Null`)

## File: cebbys-types.gtd

This file defines fundamental numeric and void type aliases under the `lv::cebbys::types` namespace:

| Type Name | Source Type      | Size    | Description              |
|-----------|------------------|---------|--------------------------|
| Snt1      | signed char      | 1 byte  | Signed 8-bit integer     |
| Snt2      | signed short     | 2 bytes | Signed 16-bit integer    |
| Snt4      | signed int       | 4 bytes | Signed 32-bit integer    |
| Snt8      | signed long      | 8 bytes | Signed 64-bit integer    |
| Unt1      | unsigned char    | 1 byte  | Unsigned 8-bit integer   |
| Unt2      | unsigned short   | 2 bytes | Unsigned 16-bit integer  |
| Unt4      | unsigned int     | 4 bytes | Unsigned 32-bit integer  |
| Unt8      | unsigned long    | 8 bytes | Unsigned 64-bit integer  |
| Int1      | char             | 1 byte  | Default 8-bit integer    |
| Int2      | short            | 2 bytes | Default 16-bit integer   |
| Int4      | int              | 4 bytes | Default 32-bit integer   |
| Int8      | long             | 8 bytes | Default 64-bit integer   |
| Void      | void             | -       | Void type                |
| Any       | Void*            | ptr     | Void pointer (any type)  |
| Null      | enum : Int4      | 4 bytes | Null enumeration (NULL=0)|

## Purpose

These type definitions provide a consistent, platform-independent naming scheme for fundamental datatypes that can be parsed by ANTLR4 and instantiated as Python objects.

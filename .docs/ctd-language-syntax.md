# CTD Language Specification

## Table of Contents

- [Overview](#overview)
- [File Structure](#file-structure)
  - [Namespace Declaration](#namespace-declaration)
  - [Type Definitions](#type-definitions)
    - [typedef Statement](#typedef-statement)
    - [alias Statement](#alias-statement)
    - [enum Statement](#enum-statement)
    - [flag Statement](#flag-statement)
    - [structure Statement](#structure-statement)
    - [function Statement](#function-statement)
    - [interface Statement](#interface-statement)
- [Annotations](#annotations)
- [Language Elements](#language-elements)
  - [Keywords](#keywords)
  - [Type Modifiers](#type-modifiers)
  - [Primitive Types](#primitive-types)
  - [Type References](#type-references)
  - [Namespace Separator](#namespace-separator)
- [Namespace Resolution](#namespace-resolution)
  - [Type Reference Resolution Rules](#type-reference-resolution-rules)
  - [Use Declaration](#use-declaration)
  - [Type Reference Examples](#type-reference-examples)
    - [Example 1: Same Namespace (Always Works)](#example-1-same-namespace-always-works)
    - [Example 2: Different Namespace Without Use (Fails)](#example-2-different-namespace-without-use-fails)
    - [Example 3: Different Namespace With Use Declaration (Works)](#example-3-different-namespace-with-use-declaration-works)
    - [Example 4: Different Namespace With Qualified Name (Works)](#example-4-different-namespace-with-qualified-name-works)
  - [Import vs Use](#import-vs-use)
- [Naming Conventions](#naming-conventions)
- [File: std-types.ctd](#file-std-typesctd)
- [Purpose](#purpose)

---

## Overview

CTD (Custom Type Definition) is a custom domain-specific language for defining datatypes. Files use the `.ctd` extension and contain type definitions organized within namespaces.

[Back to Table of Contents](#table-of-contents)

---

## File Structure

### Namespace Declaration

Files are organized using namespace declarations with double-colon (`::`) separators:

```ctd
namespace lv::cebbys::types {
    // Type definitions go here
}
```

### Type Definitions

#### typedef Statement

The `typedef` keyword defines a **new type** based on an existing type. The resulting type is considered a distinct type in the type system.

**Syntax**:
```
typedef <source_type> <target_name>
typedef <type_reference> <target_name>
```

**Examples**:
```ctd
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

#### alias Statement

The `alias` keyword creates a **transparent type alias** that resolves directly to the underlying type. Unlike `typedef`, an alias does not create a new type - it simply provides an alternative name that will be replaced with the actual type during resolution.

**Key Difference from typedef**:
- `typedef Int4 MyInt` - Creates a new type `MyInt` (distinct from `Int4`)
- `alias Int4 MyInt` - `MyInt` is just another name for `Int4` (transparent)

**Syntax**:
```
alias <source_type> <alias_name>
```

**Examples**:
```ctd
namespace com::microsoft::windows::guid {
    typedef Guid InterfaceId   // InterfaceId is a new type based on Guid

    alias InterfaceId IID      // IID resolves directly to InterfaceId (then to Guid)
    alias IID* REFIID          // REFIID resolves to pointer to InterfaceId
}
```

**Use Case**: Aliases are useful for temporary type renaming during parsing, or for creating shorthand names that should resolve to the original type rather than creating a new type hierarchy.

#### enum Statement

The `enum` keyword defines enumeration types with named constant values.

**Syntax**:
```
enum <name> : <underlying_type> {
    <member> = <value>
    <member> = <value>
}
```

Note: Enum members are separated by newlines, not commas. Values auto-increment from the previous value if not specified.

**Example**:
```ctd
namespace lv::cebbys::types {
    enum Null : Int4 {
        NULL = 0
    }

    enum DriverType : Int4 {
        UNKNOWN = 0
        HARDWARE        // Auto-increments to 1
        REFERENCE       // Auto-increments to 2
        NULL            // Auto-increments to 3
        SOFTWARE        // Auto-increments to 4
        WARP            // Auto-increments to 5
    }
}
```

#### flag Statement

The `flag` keyword defines bit flag types with bit-shifted values.

**Syntax**:
```
flag <name> : <underlying_type> {
    <member>
    <member> = <bit_offset>
    <member>
}
```

Note: Flag members are bit-shifted (1 << index). Manual offset values can be specified, and subsequent members continue from there.

**Example**:
```ctd
namespace com::example::types {
    flag CreateDeviceFlag : Unt4 {
        SINGLETHREADED              // 0x1 (1 << 0)
        DEBUG                       // 0x2 (1 << 1)
        SWITCH_TO_REF               // 0x4 (1 << 2)
        PREVENT_THREADING = 3       // 0x8 (1 << 3)
        BGRA_SUPPORT = 5            // 0x20 (1 << 5) - manual offset
        DEBUGGABLE                  // 0x40 (1 << 6)
    }
}
```

#### structure Statement

The `structure` keyword defines composite types with named members.

**Syntax**:
```
structure <name> {
    <type> <member_name>
    <type> <member_name>
}
```

**Example**:
```ctd
namespace com::example::types {
    structure Rational {
        Unt4 numerator
        Unt4 denominator
    }

    structure Config {
        Rational* ratio      // Pointer to Rational
        Unt4 flags
        int refCount
    }
}
```

#### function Statement

The `function` keyword (implicit - no keyword needed) defines function declarations with return type, name, and parameters.

**Syntax**:
```
[@annotation]
<return_type> <function_name>(<parameter_list>)
```

Where `<parameter_list>` is:
```
[@annotation] <type> <name>, [@annotation] <type> <name>, ...
```

**Example**:
```ctd
namespace com::example::api {
    use com::example::types

    @WinApi
    ResultCode CreateDevice(
        @Nullable Adapter* adapter,
        DriverType driverType,
        CreateDeviceFlag flags,
        Unt4 sdkVersion
    )
}
```

#### interface Statement

The `interface` keyword defines COM-style interfaces with method declarations.

**Syntax**:
```
interface <name> {
    <method_declaration>
    <method_declaration>
    ...
}
```

Where each `<method_declaration>` follows the function syntax.

**Example**:
```ctd
namespace com::microsoft::windows {
    interface IUnknown {
        @Virtual @StdCall HandleResult QueryInterface(
            REFIID interfaceId,
            Any* vtable
        )

        @Virtual @StdCall Unt4 AddRef()

        @Virtual @StdCall Unt4 Release()
    }
}
```

[Back to Table of Contents](#table-of-contents)

---

## Annotations

Annotations (also called decorators) provide metadata for functions and parameters.

**Syntax**:
```
@<annotation_name>
@<annotation_name>(<arguments>)
```

**Usage**:
- **Function annotations**: Placed before the return type
- **Parameter annotations**: Placed before the parameter type

**Common Annotations**:
- `@WinApi` - Indicates a Windows API calling convention
- `@Nullable` - Indicates a parameter can be null

**Example**:
```ctd
namespace com::example::api {
    @WinApi
    ResultCode Initialize(
        @Storage("reg", "ecx") @Nullable Config* config,
        @Storage("stack", 0x0) Unt4 flags
    )
}
```

Note: Annotations are stored as string metadata and their interpretation is left to the consuming application.

[Back to Table of Contents](#table-of-contents)

---

## Language Elements

### Keywords

- `namespace` - Declares a namespace scope
- `typedef` - Defines a new type based on an existing type
- `alias` - Defines a transparent type alias (resolves to underlying type)
- `enum` - Defines an enumeration type
- `flag` - Defines a bit flag type
- `structure` - Defines a composite type
- `interface` - Defines an interface with method declarations
- `use` - Imports a namespace into scope
- `import` - Includes another CTD file

### Type Modifiers

- `signed` - Indicates a signed numeric type (optional, default for primitive types)
- `unsigned` - Indicates an unsigned numeric type
- `*` - Pointer modifier (suffix), can be chained with arrays in any combination
- `[N]` - Array modifier (suffix) - defines a fixed-size array of N elements

**Type Extensions**:

Type extensions can be chained arbitrarily to create complex types. Each extension modifies the type to its left:
- `*` - Creates a pointer to the type
- `[N]` - Creates a fixed-size array of N elements

Extensions are applied left-to-right, so `int[3]*` is "array of 3 ints, then pointer" (pointer to array), while `int*[3]` is "int pointer, then array of 3" (array of 3 pointers).

**Type Extension Examples**:
```ctd
structure ComplexTypes {
    Unt1[8]         simple_array        // Array of 8 bytes
    Unt4*           simple_pointer      // Pointer to Unt4
    Unt4**          double_pointer      // Pointer to pointer to Unt4
    int[3]*         ptr_to_array        // Pointer to array of 3 ints
    int*[4]         array_of_ptrs       // Array of 4 int pointers
    int[3]**[4]*    complex_type        // Complex chained extensions:
                                        // 1. int[3] - array of 3 ints
                                        // 2. int[3]* - pointer to array of 3 ints
                                        // 3. int[3]** - pointer to pointer to array of 3 ints
                                        // 4. int[3]**[4] - array of 4 pointers to pointers to arrays
                                        // 5. int[3]**[4]* - pointer to array of 4 pointers to pointers to arrays
}
```

**Reading Complex Types**: Read from left to right, applying each modifier:
- `int[3]**[4]*[12]` reads as:
  1. Start with `int`
  2. `[3]` → array of 3 ints
  3. `*` → pointer to (array of 3 ints)
  4. `*` → pointer to pointer to (array of 3 ints)
  5. `[4]` → array of 4 (pointers to pointers to arrays of 3 ints)
  6. `*` → pointer to (array of 4 pointers to pointers to arrays of 3 ints)
  7. `[12]` → array of 12 (pointers to arrays of 4 pointers to pointers to arrays of 3 ints)

### Primitive Types

- `char` - Character type (1 byte)
- `short` - Short integer type (2 bytes)
- `int` - Integer type (4 bytes)
- `long` - Long integer type (8 bytes)
- `void` - Void type (no value)

### Type References

Previously defined types can be referenced by name:
```ctd
typedef Void*           Any      // References the Void type
enum Null : Int4 { ... }        // References the Int4 type
```

### Namespace Separator

- `::` - Separates namespace path components

[Back to Table of Contents](#table-of-contents)

---

## Namespace Resolution

### Type Reference Resolution Rules

When a type is referenced in a CTD file, it is resolved using the following priority order:

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
```ctd
namespace com::example::app {
    use com::example::lib
    use com::example::utils

    // Now can reference types from com::example::lib and com::example::utils
    // without qualification
}
```

### Type Reference Examples

#### Example 1: Same Namespace (Always Works)
```ctd
namespace com::example::lib {
    typedef int Int4
    typedef Int4 Integer  // Works - Int4 is in same namespace
}
```

#### Example 2: Different Namespace Without Use (Fails)
```ctd
namespace com::example::lib {
    structure Adapter {
        int vtable
    }
}

namespace com::example::app {
    // FAILS - Adapter is not in current namespace or used namespaces
    structure Config {
        Adapter adapter
    }
}
```

#### Example 3: Different Namespace With Use Declaration (Works)
```ctd
namespace com::example::lib {
    structure Adapter {
        int vtable
    }
}

namespace com::example::app {
    use com::example::lib

    // Works - com::example::lib is imported via use
    structure Config {
        Adapter adapter
    }
}
```

#### Example 4: Different Namespace With Qualified Name (Works)
```ctd
namespace com::example::lib {
    structure Adapter {
        int vtable
    }
}

namespace com::example::app {
    // Works - Fully qualified name used
    structure Config {
        com::example::lib::Adapter adapter
    }
}
```

### Import vs Use

CTD distinguishes between file imports and namespace usage:

- **`import "filename"`** - Includes another CTD file for parsing
- **`use namespace::path`** - Makes types from a namespace available in current scope

**Example**:
```ctd
import "std-types"  // Include the std-types.ctd file

namespace com::example::app {
    use std::lib  // Make std::lib types available without qualification

    typedef Unt4 UnsignedInt  // Works - std::lib imported via use
}
```

[Back to Table of Contents](#table-of-contents)

---

## Naming Conventions

Type names follow specific patterns:
- **Signed types**: `Snt<N>` where N is byte size (1, 2, 4, 8)
- **Unsigned types**: `Unt<N>` where N is byte size (1, 2, 4, 8)
- **Plain integer types**: `Int<N>` where N is byte size (1, 2, 4, 8)
- **Special types**: `Void` for void type, `Any` for void pointer
- **Enum types**: PascalCase naming (e.g., `Null`)

[Back to Table of Contents](#table-of-contents)

---

## File: std-types.ctd

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

[Back to Table of Contents](#table-of-contents)

---

## Purpose

These type definitions provide a consistent, platform-independent naming scheme for fundamental datatypes that can be parsed by ANTLR4 and instantiated as Python objects.

[Back to Table of Contents](#table-of-contents)

"""Tests for MetaParser parsing methods."""
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


class TestParseCompilationUnit:
    """Tests for parseCompilationUnit method."""

    def test_parse_empty_compilation_unit(self) -> None:
        """Test parsing an empty compilation unit."""
        TestLogger.header("MetaParser: Empty Compilation Unit")

        parser = Meta.MetaParser()
        result = parser.parseCompilationUnit("")

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.CompilationUnitContext)
        TestLogger.success("Empty compilation unit parsed successfully")
        TestLogger.complete()

    def test_parse_compilation_unit_with_namespace(self) -> None:
        """Test parsing a compilation unit with a namespace."""
        TestLogger.header("MetaParser: Compilation Unit with Namespace")

        parser = Meta.MetaParser()
        result = parser.parseCompilationUnit('''
            namespace test::example {
                typedef int MyInt
            }
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.CompilationUnitContext)
        TestLogger.success("Compilation unit with namespace parsed")
        TestLogger.complete()

    def test_parse_compilation_unit_with_import(self) -> None:
        """Test parsing a compilation unit with imports."""
        TestLogger.header("MetaParser: Compilation Unit with Import")

        parser = Meta.MetaParser()
        result = parser.parseCompilationUnit('''
            import "std-types"

            namespace test {
                typedef Int4 MyInt
            }
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.CompilationUnitContext)
        TestLogger.success("Compilation unit with import parsed")
        TestLogger.complete()


class TestParseNamespaceDeclaration:
    """Tests for parseNamespaceDeclaration method."""

    def test_parse_simple_namespace(self) -> None:
        """Test parsing a simple namespace."""
        TestLogger.header("MetaParser: Simple Namespace")

        parser = Meta.MetaParser()
        result = parser.parseNamespaceDeclaration('''
            namespace example {
                typedef int MyInt
            }
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.NamespaceDeclarationContext)
        TestLogger.success("Simple namespace parsed")
        TestLogger.complete()

    def test_parse_nested_namespace(self) -> None:
        """Test parsing a nested namespace."""
        TestLogger.header("MetaParser: Nested Namespace")

        parser = Meta.MetaParser()
        result = parser.parseNamespaceDeclaration('''
            namespace foo::bar::baz {
                typedef int MyInt
            }
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.NamespaceDeclarationContext)
        TestLogger.success("Nested namespace parsed")
        TestLogger.complete()


class TestParseTypedefDeclaration:
    """Tests for parseTypedefDeclaration method."""

    def test_parse_simple_typedef(self) -> None:
        """Test parsing a simple typedef."""
        TestLogger.header("MetaParser: Simple Typedef")

        parser = Meta.MetaParser()
        result = parser.parseTypedefDeclaration("typedef int MyInt")

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.TypedefDeclarationContext)
        TestLogger.success("Simple typedef parsed")
        TestLogger.complete()

    def test_parse_signed_typedef(self) -> None:
        """Test parsing a signed typedef."""
        TestLogger.header("MetaParser: Signed Typedef")

        parser = Meta.MetaParser()
        result = parser.parseTypedefDeclaration("typedef signed int Snt4")

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.TypedefDeclarationContext)
        TestLogger.success("Signed typedef parsed")
        TestLogger.complete()

    def test_parse_unsigned_typedef(self) -> None:
        """Test parsing an unsigned typedef."""
        TestLogger.header("MetaParser: Unsigned Typedef")

        parser = Meta.MetaParser()
        result = parser.parseTypedefDeclaration("typedef unsigned int Unt4")

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.TypedefDeclarationContext)
        TestLogger.success("Unsigned typedef parsed")
        TestLogger.complete()


class TestParseEnumDeclaration:
    """Tests for parseEnumDeclaration method."""

    def test_parse_simple_enum(self) -> None:
        """Test parsing a simple enum."""
        TestLogger.header("MetaParser: Simple Enum")

        parser = Meta.MetaParser()
        result = parser.parseEnumDeclaration('''
            enum Color : Int4 {
                RED
                GREEN
                BLUE
            }
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.EnumDeclarationContext)
        TestLogger.success("Simple enum parsed")
        TestLogger.complete()

    def test_parse_enum_with_values(self) -> None:
        """Test parsing an enum with explicit values."""
        TestLogger.header("MetaParser: Enum with Values")

        parser = Meta.MetaParser()
        result = parser.parseEnumDeclaration('''
            enum Status : Unt4 {
                OK = 0
                ERROR = 1
                PENDING = 0x10
            }
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.EnumDeclarationContext)
        TestLogger.success("Enum with values parsed")
        TestLogger.complete()


class TestParseFlagDeclaration:
    """Tests for parseFlagDeclaration method."""

    def test_parse_simple_flag(self) -> None:
        """Test parsing a simple flag."""
        TestLogger.header("MetaParser: Simple Flag")

        parser = Meta.MetaParser()
        result = parser.parseFlagDeclaration('''
            flag Options : Unt4 {
                OPTION_A
                OPTION_B
                OPTION_C
            }
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.FlagDeclarationContext)
        TestLogger.success("Simple flag parsed")
        TestLogger.complete()

    def test_parse_flag_with_offsets(self) -> None:
        """Test parsing a flag with manual offsets."""
        TestLogger.header("MetaParser: Flag with Offsets")

        parser = Meta.MetaParser()
        result = parser.parseFlagDeclaration('''
            flag Permissions : Unt4 {
                READ
                WRITE
                EXECUTE = 0x10
                ADMIN
            }
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.FlagDeclarationContext)
        TestLogger.success("Flag with offsets parsed")
        TestLogger.complete()


class TestParseStructureDeclaration:
    """Tests for parseStructureDeclaration method."""

    def test_parse_simple_structure(self) -> None:
        """Test parsing a simple structure."""
        TestLogger.header("MetaParser: Simple Structure")

        parser = Meta.MetaParser()
        result = parser.parseStructureDeclaration('''
            structure Point {
                Int4 x
                Int4 y
            }
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.StructureDeclarationContext)
        TestLogger.success("Simple structure parsed")
        TestLogger.complete()

    def test_parse_structure_with_extension(self) -> None:
        """Test parsing a structure with base type."""
        TestLogger.header("MetaParser: Structure with Extension")

        parser = Meta.MetaParser()
        result = parser.parseStructureDeclaration('''
            structure Point3D : Point {
                Int4 z
            }
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.StructureDeclarationContext)
        TestLogger.success("Structure with extension parsed")
        TestLogger.complete()

    def test_parse_structure_with_pointer_member(self) -> None:
        """Test parsing a structure with pointer member."""
        TestLogger.header("MetaParser: Structure with Pointer")

        parser = Meta.MetaParser()
        result = parser.parseStructureDeclaration('''
            structure Node {
                Int4 value
                Node* next
            }
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.StructureDeclarationContext)
        TestLogger.success("Structure with pointer parsed")
        TestLogger.complete()

    def test_parse_structure_with_array_member(self) -> None:
        """Test parsing a structure with array member."""
        TestLogger.header("MetaParser: Structure with Array")

        parser = Meta.MetaParser()
        result = parser.parseStructureDeclaration('''
            structure Buffer {
                Unt4 size
                Unt1[256] data
            }
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.StructureDeclarationContext)
        TestLogger.success("Structure with array parsed")
        TestLogger.complete()


class TestParseInterfaceDeclaration:
    """Tests for parseInterfaceDeclaration method."""

    def test_parse_simple_interface(self) -> None:
        """Test parsing a simple interface."""
        TestLogger.header("MetaParser: Simple Interface")

        parser = Meta.MetaParser()
        result = parser.parseInterfaceDeclaration('''
            interface IExample {
                Void doSomething()
                Int4 getValue()
            }
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.InterfaceDeclarationContext)
        TestLogger.success("Simple interface parsed")
        TestLogger.complete()

    def test_parse_interface_with_extension(self) -> None:
        """Test parsing an interface with base type."""
        TestLogger.header("MetaParser: Interface with Extension")

        parser = Meta.MetaParser()
        result = parser.parseInterfaceDeclaration('''
            interface IExtended : IBase {
                Void extendedMethod()
            }
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.InterfaceDeclarationContext)
        TestLogger.success("Interface with extension parsed")
        TestLogger.complete()

    def test_parse_interface_with_parameters(self) -> None:
        """Test parsing an interface with method parameters."""
        TestLogger.header("MetaParser: Interface with Parameters")

        parser = Meta.MetaParser()
        result = parser.parseInterfaceDeclaration('''
            interface ICalculator {
                Int4 add(Int4 a, Int4 b)
                Int4 multiply(Int4 x, Int4 y)
            }
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.InterfaceDeclarationContext)
        TestLogger.success("Interface with parameters parsed")
        TestLogger.complete()


class TestParseFunctionDeclaration:
    """Tests for parseFunctionDeclaration method."""

    def test_parse_simple_function(self) -> None:
        """Test parsing a simple function."""
        TestLogger.header("MetaParser: Simple Function")

        parser = Meta.MetaParser()
        result = parser.parseFunctionDeclaration("Int4 getValue()")

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.FunctionDeclarationContext)
        TestLogger.success("Simple function parsed")
        TestLogger.complete()

    def test_parse_function_with_parameters(self) -> None:
        """Test parsing a function with parameters."""
        TestLogger.header("MetaParser: Function with Parameters")

        parser = Meta.MetaParser()
        result = parser.parseFunctionDeclaration("Int4 add(Int4 a, Int4 b)")

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.FunctionDeclarationContext)
        TestLogger.success("Function with parameters parsed")
        TestLogger.complete()

    def test_parse_function_with_decorator(self) -> None:
        """Test parsing a function with decorator."""
        TestLogger.header("MetaParser: Function with Decorator")

        parser = Meta.MetaParser()
        result = parser.parseFunctionDeclaration('''
            @WinApi
            Int4 CreateWindow(Unt4 style, Unt4 flags)
        ''')

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.FunctionDeclarationContext)
        TestLogger.success("Function with decorator parsed")
        TestLogger.complete()

    def test_parse_function_with_pointer_return(self) -> None:
        """Test parsing a function with pointer return type."""
        TestLogger.header("MetaParser: Function with Pointer Return")

        parser = Meta.MetaParser()
        result = parser.parseFunctionDeclaration("Void* allocate(Unt4 size)")

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.FunctionDeclarationContext)
        TestLogger.success("Function with pointer return parsed")
        TestLogger.complete()


class TestParseTypeSpec:
    """Tests for parseTypeSpec method."""

    def test_parse_simple_type(self) -> None:
        """Test parsing a simple type."""
        TestLogger.header("MetaParser: Simple Type")

        parser = Meta.MetaParser()
        result = parser.parseTypeSpec("Int4")

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.TypeSpecContext)
        TestLogger.success("Simple type parsed")
        TestLogger.complete()

    def test_parse_pointer_type(self) -> None:
        """Test parsing a pointer type."""
        TestLogger.header("MetaParser: Pointer Type")

        parser = Meta.MetaParser()
        result = parser.parseTypeSpec("Void*")

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.TypeSpecContext)
        TestLogger.success("Pointer type parsed")
        TestLogger.complete()

    def test_parse_double_pointer_type(self) -> None:
        """Test parsing a double pointer type."""
        TestLogger.header("MetaParser: Double Pointer Type")

        parser = Meta.MetaParser()
        result = parser.parseTypeSpec("Int4**")

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.TypeSpecContext)
        TestLogger.success("Double pointer type parsed")
        TestLogger.complete()

    def test_parse_array_type(self) -> None:
        """Test parsing an array type."""
        TestLogger.header("MetaParser: Array Type")

        parser = Meta.MetaParser()
        result = parser.parseTypeSpec("Unt1[8]")

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.TypeSpecContext)
        TestLogger.success("Array type parsed")
        TestLogger.complete()

    def test_parse_qualified_type(self) -> None:
        """Test parsing a qualified type."""
        TestLogger.header("MetaParser: Qualified Type")

        parser = Meta.MetaParser()
        result = parser.parseTypeSpec("std::lib::Int4")

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.TypeSpecContext)
        TestLogger.success("Qualified type parsed")
        TestLogger.complete()


class TestParseAliasDeclaration:
    """Tests for parseAliasDeclaration method."""

    def test_parse_simple_alias(self) -> None:
        """Test parsing a simple alias."""
        TestLogger.header("MetaParser: Simple Alias")

        parser = Meta.MetaParser()
        result = parser.parseAliasDeclaration("alias Guid InterfaceId")

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.AliasDeclarationContext)
        TestLogger.success("Simple alias parsed")
        TestLogger.complete()

    def test_parse_pointer_alias(self) -> None:
        """Test parsing an alias to a pointer type."""
        TestLogger.header("MetaParser: Pointer Alias")

        parser = Meta.MetaParser()
        result = parser.parseAliasDeclaration("alias IID* REFIID")

        assert result is not None
        assert isinstance(result, Antlr4.CtdParser.AliasDeclarationContext)
        TestLogger.success("Pointer alias parsed")
        TestLogger.complete()

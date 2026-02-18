"""Tests for CtdParser.moduleDeclaration method.

Validates that CtdParser correctly parses complete CTD module declarations
into ANTLR4 ModuleDeclarationContext parse trees.

A module declaration consists of:
- Zero or more import declarations
- Zero or more namespace declarations
- EOF marker
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


def test_parse_empty_module() -> None:
    """Test parsing an empty module (no imports, no namespaces)."""
    TestLogger.header("CtdParser.moduleDeclaration: Empty Module")

    parser: Antlr4.CtdParser
    ctx: Antlr4.CtdGrammar.ModuleDeclarationContext

    # Create parser and parse empty module
    parser = Antlr4.CtdParser()
    ctx = parser.moduleDeclaration("")

    # Verify context is valid
    assert ctx is not None
    assert isinstance(ctx, Antlr4.CtdGrammar.ModuleDeclarationContext)

    # Verify no imports
    import_decls = ctx.importDeclaration()
    assert import_decls is not None
    assert len(import_decls) == 0
    TestLogger.success("No import declarations found")

    # Verify no namespaces
    namespace_decls = ctx.namespaceDeclaration()
    assert namespace_decls is not None
    assert len(namespace_decls) == 0
    TestLogger.success("No namespace declarations found")

    # Verify EOF is present
    assert ctx.EOF() is not None
    TestLogger.success("EOF marker present")

    TestLogger.complete()


def test_parse_module_with_single_namespace() -> None:
    """Test parsing a module with a single namespace (no imports)."""
    TestLogger.header("CtdParser.moduleDeclaration: Single Namespace")

    parser: Antlr4.CtdParser
    ctx: Antlr4.CtdGrammar.ModuleDeclarationContext

    # Create parser and parse module with single namespace
    parser = Antlr4.CtdParser()
    ctx = parser.moduleDeclaration("""
        namespace example::types {
            typedef int Int4
            typedef void Void
        }
    """)

    # Verify context is valid
    assert ctx is not None
    assert isinstance(ctx, Antlr4.CtdGrammar.ModuleDeclarationContext)

    # Verify no imports
    import_decls = ctx.importDeclaration()
    assert len(import_decls) == 0
    TestLogger.success("No import declarations found")

    # Verify single namespace
    namespace_decls = ctx.namespaceDeclaration()
    assert len(namespace_decls) == 1
    TestLogger.success("One namespace declaration found")

    # Verify namespace properties
    ns = namespace_decls[0]
    assert ns.qualifiedName() is not None
    assert ns.qualifiedName().getText() == "example::types"
    TestLogger.success("Namespace name is 'example::types'")

    # Verify namespace has declarations
    ns_decl_list = ns.declaration()
    assert ns_decl_list is not None
    assert len(ns_decl_list) == 2
    TestLogger.success("Namespace contains 2 declarations")

    # Verify first declaration is typedef
    assert ns_decl_list[0].typedefDeclaration() is not None
    assert ns_decl_list[0].typedefDeclaration().IDENTIFIER().getText() == "Int4"
    TestLogger.success("First declaration is 'typedef int Int4'")

    # Verify second declaration is typedef
    assert ns_decl_list[1].typedefDeclaration() is not None
    assert ns_decl_list[1].typedefDeclaration().IDENTIFIER().getText() == "Void"
    TestLogger.success("Second declaration is 'typedef void Void'")

    # Verify EOF is present
    assert ctx.EOF() is not None
    TestLogger.success("EOF marker present")

    TestLogger.complete()


def test_parse_module_with_multiple_namespaces() -> None:
    """Test parsing a module with multiple namespaces (no imports)."""
    TestLogger.header("CtdParser.moduleDeclaration: Multiple Namespaces")

    parser: Antlr4.CtdParser
    ctx: Antlr4.CtdGrammar.ModuleDeclarationContext

    # Create parser and parse module with multiple namespaces
    parser = Antlr4.CtdParser()
    ctx = parser.moduleDeclaration("""
        namespace std::types {
            typedef int Int4
        }

        namespace std::collections {
            structure List {
                Int4 size
            }
        }

        namespace std::utils {
            Void print(Int4 value)
        }
    """)

    # Verify context is valid
    assert ctx is not None
    assert isinstance(ctx, Antlr4.CtdGrammar.ModuleDeclarationContext)

    # Verify no imports
    import_decls = ctx.importDeclaration()
    assert len(import_decls) == 0
    TestLogger.success("No import declarations found")

    # Verify three namespaces
    namespace_decls = ctx.namespaceDeclaration()
    assert len(namespace_decls) == 3
    TestLogger.success("Three namespace declarations found")

    # Verify first namespace
    ns1 = namespace_decls[0]
    assert ns1.qualifiedName().getText() == "std::types"
    assert len(ns1.declaration()) == 1
    assert ns1.declaration()[0].typedefDeclaration() is not None
    TestLogger.success("First namespace is 'std::types' with typedef")

    # Verify second namespace
    ns2 = namespace_decls[1]
    assert ns2.qualifiedName().getText() == "std::collections"
    assert len(ns2.declaration()) == 1
    assert ns2.declaration()[0].structureDeclaration() is not None
    assert ns2.declaration()[0].structureDeclaration().IDENTIFIER().getText() == "List"
    TestLogger.success("Second namespace is 'std::collections' with structure")

    # Verify third namespace
    ns3 = namespace_decls[2]
    assert ns3.qualifiedName().getText() == "std::utils"
    assert len(ns3.declaration()) == 1
    assert ns3.declaration()[0].functionDeclaration() is not None
    assert ns3.declaration()[0].functionDeclaration().IDENTIFIER().getText() == "print"
    TestLogger.success("Third namespace is 'std::utils' with function")

    # Verify EOF is present
    assert ctx.EOF() is not None
    TestLogger.success("EOF marker present")

    TestLogger.complete()


def test_parse_module_with_imports_and_namespaces() -> None:
    """Test parsing a module with import declarations and namespaces."""
    TestLogger.header("CtdParser.moduleDeclaration: Imports and Namespaces")

    parser: Antlr4.CtdParser
    ctx: Antlr4.CtdGrammar.ModuleDeclarationContext

    # Create parser and parse module with imports and namespaces
    parser = Antlr4.CtdParser()
    ctx = parser.moduleDeclaration("""
        import "std-types"
        import "utils"

        namespace app::core {
            typedef int AppInt
        }

        namespace app::ui {
            structure Window {
                AppInt width
                AppInt height
            }
        }
    """)

    # Verify context is valid
    assert ctx is not None
    assert isinstance(ctx, Antlr4.CtdGrammar.ModuleDeclarationContext)

    # Verify imports
    import_decls = ctx.importDeclaration()
    assert len(import_decls) == 2
    TestLogger.success("Two import declarations found")

    # Verify first import
    import1 = import_decls[0]
    assert import1.STRING_LITERAL() is not None
    assert import1.STRING_LITERAL().getText() == '"std-types"'
    TestLogger.success("First import is 'std-types'")

    # Verify second import
    import2 = import_decls[1]
    assert import2.STRING_LITERAL() is not None
    assert import2.STRING_LITERAL().getText() == '"utils"'
    TestLogger.success("Second import is 'utils'")

    # Verify namespaces
    namespace_decls = ctx.namespaceDeclaration()
    assert len(namespace_decls) == 2
    TestLogger.success("Two namespace declarations found")

    # Verify first namespace
    ns1 = namespace_decls[0]
    assert ns1.qualifiedName().getText() == "app::core"
    TestLogger.success("First namespace is 'app::core'")

    # Verify second namespace
    ns2 = namespace_decls[1]
    assert ns2.qualifiedName().getText() == "app::ui"
    TestLogger.success("Second namespace is 'app::ui'")

    # Verify EOF is present
    assert ctx.EOF() is not None
    TestLogger.success("EOF marker present")

    TestLogger.complete()


def test_parse_module_with_only_imports() -> None:
    """Test parsing a module with only import declarations (no namespaces)."""
    TestLogger.header("CtdParser.moduleDeclaration: Only Imports")

    parser: Antlr4.CtdParser
    ctx: Antlr4.CtdGrammar.ModuleDeclarationContext

    # Create parser and parse module with only imports
    parser = Antlr4.CtdParser()
    ctx = parser.moduleDeclaration("""
        import "base"
        import "core"
        import "extended"
    """)

    # Verify context is valid
    assert ctx is not None
    assert isinstance(ctx, Antlr4.CtdGrammar.ModuleDeclarationContext)

    # Verify imports
    import_decls = ctx.importDeclaration()
    assert len(import_decls) == 3
    TestLogger.success("Three import declarations found")

    # Verify import file names
    assert import_decls[0].STRING_LITERAL().getText() == '"base"'
    assert import_decls[1].STRING_LITERAL().getText() == '"core"'
    assert import_decls[2].STRING_LITERAL().getText() == '"extended"'
    TestLogger.success("All import file names validated")

    # Verify no namespaces
    namespace_decls = ctx.namespaceDeclaration()
    assert len(namespace_decls) == 0
    TestLogger.success("No namespace declarations found")

    # Verify EOF is present
    assert ctx.EOF() is not None
    TestLogger.success("EOF marker present")

    TestLogger.complete()


def test_parse_module_with_namespace_containing_use_declarations() -> None:
    """Test parsing a module with namespace containing use declarations."""
    TestLogger.header("CtdParser.moduleDeclaration: Namespace with Use Declarations")

    parser: Antlr4.CtdParser
    ctx: Antlr4.CtdGrammar.ModuleDeclarationContext

    # Create parser and parse module with use declarations in namespace
    parser = Antlr4.CtdParser()
    ctx = parser.moduleDeclaration("""
        import "std-types"

        namespace app {
            use std::types
            use std::collections

            typedef Int4 AppInt
        }
    """)

    # Verify context is valid
    assert ctx is not None
    assert isinstance(ctx, Antlr4.CtdGrammar.ModuleDeclarationContext)

    # Verify imports
    import_decls = ctx.importDeclaration()
    assert len(import_decls) == 1
    TestLogger.success("One import declaration found")

    # Verify namespace
    namespace_decls = ctx.namespaceDeclaration()
    assert len(namespace_decls) == 1
    ns = namespace_decls[0]
    assert ns.qualifiedName().getText() == "app"
    TestLogger.success("One namespace 'app' found")

    # Verify use declarations within namespace
    use_decls = ns.useDeclaration()
    assert use_decls is not None
    assert len(use_decls) == 2
    TestLogger.success("Two use declarations found in namespace")

    # Verify first use declaration
    use1 = use_decls[0]
    assert use1.qualifiedName().getText() == "std::types"
    TestLogger.success("First use declaration is 'std::types'")

    # Verify second use declaration
    use2 = use_decls[1]
    assert use2.qualifiedName().getText() == "std::collections"
    TestLogger.success("Second use declaration is 'std::collections'")

    # Verify namespace has declarations
    ns_decls = ns.declaration()
    assert len(ns_decls) == 1
    assert ns_decls[0].typedefDeclaration() is not None
    TestLogger.success("Namespace contains one typedef declaration")

    # Verify EOF is present
    assert ctx.EOF() is not None
    TestLogger.success("EOF marker present")

    TestLogger.complete()

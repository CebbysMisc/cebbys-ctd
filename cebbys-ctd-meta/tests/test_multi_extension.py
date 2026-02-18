"""Test to demonstrate multi-extension type capability."""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta.parser as Parser


def test_complex_multi_extensions():
    """Test that complex multi-extension types parse correctly."""
    test_cases = {
        "int[3]": "int [3]",
        "int*": "int *",
        "int**": "int * *",
        "int[3]*": "int [3] *",
        "int*[4]": "int * [4]",
        "int[3]**": "int [3] * *",
        "int[3]**[4]": "int [3] * * [4]",
        "int[3]**[4]*": "int [3] * * [4] *",
        "int[3]**[4]*[12]": "int [3] * * [4] * [12]",
    }
    
    for input_type, expected_output in test_cases.items():
        ctd_parser = Antlr4.CtdParser()
        typespec_ctx = ctd_parser.typeSpec(input_type)
        
        assert typespec_ctx is not None, f"Failed to parse: {input_type}"
        
        typespec_str = Parser.CtdMetaParser.parse_typespec(typespec_ctx)
        
        assert typespec_str == expected_output, \
            f"Input: {input_type}\n  Expected: {expected_output}\n  Got: {typespec_str}"
        
        print(f"✓ {input_type:20} → {typespec_str}")
    
    print("\n✅ All complex multi-extension tests passed!")


if __name__ == "__main__":
    test_complex_multi_extensions()

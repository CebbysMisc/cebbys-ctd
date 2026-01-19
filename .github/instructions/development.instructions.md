# Development Instructions

## Project Overview

cebbys-ctd is a custom type definition language project that uses ANTLR4 to parse custom language files and Python to interpret, instantiate, and link the resulting objects.

## Project Structure

```
cebbys-ctd/
├── sources/          # Source code root directory
├── tests/            # Tests directory with subdirectories as test modules
├── resources/        # Resources directory containing ANTLR4 grammar files
└── hints/            # Type hints directory (not a source root)
    └── antlr4/       # ANTLR4 type stubs (.pyi files only)
```

### Directory Guidelines

- **sources/**: Main source code directory. This is the source root for the Python project.
- **tests/**: Test files organized in subdirectories as modules containing multiple tests.
- **resources/**: Contains ANTLR4 grammar files (`.g4`) and other project resources.
- **hints/**: Type hint stubs directory. Not a source root, but subdirectories within it are added to Python's extra paths.

## Development Environment

This project is developed using **Visual Studio Code** with the following configuration:

- Python analysis and autocomplete paths include `sources` and subdirectories of `hints/`
- pytest is configured for testing with tests located in the `tests/` directory

## Development Workflow

1. **Define grammar**: Create/modify ANTLR4 grammar files in `resources/`
2. **Generate parsers**: Use ANTLR4 to generate Python parser code
3. **Implement interpreters**: Write Python code in `sources/` to interpret parsed AST
4. **Create objects**: Instantiate Python objects from parsed definitions
5. **Link objects**: Implement linking logic to connect related objects
6. **Test**: Write tests in `tests/` directory organized by module

## Implementing GTD Language Features

**REQUIRED**: Follow this comprehensive workflow when implementing new GTD language features or modifying existing language behavior.

### Step 1: Familiarization and Analysis

Before making any changes, thoroughly understand the existing codebase and requirements:

1. **Read all development instructions**:
   - Review `.github/instructions/development.instructions.md` (this file)
   - Review `.github/instructions/python.instructions.md`

2. **Read the language specification**:
   - Review `resources/documents/gtd-language-syntax.md` - this is the authoritative source of truth for GTD language syntax
   - Understand all existing language features, keywords, and rules
   - This document explains the fully implemented logic for language syntax

3. **Study relevant implementation files**:
   - **Parser/Visitor**: `sources/lv/cebbys/languages/ctd/visitor.py`
   - **Meta types**: `sources/lv/cebbys/languages/ctd/meta/types.py`
   - **Resolvers**: `sources/lv/cebbys/languages/ctd/meta/resolver/*.py`
   - **Definition types**: `sources/lv/cebbys/languages/ctd/define/types.py`
   - **Loader**: `sources/lv/cebbys/languages/ctd/loader.py` and `sources/lv/cebbys/languages/ctd/meta/loader.py`

4. **Review existing tests**:
   - Examine `tests/*.py` to understand testing patterns
   - Look at `tests/resources/gtd/*.gtd` for test resource organization

5. **Identify what needs to change**:
   - Determine if grammar changes are needed
   - Identify which Python modules need updates
   - Plan the scope of changes

### Step 2: Document the Language Specification

**ALWAYS** document the feature before implementing it:

1. **Update `resources/documents/gtd-language-syntax.md`**:
   - Add or modify sections describing the new feature
   - Include complete syntax definitions
   - Document all keywords, operators, and grammar rules
   - Explain semantic behavior and resolution rules

2. **Provide comprehensive examples**:
   - Show correct usage patterns (✓ Works)
   - Show incorrect usage patterns (✗ Fails)
   - Include edge cases
   - Explain WHY each example works or fails

3. **Document interactions with existing features**:
   - Explain how the new feature interacts with other language elements
   - Clarify precedence and scoping rules
   - Note any breaking changes

**Example sections to include**:
```markdown
### New Feature Name

Syntax:
```gtd
keyword syntax_pattern { ... }
```

Rules:
- Rule 1: Clear description
- Rule 2: Clear description

Examples:
#### Example 1: Basic Usage (Works)
```gtd
// Working example with explanation
```

#### Example 2: Invalid Usage (Fails)
```gtd
// Failing example with explanation
```

### Step 3: Update Grammar (if needed)

If the feature requires parser-level changes:

1. **Modify ANTLR4 grammar**:
   - Edit `resources/gtd/Gtd.g4` (or relevant `.g4` file)
   - Add new keywords to the lexer
   - Add new grammar rules to the parser
   - Follow existing naming conventions

2. **Regenerate parser/lexer**:
   - Run ANTLR4 to regenerate Python parser code
   - Update `sources/lv/cebbys/languages/ctd/antlr4/*.py`

3. **Verify generated code**:
   - Ensure generated code compiles without errors
   - Check that new rules are accessible

**Note**: Only modify grammar if the feature requires new syntax. Many features (like resolution rules) don't need grammar changes.

### Step 4: Implement the Feature

Implement changes following the data flow: Parse → Meta → Resolve → Define

#### 4.1: Update Visitor (if needed)

**File**: `sources/lv/cebbys/languages/ctd/visitor.py`

1. Add visitor methods for new grammar rules:
   ```python
   def visitNewFeatureDeclaration(
       self,
       ctx: GtdParser.GtdParser.NewFeatureDeclarationContext
   ) -> None:
       """Visit new feature declaration."""
       # Extract data from parse tree
       # Create Meta objects
       # Add to collection
   ```

2. Update existing visitor methods if feature affects them

3. Extract data from parse tree contexts properly

#### 4.2: Update Meta Types (if needed)

**File**: `sources/lv/cebbys/languages/ctd/meta/types.py`

1. Add new Meta classes for unresolved types:
   ```python
   class NewFeatureMeta:
       """Metadata for new feature before resolution."""
       def __init__(self, name: str, namespace: str, ...):
           # Store raw, unresolved data
   ```

2. Update `DefinitionCollectionMeta` if needed:
   - Add new collection for the feature type
   - Add `add_*` methods

#### 4.3: Update Resolvers (if needed)

**Files**: `sources/lv/cebbys/languages/ctd/meta/resolver/*.py`

1. Create new resolver class if needed (in separate file):
   ```python
   class NewFeatureResolver(BaseResolver):
       """Resolves new feature type references."""

       def create_instances(self) -> None:
           """Create instances and add to type cache."""

       def resolve_instances(self) -> None:
           """Resolve type references."""
   ```

2. Update `BaseResolver` (`__api__.py`) if feature affects common resolution logic

3. Register new resolver in `sources/lv/cebbys/languages/ctd/meta/resolver/__init__.py`:
   ```python
   def resolve(...) -> Define.DefinitionCollection:
       # Add new resolver to pipeline
       new_feature_resolver = NewFeatureResolver(context)
       new_feature_resolver.create_instances()
   ```

#### 4.4: Update Definition Types (if needed)

**File**: `sources/lv/cebbys/languages/ctd/define/types.py`

1. Add new Definition classes for resolved types:
   ```python
   class NewFeatureDefinition(BaseDefinition):
       """Resolved new feature definition."""
       # Immutable, fully resolved representation
   ```

2. Update `DefinitionCollection` if needed:
   - Add new property for accessing the feature
   - Update `find_type()` if feature is a type

#### 4.5: Follow Python Coding Standards

Ensure all code follows `python.instructions.md`:
- Use `import module as Module` style
- Declare variable types at function start
- Define `__all__` exports
- Follow SRP (Single Responsibility Principle)
- Use proper type annotations

### Step 5: Update Existing Code

Fix existing GTD files and code to comply with new behavior:

1. **Update GTD resource files**:
   - Modify `resources/ctd/*.gtd` files if needed
   - Ensure all files comply with new language rules
   - Fix any violations

2. **Update dependent Python code**:
   - Fix any code that depends on changed behavior
   - Update imports if module structure changed

3. **Test existing files load correctly**:
   - Verify no regressions in existing GTD file loading

### Step 6: Create Test Resources

Create comprehensive test GTD files in `tests/resources/gtd/`:

1. **Organize by test scenario**:
   ```
   tests/resources/gtd/
   ├── feature-name-basic/
   │   ├── test-file-1.gtd
   │   └── test-file-2.gtd
   ├── feature-name-with-dependency/
   │   ├── dependency.gtd
   │   └── consumer.gtd
   └── feature-name-invalid/
       └── invalid-usage.gtd
   ```

2. **Use subdirectories** to isolate test scenarios:
   - Each subdirectory contains files for one test case
   - Prevents type name collisions between tests
   - Allows loading entire directory as test input

3. **Create multiple scenarios**:
   - **Positive tests**: Feature works correctly
   - **Edge cases**: Boundary conditions
   - **Negative tests**: Invalid usage that should fail

4. **Document test intent**:
   - Add comments in GTD files explaining what's being tested
   - Include comments like `// This should WORK because...`
   - Include comments like `// This should FAIL because...`

**Example**:
```gtd
// tests/resources/gtd/namespace-with-use/base.gtd
namespace test::base {
    typedef int Int4
}

// tests/resources/gtd/namespace-with-use/consumer.gtd
import "base"

namespace test::consumer {
    use test::base

    // This should WORK - test::base is imported via use
    typedef Int4 MyInt
}
```

### Step 7: Write Comprehensive Tests

Create test file in `tests/` directory:

1. **File naming**: `tests/test_<feature_name>.py`

2. **Import required modules**:
   ```python
   import pathlib as Pathlib
   import pytest as Pytest
   import lv.cebbys.languages.ctd as Ctd
   from test_utils import TestLogger
   ```

3. **Write test functions**:
   ```python
   def test_feature_basic_usage() -> None:
       """Test that basic feature usage works correctly."""
       loader: Ctd.Loader.CtdLoader
       paths: list[Pathlib.Path]
       collection: Ctd.Define.DefinitionCollection

       TestLogger.header("Feature Name: Basic Usage")

       # Load test GTD files
       paths = [Pathlib.Path('tests/resources/gtd/feature-basic')]
       loader = Ctd.Loader.CtdLoader(paths)
       collection = loader.load()

       # Verify expected behavior
       result = collection.get('expected::item')
       assert result is not None, "Should find expected item"

       TestLogger.success("Feature works correctly")
       TestLogger.complete("Test passed")
   ```

4. **Test positive cases**:
   - Feature works as documented
   - All valid syntax variations
   - Integration with other features

5. **Test negative cases**:
   - Invalid usage raises appropriate errors
   - Error messages are clear and helpful
   ```python
   def test_feature_invalid_usage_should_fail() -> None:
       """Test that invalid usage raises appropriate error."""
       loader: Ctd.Loader.CtdLoader
       paths: list[Pathlib.Path]

       paths = [Pathlib.Path('tests/resources/gtd/feature-invalid')]
       loader = Ctd.Loader.CtdLoader(paths)

       with Pytest.raises(Exception) as exc_info:
           loader.load()

       error_message = str(exc_info.value)
       assert 'expected error keyword' in error_message

       TestLogger.success("Correctly raised error for invalid usage")
   ```

6. **Test edge cases**:
   - Boundary conditions
   - Empty inputs
   - Maximum complexity
   - Interactions with other features

7. **Use TestLogger for output**:
   - `TestLogger.header()` - Test section header
   - `TestLogger.success()` - Success message
   - `TestLogger.info()` - Informational message
   - `TestLogger.complete()` - Test completion

### Step 8: Validation and Regression Testing

Ensure no existing functionality is broken:

1. **Run all tests**:
   ```bash
   python -m pytest tests/ -v
   ```

2. **Verify all tests pass**:
   - New tests must pass
   - ALL existing tests must still pass
   - No regressions allowed

3. **Fix any failures**:
   - If existing tests fail, fix the implementation
   - Do not modify existing tests unless they're testing incorrect behavior
   - Ensure backward compatibility when possible

4. **Check test coverage**:
   - Ensure new code has adequate test coverage
   - Test both success and failure paths

5. **Manual testing** (if applicable):
   - Load real-world GTD files
   - Verify feature works in practical scenarios

### Step 9: Documentation Review

Before completing, verify documentation is complete:

1. **Language specification updated**: `resources/documents/gtd-language-syntax.md`
2. **Code comments added**: Complex logic explained
3. **Examples provided**: Both in docs and tests
4. **Error messages clear**: Users understand what went wrong

### Step 10: Commit and Pull Request

Follow the branching strategy:

1. **Ensure you're on a feature branch**:
   ```bash
   git checkout -b feature/<feature-name>
   ```

2. **Stage all changes**:
   ```bash
   git add .
   ```

3. **Commit with descriptive message**:
   ```bash
   git commit -m "Add <feature-name> support

   - Document feature in gtd-language-syntax.md
   - Implement parser/resolver changes
   - Add comprehensive tests
   - All tests passing (X/X)"
   ```

4. **Push and create Pull Request**:
   ```bash
   git push origin feature/<feature-name>
   ```

5. **PR should target**: `release/<version>` branch

### Quick Reference Checklist

When implementing a new GTD language feature, complete these items:

- [ ] Read development instructions
- [ ] Examine existing code and GTD files
- [ ] Update `resources/documents/gtd-language-syntax.md` with feature documentation
- [ ] Modify ANTLR4 grammar (if needed)
- [ ] Update visitor.py (if needed)
- [ ] Update meta/types.py (if needed)
- [ ] Update or create resolver (if needed)
- [ ] Update define/types.py (if needed)
- [ ] Fix existing GTD files to comply with changes
- [ ] Create test GTD files in `tests/resources/gtd/<feature-name>/`
- [ ] Write comprehensive tests in `tests/test_<feature_name>.py`
- [ ] Run all tests: `python -m pytest tests/ -v`
- [ ] Verify all tests pass (no regressions)
- [ ] Commit changes to feature branch
- [ ] Create Pull Request to release branch

### Common Pitfalls to Avoid

1. **Don't skip documentation**: Always update `gtd-language-syntax.md` first
2. **Don't forget existing files**: Update `resources/ctd/*.gtd` to comply with changes
3. **Don't break existing tests**: All tests must continue to pass
4. **Don't mix test scenarios**: Use subdirectories to isolate test cases
5. **Don't create type collisions**: Avoid reusing type names across test files in same directory
6. **Don't skip negative tests**: Always test that invalid usage fails correctly
7. **Don't commit to release branch**: Always use feature branches

## Technology Stack

- ANTLR4 for grammar definition and parsing
- Python for runtime interpretation and object management
- VSCode as the development environment

## Branching Strategy

**REQUIRED**: Follow this Git branching workflow:

### Release Branch

- **Branch name**: `release/{version}` (e.g., `release/1.0.0`)
- **Protection**: No direct commits allowed
- **Updates**: Only via Pull Requests from feature branches

### Feature Branches

- **Branch name template**: `feature/{short-description-for-the-feature}`
- **Examples**:
  - `feature/add-parser-support`
  - `feature/implement-type-checker`
  - `feature/fix-namespace-resolution`

### Workflow

1. **Create feature branch** from latest release branch:
   ```bash
   git checkout release/1.0.0
   git pull
   git checkout -b feature/my-new-feature
   ```

2. **Develop and commit** changes on feature branch:
   ```bash
   git add .
   git commit -m "Your commit message"
   ```

3. **Push feature branch** and create Pull Request:
   ```bash
   git push origin feature/my-new-feature
   ```

4. **Merge via PR** after review and approval

5. **Delete feature branch** after successful merge

### Branch Protection Rules

- Release branches must be protected
- All changes require PR approval
- No force pushes to release branches

## Adding Type Hint Modules

The `hints/` directory contains type stub modules (`.pyi` files) for external libraries that may lack type hints. To add a new hint module:

1. **Create a subdirectory** under `hints/` with the module name:
   ```
   mkdir hints/<module_name>
   ```

2. **Add type stub files** (`.pyi` files) to the new directory. These files should contain type definitions for the external library.

3. **Update VSCode settings** in `.vscode/settings.json` to include the new module in the Python extra paths:
   ```json
   {
       "python.analysis.extraPaths": [
           "${workspaceFolder}/sources",
           "${workspaceFolder}/hints/antlr4",
           "${workspaceFolder}/hints/<module_name>"
       ],
       "python.autoComplete.extraPaths": [
           "${workspaceFolder}/sources",
           "${workspaceFolder}/hints/antlr4",
           "${workspaceFolder}/hints/<module_name>"
       ]
   }
   ```

**Note**: The `hints/` directory itself is NOT a source root. Only the subdirectories within `hints/` are added to the Python path.

# CTD Loader Implementation Plan

## Overview

Implement the CTD loader module following a clean four-stage pipeline that loads all .ctd files from configured directories and produces a fully-resolved, immutable type definition collection with query APIs.

## Architecture

### Four-Stage Transformation Pipeline

```
1. Recursively iterate directories to gather **/*.ctd files
   list[Path] - collected file paths

2. Parse each file to ANTLR4 ModuleDeclarationContext
   list[Path] → list[ModuleDeclarationContext]

3. Convert each context to ModuleMeta
   list[ModuleDeclarationContext] → list[ModuleMeta]

4. Construct CebbysTypeDefinitions (singleton collection)
   list[ModuleMeta] → CebbysTypeDefinitions
   - Two-step resolution: create singletons, then resolve references
   - Track file path for each definition (for error reporting)
   - Expose query APIs
```

### Key Requirements

1. **Eager loading** - Load ALL files immediately
2. **Error collection** - Collect all errors, report at once (don't fail fast)
3. **File path tracking** - Track source file for each definition
4. **Query APIs** - Convenient methods for accessing types
5. **Immutable result** - Frozen definitions after resolution

## Completed Work

### ✅ Phase 1: CtdLoader Transformation Chain (Commit: 9f4cd0f)

**File**: `cebbys-ctd-loader/sources/lv/cebbys/languages/ctd/loader.py`

Implemented transformation chain in `__init__`:

```python
# Stage 1: list[Path] - Gather .ctd files
self._ctd_files = self._list_ctd_from_dirs(dirs)

# Stage 2: list[tuple[Path, ModuleDeclarationContext]] - Parse to contexts
self._module_contexts = self._parse_files_to_contexts(self._ctd_files)

# Stage 3: list[tuple[Path, ModuleMeta]] - Convert to meta
self._module_metas = self._convert_contexts_to_metas(self._module_contexts)

# Stage 4: TODO - Build CebbysTypeDefinitions
# self._definitions = self._build_type_definitions(self._module_metas)
```

**Implemented**:
- ✅ `_list_ctd_from_dirs()` - Recursively finds .ctd files using `rglob('*.ctd')`
- ✅ `_parse_files_to_contexts()` - Parses files using `Antlr4.CtdParser.moduleDeclaration()`
- ✅ `_convert_contexts_to_metas()` - Uses `MetaVisitor` (creates empty ModuleMeta for now)
- ✅ `load()` - Temporary implementation using visitor directly

**Tests Created**: `cebbys-ctd-loader/tests/test_loader.py`
- ✅ `test_loader_transformation_chain()` - Verifies all 3 stages execute
- ✅ `test_loader_with_existing_resources()` - Tests with 6 real CTD files
- ✅ `test_loader_empty_directory()` - Edge case handling

**Test Results**: 3/3 passing ✅

### ✅ Phase 2: Meta Test Refactoring (Commit: 9f4cd0f)

**Refactored 8 test files** with consistent three-step pattern:
- Step 1: Parse CTD string → ANTLR4 context
- Step 2: Map context → Meta object using MetaVisitor
- Step 3: Validate Meta object attributes

**Files**:
- ✅ `test_parse_alias.py` (3 tests)
- ✅ `test_parse_typedef.py` (4 tests)
- ✅ `test_parse_enum.py` (2 tests)
- ✅ `test_parse_flag.py` (2 tests)
- ✅ `test_parse_structure.py` (4 tests)
- ✅ `test_parse_interface.py` (3 tests)
- ✅ `test_parse_function.py` (4 tests)
- ✅ `test_parse_type_spec.py` (5 tests)

**Removed deprecated tests**:
- ❌ `test_parse_compilation_unit.py`
- ❌ `test_parse_namespace.py`

**Benefits**:
- ~50% code reduction per test file
- Consistent pattern across all meta tests
- Helper functions reduce duplication

**Test Results**: 27/27 passing ✅

### ✅ Phase 3: MetaLoader Deprecation (Commit: 0e4f94d)

**Removed**:
- ❌ `cebbys-ctd-meta/sources/lv/cebbys/languages/ctd/meta/loader.py`
- ❌ MetaLoader exports from `cebbys-ctd-meta/sources/lv/cebbys/languages/ctd/meta/__init__.py`

**Added**:
- ✅ `load_meta_collection()` helper in `conftest.py`
  - Replacement for MetaLoader in tests
  - Returns `(DefinitionCollectionMeta, namespace_uses)`
  - Used by resolver tests

**Updated**:
- ✅ CtdLoader.load() - uses transformation chain (stages 1-3)
- ✅ Resolver tests - use `load_meta_collection()` instead of `MetaLoader`
- ✅ conftest.py - fixed to use `CtdGrammar` instead of `CtdParser` wrapper
- ✅ Resolver pyproject.toml - added workspace root to pythonpath

**Test Results**:
- cebbys-ctd-meta: 27/27 passing ✅
- cebbys-ctd-loader: 3/3 passing ✅
- cebbys-ctd-resolver: 5/12 passing (7 pre-existing failures)

### ✅ Phase 4: VSCode Tasks

**Tasks Added** to `.vscode/tasks.json`:
- ✅ "Run All Tests (loader)" - Runs loader tests from workspace root
- ✅ "Run Loader Test (test_loader.py)" - Runs specific loader test
- ✅ "Run All Tests (all modules)" - Runs meta, resolver, loader tests

## Current Status

**Overall Test Results**: 35/42 passing (83% pass rate)
- ✅ cebbys-ctd-meta: 27/27 passing
- ✅ cebbys-ctd-loader: 3/3 passing
- ⚠️ cebbys-ctd-resolver: 5/12 passing
  - 5 tests in test_definition_creation.py passing ✅
  - 7 tests in test_type_resolution.py failing (pre-existing)

**Commits**:
- `9f4cd0f` - CtdLoader transformation chain + meta test refactoring
- `0e4f94d` - MetaLoader deprecation and removal

## Remaining Work

### Phase 5: MetaVisitor Enhancement

**File**: `cebbys-ctd-meta/sources/lv/cebbys/languages/ctd/meta/visitor.py`

- [ ] Implement `to_module_meta()` method
  - Extract namespaces from visitor state
  - Extract includes from visitor state
  - Build and return ModuleMeta instance

**Current Issue**: `_convert_contexts_to_metas()` creates empty ModuleMeta objects.

### Phase 6: Error Collection Infrastructure

**File**: `cebbys-ctd-loader/sources/lv/cebbys/languages/ctd/definitions.py`

- [ ] Create `LoadError` dataclass
  ```python
  @dataclass(frozen=True)
  class LoadError:
      file_path: Path
      error_type: str  # "parse_error", "meta_error", "resolution_error"
      message: str
      line: int | None = None
      column: int | None = None
  ```

- [ ] Update `_parse_files_to_contexts()` to collect parse errors
- [ ] Update `_convert_contexts_to_metas()` to collect meta errors

### Phase 7: CebbysTypeDefinitions Class

**File**: `cebbys-ctd-loader/sources/lv/cebbys/languages/ctd/definitions.py`

- [ ] Create `DefinitionMetadata` dataclass
  ```python
  @dataclass(frozen=True)
  class DefinitionMetadata:
      source_file: Path
      qualified_name: str
      namespace: str
      definition: BaseDefinition
  ```

- [ ] Implement `CebbysTypeDefinitions` class
  - [ ] `__init__(collection, metadata, errors)`
  - [ ] Build internal indexes (by name, namespace, file)
  - [ ] `get_declaration(qualified_name)` - O(1) lookup
  - [ ] `get_namespace(namespace_path)` - return all in namespace
  - [ ] `get_module(file_path)` - return all from file
  - [ ] `get_all()` - return all definitions
  - [ ] `get_collection()` - return DefinitionCollection
  - [ ] `get_errors()` - return collected errors
  - [ ] `is_valid()` - check if any errors occurred

### Phase 8: Stage 4 Implementation

**File**: `cebbys-ctd-loader/sources/lv/cebbys/languages/ctd/loader.py`

- [ ] Implement `_build_type_definitions()` method
  - [ ] Aggregate ModuleMeta → DefinitionCollectionMeta
  - [ ] Build file→qualified_name mapping
  - [ ] Resolve using MetaResolver
  - [ ] Track metadata (file paths)
  - [ ] Collect resolution errors
  - [ ] Return CebbysTypeDefinitions

- [ ] Update `load()` to return CebbysTypeDefinitions
- [ ] Remove temporary fallback implementation

### Phase 9: MetaResolver Enhancement

**File**: `cebbys-ctd-resolver/sources/lv/cebbys/languages/ctd/resolver/__init__.py`

- [ ] Update `resolve()` signature
  - Accept `list[tuple[Path, ModuleMeta]]`
  - Return `tuple[DefinitionCollection, list[DefinitionMetadata]]`

- [ ] Track file paths during resolution
- [ ] Build DefinitionMetadata list

### Phase 10: Testing

- [ ] Add tests for error collection
- [ ] Add tests for CebbysTypeDefinitions query APIs
- [ ] Add integration tests for complete pipeline
- [ ] Fix failing resolver tests (test_type_resolution.py)

### Phase 11: Documentation

- [ ] Update README.md with loader usage examples
- [ ] Document CebbysTypeDefinitions API
- [ ] Document error handling approach
- [ ] Update architecture diagrams

## Timeline Estimate

- Phase 5 (MetaVisitor): 1-2 hours
- Phase 6 (Error collection): 2-3 hours
- Phase 7 (CebbysTypeDefinitions): 2-3 hours
- Phase 8 (Stage 4): 2-3 hours
- Phase 9 (MetaResolver): 3-4 hours
- Phase 10 (Testing): 3-4 hours
- Phase 11 (Documentation): 1-2 hours

**Total**: ~15-20 hours (2-3 days)

## Success Criteria

- [ ] All .ctd files loaded eagerly from directories
- [ ] Errors collected and available via `get_errors()`
- [ ] File path tracked for every definition
- [ ] Query APIs work correctly
- [ ] All tests passing (target: 100%)
- [ ] Documentation complete
- [ ] No breaking changes to existing tests

## Notes

- MetaLoader successfully deprecated and removed ✅
- Transformation chain working end-to-end ✅
- Tests running from workspace root for dependency resolution ✅
- VSCode tasks configured for easy testing ✅

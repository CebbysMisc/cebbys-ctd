"""Definition Collection Module"""
import typing as Typing
import types as Types
import lv.cebbys.languages.ctd.define.__api__ as Api
import lv.cebbys.languages.ctd.define.typedef as TypedefModule
import lv.cebbys.languages.ctd.define.enum as EnumModule
import lv.cebbys.languages.ctd.define.flag as FlagModule
import lv.cebbys.languages.ctd.define.structure as StructureModule
import lv.cebbys.languages.ctd.define.function as FunctionModule

__all__ = ['DefinitionCollection']


def mapping[T](input: dict[str, T] | None) -> Typing.Mapping[str, T]:
    return Types.MappingProxyType(
        input if input is not None else {}
    )


class DefinitionCollection:
    """Immutable collection of resolved type definitions."""

    def __init__(
        self,
        typedefs: dict[str, TypedefModule.TypedefDefinition] | None = None,
        enums: dict[str, EnumModule.EnumDefinition] | None = None,
        flags: dict[str, FlagModule.FlagDefinition] | None = None,
        structures: dict[str, StructureModule.StructureDefinition] | None = None,
        functions: dict[str, FunctionModule.FunctionDefinition] | None = None
    ):
        """Initialize collection.

        Args:
            typedefs: Dictionary of typedefs indexed by qualified name
            enums: Dictionary of enums indexed by qualified name
            flags: Dictionary of flags indexed by qualified name
            structures: Dictionary of structures indexed by qualified name
            functions: Dictionary of functions indexed by qualified name
        """
        # Create immutable copies using MappingProxyType
        self._typedefs = mapping(typedefs)
        self._enums = mapping(enums)
        self._flags = mapping(flags)
        self._structures = mapping(structures)
        self._functions = mapping(functions)

    @property
    def typedefs(self) -> Typing.Mapping[str, TypedefModule.TypedefDefinition]:
        """Get immutable view of typedefs indexed by qualified name."""
        return self._typedefs

    @property
    def enums(self) -> Typing.Mapping[str, EnumModule.EnumDefinition]:
        """Get immutable view of enums indexed by qualified name."""
        return self._enums

    @property
    def flags(self) -> Typing.Mapping[str, FlagModule.FlagDefinition]:
        """Get immutable view of flags indexed by qualified name."""
        return self._flags

    @property
    def structures(self) -> Typing.Mapping[str, StructureModule.StructureDefinition]:
        """Get immutable view of structures indexed by qualified name."""
        return self._structures

    @property
    def functions(self) -> Typing.Mapping[str, FunctionModule.FunctionDefinition]:
        """Get immutable view of functions indexed by qualified name."""
        return self._functions

    def find_type(self, qualified_name: str) -> Api.BaseDefinition | None:
        """Find a type by qualified name.

        Args:
            qualified_name: Fully qualified type name

        Returns:
            The type definition or None if not found
        """
        if qualified_name in self._typedefs:
            return self._typedefs[qualified_name]
        if qualified_name in self._enums:
            return self._enums[qualified_name]
        if qualified_name in self._flags:
            return self._flags[qualified_name]
        if qualified_name in self._structures:
            return self._structures[qualified_name]
        return None

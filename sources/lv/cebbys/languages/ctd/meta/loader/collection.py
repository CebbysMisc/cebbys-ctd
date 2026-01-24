"""Definition Collection Meta Module"""
import lv.cebbys.languages.ctd.meta.loader.typedef as TypedefModule
import lv.cebbys.languages.ctd.meta.loader.alias as AliasModule
import lv.cebbys.languages.ctd.meta.loader.enum as EnumModule
import lv.cebbys.languages.ctd.meta.loader.flag as FlagModule
import lv.cebbys.languages.ctd.meta.loader.structure as StructureModule
import lv.cebbys.languages.ctd.meta.loader.interface as InterfaceModule
import lv.cebbys.languages.ctd.meta.loader.function as FunctionModule

__all__ = ['DefinitionCollectionMeta']


class DefinitionCollectionMeta:
    """Collection of parsed type definitions from CTD modules."""

    def __init__(self):
        """Initialize an empty definition collection."""
        self._typedefs: list[TypedefModule.TypedefMeta]
        self._aliases: list[AliasModule.AliasMeta]
        self._enums: list[EnumModule.EnumMeta]
        self._flags: list[FlagModule.FlagMeta]
        self._structures: list[StructureModule.StructureMeta]
        self._interfaces: list[InterfaceModule.InterfaceMeta]
        self._functions: list[FunctionModule.FunctionMeta]

        self._typedefs = []
        self._aliases = []
        self._enums = []
        self._flags = []
        self._structures = []
        self._interfaces = []
        self._functions = []

    @property
    def typedefs(self) -> list[TypedefModule.TypedefMeta]:
        """Get the list of typedef definitions."""
        return self._typedefs

    @property
    def aliases(self) -> list[AliasModule.AliasMeta]:
        """Get the list of alias definitions."""
        return self._aliases

    @property
    def enums(self) -> list[EnumModule.EnumMeta]:
        """Get the list of enum definitions."""
        return self._enums

    @property
    def flags(self) -> list[FlagModule.FlagMeta]:
        """Get the list of flag definitions."""
        return self._flags

    @property
    def structures(self) -> list[StructureModule.StructureMeta]:
        """Get the list of structure definitions."""
        return self._structures

    @property
    def interfaces(self) -> list[InterfaceModule.InterfaceMeta]:
        """Get the list of interface definitions."""
        return self._interfaces

    @property
    def functions(self) -> list[FunctionModule.FunctionMeta]:
        """Get the list of function definitions."""
        return self._functions

    def add_typedef(self, typedef: TypedefModule.TypedefMeta) -> None:
        """Add a typedef to the collection.

        Args:
            typedef: TypedefMeta instance to add
        """
        self._typedefs.append(typedef)

    def add_alias(self, alias: AliasModule.AliasMeta) -> None:
        """Add an alias to the collection.

        Args:
            alias: AliasMeta instance to add
        """
        self._aliases.append(alias)

    def add_enum(self, enum: EnumModule.EnumMeta) -> None:
        """Add an enum to the collection.

        Args:
            enum: EnumMeta instance to add
        """
        self._enums.append(enum)

    def add_flag(self, flag: FlagModule.FlagMeta) -> None:
        """Add a flag to the collection.

        Args:
            flag: FlagMeta instance to add
        """
        self._flags.append(flag)

    def add_structure(self, structure: StructureModule.StructureMeta) -> None:
        """Add a structure to the collection.

        Args:
            structure: StructureMeta instance to add
        """
        self._structures.append(structure)

    def add_interface(self, interface: InterfaceModule.InterfaceMeta) -> None:
        """Add an interface to the collection.

        Args:
            interface: InterfaceMeta instance to add
        """
        self._interfaces.append(interface)

    def add_function(self, function: FunctionModule.FunctionMeta) -> None:
        """Add a function to the collection.

        Args:
            function: FunctionMeta instance to add
        """
        self._functions.append(function)

"""Definition Collection Meta Module"""
import lv.cebbys.languages.ctd.meta.loader.interface as InterfaceModule
import lv.cebbys.languages.ctd.meta.loader.structure as StructureModule
import lv.cebbys.languages.ctd.meta.loader.function as FunctionModule
import lv.cebbys.languages.ctd.meta.loader.typedef as TypedefModule
import lv.cebbys.languages.ctd.meta.loader.alias as AliasModule
import lv.cebbys.languages.ctd.meta.loader.enum as EnumModule
import lv.cebbys.languages.ctd.meta.loader.flag as FlagModule
import typing as Typing

__all__ = ['DefinitionCollectionMeta']


class DefinitionCollectionMeta:
    """Collection of parsed type definitions from CTD modules."""

    def __init__(self):
        """Initialize an empty definition collection."""
        self._collections: list[list[Typing.Any]] = []

        def create_collection[T](_: type[T]) -> list[T]:
            out: list[T] = []
            self._collections.append(out)
            return out

        self._interfaces = create_collection(InterfaceModule.InterfaceMeta)
        self._structures = create_collection(StructureModule.StructureMeta)
        self._functions = create_collection(FunctionModule.FunctionMeta)
        self._typedefs = create_collection(TypedefModule.TypedefMeta)
        self._aliases = create_collection(AliasModule.AliasMeta)
        self._enums = create_collection(EnumModule.EnumMeta)
        self._flags = create_collection(FlagModule.FlagMeta)

    @property
    def typedefs(self):
        """Get the list of typedef definitions."""
        return self._typedefs

    @property
    def aliases(self):
        """Get the list of alias definitions."""
        return self._aliases

    @property
    def enums(self):
        """Get the list of enum definitions."""
        return self._enums

    @property
    def flags(self):
        """Get the list of flag definitions."""
        return self._flags

    @property
    def structures(self):
        """Get the list of structure definitions."""
        return self._structures

    @property
    def interfaces(self):
        """Get the list of interface definitions."""
        return self._interfaces

    @property
    def functions(self):
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

    def add_all(self, collection: 'DefinitionCollectionMeta') -> None:
        """Adds all definitions from collection to the collection.

        Args:
            collection: DefinitionCollectionMeta container of definitions to add
        """
        for i in range(len(self._collections)):
            self._collections[i].extend(collection._collections[i])

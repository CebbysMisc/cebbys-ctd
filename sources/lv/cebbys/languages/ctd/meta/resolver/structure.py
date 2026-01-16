"""Structure resolver module."""
import lv.cebbys.languages.ctd.meta.types as Meta
import lv.cebbys.languages.ctd.define.types as Define
import lv.cebbys.languages.ctd.meta.resolver.__api__ as Api


class StructureResolver(Api.BaseResolver):
    """Resolves structure metadata into structure definitions."""

    def create_instances(self) -> None:
        """Create structure instances and cache them (Phase 1).

        Creates StructureDefinition instances without resolving member types.
        """
        structure_meta: Meta.StructureMeta

        # Ensure structures collection exists
        if self._context.meta_collection.structures is None:
            return

        for structure_meta in self._context.meta_collection.structures:
            qualified_name: str = f"{structure_meta.namespace}::{structure_meta.name}"

            # Create structure instance
            structure_def: Define.StructureDefinition = Define.StructureDefinition(
                structure_meta.name,
                structure_meta.namespace
            )

            # Cache the instance
            self._context.type_cache[qualified_name] = structure_def

    def resolve_instances(self) -> None:
        """Resolve structure member types (Phase 2).

        Resolves all structure member type specifications using cached instances.
        """
        structure_meta: Meta.StructureMeta
        structure_def: Define.StructureDefinition

        # Ensure structures collection exists
        if self._context.meta_collection.structures is None:
            return

        for structure_meta in self._context.meta_collection.structures:
            qualified_name: str = f"{structure_meta.namespace}::{structure_meta.name}"

            # Get cached structure instance
            structure_def = self._context.type_cache[qualified_name]
            if not isinstance(structure_def, Define.StructureDefinition):
                raise Api.ResolutionError(
                    f"Expected StructureDefinition for {qualified_name}, "
                    f"got {type(structure_def).__name__}"
                )

            # Resolve members
            members: list[Define.StructureMemberDefinition] = self._resolve_structure_members(
                structure_meta, structure_meta.namespace
            )
            structure_def.set_members(members)

    def _resolve_structure_members(
        self,
        structure_meta: Meta.StructureMeta,
        namespace: str
    ) -> list[Define.StructureMemberDefinition]:
        """Resolve structure members.

        Args:
            structure_meta: Structure metadata
            namespace: Namespace for resolving type references

        Returns:
            List of resolved structure member definitions
        """
        members: list[Define.StructureMemberDefinition] = []
        member_meta: Meta.StructureMemberMeta
        type_spec: Define.TypeSpec

        for member_meta in structure_meta.members:
            # Parse and resolve the member type
            type_spec = self.parse_type_spec(member_meta.type_spec, namespace)

            # Create member definition
            member_def: Define.StructureMemberDefinition = Define.StructureMemberDefinition(
                member_meta.name,
                type_spec
            )
            members.append(member_def)

        return members

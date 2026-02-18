import lv.cebbys.languages.ctd.types.meta as Meta
import lv.cebbys.languages.ctd.types.ctd as Ctd
import lv.cebbys.languages.ctd.utility.logging as Logging
import typing as Typing

logger = Logging.get_logger(__name__)


class DeclarationConstructor:
    MAPPINGS: Typing.Final[dict[type, type[Ctd.Declaration]]] = {
        Meta.AliasMeta: Ctd.Alias,
        Meta.TypedefMeta: Ctd.Typedef,
        Meta.EnumMeta: Ctd.Enum,
        Meta.FlagMeta: Ctd.Flag,
        Meta.StructureMeta: Ctd.Structure,
        Meta.InterfaceMeta: Ctd.Interface,
        Meta.FunctionMeta: Ctd.Function,
    }

    @staticmethod
    def construct(meta: Meta.DeclarationMeta) -> Ctd.Declaration:
        """Construct a CTD declaration from metadata.
        
        Args:
            meta: Declaration metadata to construct from
            
        Returns:
            Constructed declaration object
            
        Raises:
            NotImplementedError: If declaration type is not supported
        """
        out: Ctd.Declaration

        meta_type = type(meta)
        logger.trace(f"Constructing declaration: {meta_type.__name__}")

        if meta_type not in DeclarationConstructor.MAPPINGS:
            raise BaseException(f"Mapping of Meta to Ctd not implemented for {meta_type}")

        ctd_type = DeclarationConstructor.MAPPINGS[meta_type]
        out = ctd_type()
        logger.trace(f"Created {type(out).__name__}: {meta.name}")
        out.name = meta.name
        out.meta = meta
        return out


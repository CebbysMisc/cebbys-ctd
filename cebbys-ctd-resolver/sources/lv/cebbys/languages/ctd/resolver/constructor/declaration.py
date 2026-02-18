import lv.cebbys.languages.ctd.types.meta as Meta
import lv.cebbys.languages.ctd.types.ctd as Ctd
import lv.cebbys.languages.ctd.utility.logging as Logging

logger = Logging.get_logger(__name__)


class DeclarationConstructor:
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

        logger.trace(f"Constructing declaration: {type(meta).__name__}")

        if isinstance(meta, Meta.AliasMeta):
            out = Ctd.Alias()
            logger.trace(f"Created Alias: {meta.name}")
            
        elif isinstance(meta, Meta.TypedefMeta):
            out = Ctd.Typedef()
            logger.trace(f"Created Typedef: {meta.name}")
            
        elif isinstance(meta, Meta.EnumMeta):
            out = Ctd.Enum()
            out.members = []
            logger.trace(f"Created Enum: {meta.name}")
            
        elif isinstance(meta, Meta.FlagMeta):
            out = Ctd.Flag()
            out.members = []
            logger.trace(f"Created Flag: {meta.name}")
            
        elif isinstance(meta, Meta.StructureMeta):
            out = Ctd.Structure()
            out.members = []
            logger.trace(f"Created Structure: {meta.name}")
            
        elif isinstance(meta, Meta.InterfaceMeta):
            out = Ctd.Interface()
            logger.trace(f"Created Interface: {meta.name}")
            
        elif isinstance(meta, Meta.FunctionMeta):
            out = Ctd.Function()
            out.parameters = []
            logger.trace(f"Created Function: {meta.name}")
        else:
            raise NotImplementedError(
                f"Construction for declaration type '{type(meta).__name__}' not implemented"
            )
        out.name = meta.name
        out.decorators = []
        out.meta = meta # type: ignore
        return out


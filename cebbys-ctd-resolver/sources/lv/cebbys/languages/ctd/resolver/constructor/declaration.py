import lv.cebbys.languages.ctd.types.meta as Meta
import lv.cebbys.languages.ctd.types.ctd as Ctd
import lv.cebbys.languages.ctd.utility.logging as Logging
import typing as Typing

from lv.cebbys.languages.ctd.resolver.event.emitter import (
    CtdInterfaceConstructEvent,
    CtdStructureConstructEvent,
    CtdFunctionConstructEvent,
    CtdTypedefConstructEvent,
    CtdAliasConstructEvent,
    CtdEnumConstructEvent,
    CtdFlagConstructEvent,
    Event,
)
from lv.cebbys.languages.ctd.types.meta import (
    DeclarationMeta
)
from lv.cebbys.languages.ctd.types.ctd import (
    Declaration,
    Namespace
)

logger = Logging.get_logger(__name__)

class DeclarationConstructorCtx:
    def __init__(self, factory: type[Ctd.Declaration], consumer: type[Event[Typing.Any]]) -> None:
        self.emitter: Typing.Final = consumer
        self.factory: Typing.Final = factory

class DeclarationConstructor:
    MAPPINGS: Typing.Final[dict[type, DeclarationConstructorCtx]] = {
        Meta.InterfaceMeta: DeclarationConstructorCtx(Ctd.Interface, CtdInterfaceConstructEvent),
        Meta.StructureMeta: DeclarationConstructorCtx(Ctd.Structure, CtdStructureConstructEvent),
        Meta.FunctionMeta: DeclarationConstructorCtx(Ctd.Function, CtdFunctionConstructEvent),
        Meta.TypedefMeta: DeclarationConstructorCtx(Ctd.Typedef, CtdTypedefConstructEvent),
        Meta.AliasMeta: DeclarationConstructorCtx(Ctd.Alias, CtdAliasConstructEvent),
        Meta.EnumMeta: DeclarationConstructorCtx(Ctd.Enum, CtdEnumConstructEvent),
        Meta.FlagMeta: DeclarationConstructorCtx(Ctd.Flag, CtdFlagConstructEvent),
    }

    @staticmethod
    def construct(namespace: Namespace, meta: DeclarationMeta) -> Declaration:
        """Construct a CTD declaration from metadata.
        
        Args:
            meta: Declaration metadata to construct from
            
        Returns:
            Constructed declaration object
            
        Raises:
            NotImplementedError: If declaration type is not supported
        """
        meta_type = type(meta)
        logger.trace(f"Constructing declaration: {meta_type.__name__}")

        if meta_type not in DeclarationConstructor.MAPPINGS:
            raise BaseException(f"Mapping of Meta to Ctd not implemented for {meta_type}")

        ctx = DeclarationConstructor.MAPPINGS[meta_type]
        declaration = ctx.factory(namespace, meta)
        logger.trace(f"Created {type(declaration).__name__}: {meta.name}")
        ctx.emitter.emit(declaration)
        return declaration


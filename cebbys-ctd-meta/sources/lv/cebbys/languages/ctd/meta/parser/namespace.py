import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.meta.parser.declaration as DeclarationModule
import lv.cebbys.languages.ctd.types.meta as Meta
import typing as Typing


import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)


class CtdNamespaceContextParser(Api.CtdContextParserBase[Api.CtdGrammar.NamespaceDeclarationContext, Meta.NamespaceMeta]):
    def __init__(
        self,
        consumers: dict[
            type[Meta.DeclarationMeta],
            Typing.Callable[[Meta.NamespaceMeta], Typing.Callable[[Typing.Any], None]]
        ]
    ) -> None:
        super().__init__()
        self._consumers = {
            k: v for k, v in consumers.items()
        }

    @staticmethod
    def instance() -> Api.CtdContextParser[Api.CtdGrammar.NamespaceDeclarationContext, Meta.NamespaceMeta]:
        return INSTANCE

    def parse(self, ctx: Api.CtdGrammar.NamespaceDeclarationContext):
        LOGGER.trace("Parsing namespace declaration")

        namespace: str = self.qualified_name(self.rule(ctx, Api.CtdGrammar.QualifiedNameContext))

        out = Meta.NamespaceMeta()
        for use_ctx in self.rules(ctx, Api.CtdGrammar.UseDeclarationContext):
            out.add_use(self.qualified_name(self.rule(use_ctx, Api.CtdGrammar.QualifiedNameContext)))

        for declaration_ctx in self.rules(ctx, Api.CtdGrammar.DeclarationContext):
            meta = DeclarationModule.CtdDeclarationContextParser.instance().parse(namespace, declaration_ctx)
            self._consumers[type(meta)](out)(meta)
        
        LOGGER.debug(f"Namespace '{namespace}' parsing complete: {len(out.uses)} use(s) and {len(out.declarations)} declaration(s) statements")

        return out


INSTANCE = CtdNamespaceContextParser({
    Meta.StructureMeta: lambda namespace: namespace.add_structure,
    Meta.InterfaceMeta: lambda namespace: namespace.add_interface,
    Meta.FunctionMeta: lambda namespace: namespace.add_function,
    Meta.TypedefMeta: lambda namespace: namespace.add_typedef,
    Meta.AliasMeta: lambda namespace: namespace.add_alias,
    Meta.EnumMeta: lambda namespace: namespace.add_enum,
    Meta.FlagMeta: lambda namespace: namespace.add_flag
})

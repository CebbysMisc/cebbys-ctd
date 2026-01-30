from typing import Iterable
import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as Meta


class CtdDecoratorContextParser(Api.CtdContextParserBase[Api.CtdParser.DecoratorContext, Meta.DecoratorMeta]):
    @staticmethod
    def instance() -> 'CtdDecoratorContextParser':
        return INSTANCE

    def parse(self, ctx: Api.CtdParser.DecoratorContext) -> Meta.DecoratorMeta:
        """Parse decorator and create DecoratorMeta.

        Args:
            ctx: Decorator context
        """
        name = self.text(self.token(ctx, Api.CtdParser.IDENTIFIER))
        arguments: list[str] = []

        args_ctx = self.optional_rule(ctx, Api.CtdParser.DecoratorArgumentsContext)
        if args_ctx:
            for arg_ctx in self.rules(args_ctx, Api.CtdParser.DecoratorArgumentContext):
                arg_text = self.text(arg_ctx)
                # Strip quotes from string literals
                if arg_text.startswith('"') and arg_text.endswith('"'):
                    arg_text = arg_text[1:-1]
                arguments.append(arg_text)

        return Meta.DecoratorMeta(name, arguments if arguments else None)

    def parse_all(self, contexts: Iterable[Api.CtdParser.DecoratorContext]) -> list[Meta.DecoratorMeta]:
        """Parse multiple decorator contexts.

        Args:
            contexts: Iterable of decorator contexts

        Returns:
            List of DecoratorMeta objects
        """
        return [self.parse(ctx) for ctx in contexts]


INSTANCE = CtdDecoratorContextParser()

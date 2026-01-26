"""Function resolver module."""
import lv.cebbys.languages.ctd.meta.loader as Meta
import lv.cebbys.languages.ctd.define as Define
import lv.cebbys.languages.ctd.meta.resolver.__api__ as Api


class FunctionResolver(Api.BaseResolver):
    """Resolves function metadata into function definitions."""

    def create_instances(self) -> None:
        """Create function instances and cache them (Phase 1).

        Creates FunctionDefinition instances without resolving types.
        """
        function_meta: Meta.FunctionMeta

        for function_meta in self._context.meta_collection.functions:
            qualified_name: str = f"{function_meta.namespace}::{function_meta.name}"

            # Convert meta decorators to definition decorators
            decorators: list[Define.DecoratorDefinition] = self._convert_decorators(
                function_meta.decorators
            )

            # Create function instance
            function_def: Define.FunctionDefinition = Define.FunctionDefinition(
                function_meta.name,
                function_meta.namespace,
                decorators=decorators
            )

            # Cache the instance
            self._context.type_cache[qualified_name] = function_def

    def resolve_instances(self) -> None:
        """Resolve function return types and parameter types (Phase 2).

        Resolves all function type specifications using cached instances.
        """
        function_meta: Meta.FunctionMeta

        for function_meta in self._context.meta_collection.functions:
            qualified_name: str = f"{function_meta.namespace}::{function_meta.name}"

            # Get cached function instance
            function_def = self._context.type_cache[qualified_name]
            if not isinstance(function_def, Define.FunctionDefinition):
                raise Api.ResolutionError(
                    f"Expected FunctionDefinition for {qualified_name}, "
                    f"got {type(function_def).__name__}"
                )

            # Resolve return type
            return_type: Define.TypeSpec = self.parse_type_spec(
                function_meta.return_type, function_meta.namespace
            )
            function_def.set_return_type(return_type)

            # Resolve parameters
            parameters: list[Define.ParameterDefinition] = self._resolve_parameters(
                function_meta, function_meta.namespace
            )
            function_def.set_parameters(parameters)

    def _resolve_parameters(
        self,
        function_meta: Meta.FunctionMeta,
        namespace: str
    ) -> list[Define.ParameterDefinition]:
        """Resolve function parameters.

        Args:
            function_meta: Function metadata
            namespace: Namespace for resolving type references

        Returns:
            List of resolved parameter definitions
        """
        parameters: list[Define.ParameterDefinition] = []
        param_meta: Meta.ParameterMeta
        type_spec: Define.TypeSpec

        for param_meta in function_meta.parameters:
            # Parse and resolve the parameter type
            type_spec = self.parse_type_spec(param_meta.type_spec, namespace)

            # Convert meta decorators to definition decorators
            decorators: list[Define.DecoratorDefinition] = self._convert_decorators(
                param_meta.decorators
            )

            # Create parameter definition
            param_def: Define.ParameterDefinition = Define.ParameterDefinition(
                param_meta.name,
                type_spec,
                decorators
            )
            parameters.append(param_def)

        return parameters

    def _convert_decorators(
        self,
        meta_decorators: tuple[Meta.DecoratorMeta, ...]
    ) -> list[Define.DecoratorDefinition]:
        """Convert meta decorators to definition decorators.

        Args:
            meta_decorators: Tuple of meta decorator objects

        Returns:
            List of definition decorator objects
        """
        decorators: list[Define.DecoratorDefinition] = []
        meta_decorator: Meta.DecoratorMeta

        for meta_decorator in meta_decorators:
            decorator_def: Define.DecoratorDefinition = Define.DecoratorDefinition(
                meta_decorator.name,
                meta_decorator.arguments
            )
            decorators.append(decorator_def)

        return decorators

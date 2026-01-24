"""CTD Parser Visitor

This module implements an ANTLR4 visitor to transform parse trees into Meta objects.
"""
import typing as Typing
import lv.cebbys.languages.ctd.__api__ as Api
import lv.cebbys.languages.ctd.meta.loader as Meta
import lv.cebbys.languages.ctd.antlr4.GtdParser as GtdParser
import lv.cebbys.languages.ctd.antlr4.GtdVisitor as GtdVisitor

__all__ = ['MetaVisitor']


class MetaVisitor(GtdVisitor.GtdVisitor):
    """Visitor that transforms ANTLR4 parse tree into Meta objects."""
    
    def __init__(self):
        """Initialize the visitor."""
        super().__init__()
        self._current_namespace: str
        self._current_used_namespaces: list[str]
        self._collection: Meta.DefinitionCollectionMeta
        self._imports: list[str]
        self._namespace_uses: dict[str, list[str]]
        
        self._current_namespace = ""
        self._current_used_namespaces = []
        self._collection = Meta.DefinitionCollectionMeta()
        self._imports = []
        self._namespace_uses = {}
    
    @property
    def collection(self) -> Meta.DefinitionCollectionMeta:
        """Get the collected metadata."""
        return self._collection
    
    @property
    def imports(self) -> list[str]:
        """Get the list of imported module names."""
        return self._imports
    
    @property
    def namespace_uses(self) -> dict[str, list[str]]:
        """Get mapping of namespace to list of used namespaces."""
        return self._namespace_uses
    
    def visitCompilationUnit(
        self,
        ctx: GtdParser.GtdParser.CompilationUnitContext
    ) -> None:
        """Visit compilation unit and process imports and namespace declarations.
        
        Args:
            ctx: Compilation unit context
        """
        import_ctx: GtdParser.GtdParser.ImportDeclarationContext
        namespace_ctx: GtdParser.GtdParser.NamespaceDeclarationContext
        
        # Process imports first
        for import_ctx in ctx.importDeclaration():
            self.visitImportDeclaration(import_ctx)
        
        # Then process namespaces
        for namespace_ctx in ctx.namespaceDeclaration():
            self.visitNamespaceDeclaration(namespace_ctx)
    
    def visitImportDeclaration(
        self,
        ctx: GtdParser.GtdParser.ImportDeclarationContext
    ) -> None:
        """Visit import declaration and store the imported module name.
        
        Args:
            ctx: Import declaration context
        """
        import_path: str
        
        # Get the string literal and remove quotes
        import_path = ctx.STRING_LITERAL().getText()[1:-1]
        self._imports.append(import_path)
    
    def visitNamespaceDeclaration(
        self,
        ctx: GtdParser.GtdParser.NamespaceDeclarationContext
    ) -> None:
        """Visit namespace declaration and process use declarations and type declarations.
        
        Args:
            ctx: Namespace declaration context
        """
        qualified_name: str
        use_ctx: GtdParser.GtdParser.UseDeclarationContext
        declaration_ctx: GtdParser.GtdParser.DeclarationContext
        previous_namespace: str
        previous_used_namespaces: list[str]
        
        # Get qualified namespace name
        qualified_name = self._get_qualified_name(ctx.qualifiedName())
        
        # Save previous namespace and used namespaces
        previous_namespace = self._current_namespace
        previous_used_namespaces = self._current_used_namespaces
        
        # Set current namespace and reset used namespaces
        self._current_namespace = qualified_name
        self._current_used_namespaces = []
        
        # Process use declarations
        for use_ctx in ctx.useDeclaration():
            self.visitUseDeclaration(use_ctx)
        
        # Store the used namespaces for this namespace
        self._namespace_uses[qualified_name] = self._current_used_namespaces.copy()
        
        # Visit all declarations in this namespace
        for declaration_ctx in ctx.declaration():
            self.visitDeclaration(declaration_ctx)
        
        # Restore previous namespace and used namespaces
        self._current_namespace = previous_namespace
        self._current_used_namespaces = previous_used_namespaces
    
    def visitUseDeclaration(
        self,
        ctx: GtdParser.GtdParser.UseDeclarationContext
    ) -> None:
        """Visit use declaration and track the used namespace.
        
        Args:
            ctx: Use declaration context
        """
        used_namespace: str
        
        # Get the qualified namespace being used
        used_namespace = self._get_qualified_name(ctx.qualifiedName())
        self._current_used_namespaces.append(used_namespace)
    
    def visitDeclaration(
        self,
        ctx: GtdParser.GtdParser.DeclarationContext
    ) -> None:
        """Visit a declaration (typedef, alias, enum, flag, structure, interface, or function).

        Args:
            ctx: Declaration context
        """
        if ctx.typedefDeclaration():
            self.visitTypedefDeclaration(ctx.typedefDeclaration())
        elif ctx.aliasDeclaration():
            self.visitAliasDeclaration(ctx.aliasDeclaration())
        elif ctx.enumDeclaration():
            self.visitEnumDeclaration(ctx.enumDeclaration())
        elif ctx.flagDeclaration():
            self.visitFlagDeclaration(ctx.flagDeclaration())
        elif ctx.structureDeclaration():
            self.visitStructureDeclaration(ctx.structureDeclaration())
        elif ctx.interfaceDeclaration():
            self.visitInterfaceDeclaration(ctx.interfaceDeclaration())
        elif ctx.functionDeclaration():
            self.visitFunctionDeclaration(ctx.functionDeclaration())
    
    def visitTypedefDeclaration(
        self,
        ctx: GtdParser.GtdParser.TypedefDeclarationContext
    ) -> None:
        """Visit typedef declaration and create TypedefMeta.

        Args:
            ctx: Typedef declaration context
        """
        name: str
        type_spec: str
        typedef_meta: Meta.TypedefMeta

        # Get typedef name
        name = ctx.IDENTIFIER().getText()

        # Get type specification
        type_spec = self._get_type_spec(ctx.typeSpec())

        # Create and add typedef metadata
        typedef_meta = Meta.TypedefMeta(name, type_spec, self._current_namespace)
        self._collection.add_typedef(typedef_meta)

    def visitAliasDeclaration(
        self,
        ctx: GtdParser.GtdParser.AliasDeclarationContext
    ) -> None:
        """Visit alias declaration and create AliasMeta.

        Args:
            ctx: Alias declaration context
        """
        name: str
        type_spec: str
        alias_meta: Meta.AliasMeta

        # Get alias name
        name = ctx.IDENTIFIER().getText()

        # Get type specification
        type_spec = self._get_type_spec(ctx.typeSpec())

        # Create and add alias metadata
        alias_meta = Meta.AliasMeta(name, type_spec, self._current_namespace)
        self._collection.add_alias(alias_meta)

    def visitEnumDeclaration(
        self,
        ctx: GtdParser.GtdParser.EnumDeclarationContext
    ) -> None:
        """Visit enum declaration and create EnumMeta.
        
        Args:
            ctx: Enum declaration context
        """
        name: str
        base_type: str | None
        members: list[Meta.EnumMemberMeta]
        enum_meta: Meta.EnumMeta
        
        # Get enum name
        name = ctx.IDENTIFIER().getText()
        
        # Get base type if specified
        base_type = None
        if ctx.typeSpec():
            base_type = self._get_type_spec(ctx.typeSpec())
        
        # Get enum members
        members = []
        if ctx.enumMemberList():
            members = self._get_enum_members(ctx.enumMemberList())
        
        # Create and add enum metadata
        enum_meta = Meta.EnumMeta(name, self._current_namespace, base_type, members)
        self._collection.add_enum(enum_meta)
    
    def visitFlagDeclaration(
        self,
        ctx: GtdParser.GtdParser.FlagDeclarationContext
    ) -> None:
        """Visit flag declaration and create FlagMeta.
        
        Args:
            ctx: Flag declaration context
        """
        name: str
        base_type: str | None
        members: list[Meta.FlagMemberMeta]
        flag_meta: Meta.FlagMeta
        
        # Get flag name
        name = ctx.IDENTIFIER().getText()
        
        # Get base type if specified
        base_type = None
        if ctx.typeSpec():
            base_type = self._get_type_spec(ctx.typeSpec())
        
        # Get flag members
        members = []
        if ctx.flagMemberList():
            members = self._get_flag_members(ctx.flagMemberList())
        
        # Create and add flag metadata
        flag_meta = Meta.FlagMeta(name, self._current_namespace, base_type, members)
        self._collection.add_flag(flag_meta)
    
    def _get_qualified_name(
        self,
        ctx: GtdParser.GtdParser.QualifiedNameContext
    ) -> str:
        """Extract qualified name from context.
        
        Args:
            ctx: Qualified name context
            
        Returns:
            Qualified name as string (e.g., 'ns1::ns2::name')
        """
        identifiers: list[str]
        
        identifiers = [id_token.getText() for id_token in ctx.IDENTIFIER()]
        return '::'.join(identifiers)
    
    def _get_type_spec(
        self,
        ctx: GtdParser.GtdParser.TypeSpecContext
    ) -> str:
        """Extract type specification as string.

        Args:
            ctx: Type spec context

        Returns:
            Type specification string
        """
        parts: list[str]
        array_ctx: GtdParser.GtdParser.ArrayModifierContext | None
        pointer_ctx: GtdParser.GtdParser.PointerModifierContext | None

        parts = []

        # Handle sign modifier
        if ctx.signModifier():
            parts.append(ctx.signModifier().getText())

        # Handle primitive type
        if ctx.primitiveType():
            parts.append(ctx.primitiveType().getText())

        # Handle type reference
        if ctx.typeReference():
            parts.append(ctx.typeReference().qualifiedName().getText())

        # Handle array modifier - check in typeSpec first, then in typeReference
        array_ctx = ctx.arrayModifier()
        if array_ctx is None and ctx.typeReference():
            array_ctx = ctx.typeReference().arrayModifier()

        if array_ctx:
            parts.append(array_ctx.getText())

        # Handle pointer modifier - check in typeSpec first, then in typeReference
        pointer_ctx = ctx.pointerModifier()
        if pointer_ctx is None and ctx.typeReference():
            pointer_ctx = ctx.typeReference().pointerModifier()

        if pointer_ctx:
            parts.append(pointer_ctx.getText())

        return ' '.join(parts)
    
    def _get_enum_members(
        self,
        ctx: GtdParser.GtdParser.EnumMemberListContext
    ) -> list[Meta.EnumMemberMeta]:
        """Extract enum members from context.
        
        Args:
            ctx: Enum member list context
            
        Returns:
            List of EnumMemberMeta objects
        """
        members: list[Meta.EnumMemberMeta]
        member_ctx: GtdParser.GtdParser.EnumMemberContext
        name: str
        value: int | None
        
        members = []
        
        for member_ctx in ctx.enumMember():
            name = member_ctx.IDENTIFIER().getText()
            value = None
            
            if member_ctx.INTEGER_LITERAL():
                value = int(member_ctx.INTEGER_LITERAL().getText())
            elif member_ctx.HEX_LITERAL():
                value = int(member_ctx.HEX_LITERAL().getText(), 16)
            
            members.append(Meta.EnumMemberMeta(name, value))
        
        return members
    
    def _get_flag_members(
        self,
        ctx: GtdParser.GtdParser.FlagMemberListContext
    ) -> list[Meta.FlagMemberMeta]:
        """Extract flag members from context.

        Args:
            ctx: Flag member list context

        Returns:
            List of FlagMemberMeta objects
        """
        members: list[Meta.FlagMemberMeta]
        member_ctx: GtdParser.GtdParser.FlagMemberContext
        name: str
        value: int | None

        members = []

        for member_ctx in ctx.flagMember():
            name = member_ctx.IDENTIFIER().getText()
            value = None

            if member_ctx.INTEGER_LITERAL():
                value = int(member_ctx.INTEGER_LITERAL().getText())
            elif member_ctx.HEX_LITERAL():
                # Parse hex literal (e.g., "0x20" -> 32)
                hex_text = member_ctx.HEX_LITERAL().getText()
                value = int(hex_text, 16)

            members.append(Meta.FlagMemberMeta(name, value))

        return members
    
    def visitStructureDeclaration(
        self,
        ctx: GtdParser.GtdParser.StructureDeclarationContext
    ) -> None:
        """Visit structure declaration and create StructureMeta.
        
        Args:
            ctx: Structure declaration context
        """
        name: str
        members: list[Meta.StructureMemberMeta]
        structure_meta: Meta.StructureMeta
        
        # Get structure name
        name = ctx.IDENTIFIER().getText()
        
        # Get structure members
        members = []
        if ctx.structureMemberList():
            members = self._get_structure_members(ctx.structureMemberList())
        
        # Create and add structure metadata
        structure_meta = Meta.StructureMeta(name, self._current_namespace, members)
        self._collection.add_structure(structure_meta)
    
    def _get_structure_members(
        self,
        ctx: GtdParser.GtdParser.StructureMemberListContext
    ) -> list[Meta.StructureMemberMeta]:
        """Extract structure members from context.

        Args:
            ctx: Structure member list context

        Returns:
            List of StructureMemberMeta objects
        """
        members: list[Meta.StructureMemberMeta]
        member_ctx: GtdParser.GtdParser.StructureMemberContext
        name: str
        type_spec: str

        members = []

        for member_ctx in ctx.structureMember():
            type_spec = self._get_type_spec(member_ctx.typeSpec())
            name = member_ctx.IDENTIFIER().getText()
            members.append(Meta.StructureMemberMeta(name, type_spec))

        return members

    def visitInterfaceDeclaration(
        self,
        ctx: GtdParser.GtdParser.InterfaceDeclarationContext
    ) -> None:
        """Visit interface declaration and create InterfaceMeta.

        Args:
            ctx: Interface declaration context
        """
        name: str
        methods: list[Meta.FunctionMeta]
        interface_meta: Meta.InterfaceMeta

        # Get interface name
        name = ctx.IDENTIFIER().getText()

        # Get interface methods
        methods = []
        if ctx.interfaceMethodList():
            methods = self._get_interface_methods(ctx.interfaceMethodList())

        # Create and add interface metadata
        interface_meta = Meta.InterfaceMeta(name, self._current_namespace, methods)
        self._collection.add_interface(interface_meta)

    def _get_interface_methods(
        self,
        ctx: GtdParser.GtdParser.InterfaceMethodListContext
    ) -> list[Meta.FunctionMeta]:
        """Extract interface methods from context.

        Args:
            ctx: Interface method list context

        Returns:
            List of FunctionMeta objects representing interface methods
        """
        methods: list[Meta.FunctionMeta]
        func_ctx: GtdParser.GtdParser.FunctionDeclarationContext
        name: str
        return_type: str
        parameters: list[Meta.ParameterMeta]
        decorators: list[Meta.DecoratorMeta]

        methods = []

        for func_ctx in ctx.functionDeclaration():
            # Get function name
            name = func_ctx.IDENTIFIER().getText()

            # Get return type
            return_type = self._get_type_spec(func_ctx.typeSpec())

            # Get parameters
            parameters = []
            if func_ctx.parameterList():
                parameters = self._get_parameters(func_ctx.parameterList())

            # Get decorators if present
            decorators = self._get_decorators(func_ctx.decorator())

            # Create function meta for the interface method
            method_meta = Meta.FunctionMeta(
                name,
                self._current_namespace,
                return_type,
                parameters,
                decorators
            )
            methods.append(method_meta)

        return methods

    def visitFunctionDeclaration(
        self,
        ctx: GtdParser.GtdParser.FunctionDeclarationContext
    ) -> None:
        """Visit function declaration and create FunctionMeta.

        Args:
            ctx: Function declaration context
        """
        name: str
        return_type: str
        parameters: list[Meta.ParameterMeta]
        decorators: list[Meta.DecoratorMeta]
        function_meta: Meta.FunctionMeta

        # Get function name
        name = ctx.IDENTIFIER().getText()

        # Get return type
        return_type = self._get_type_spec(ctx.typeSpec())

        # Get parameters
        parameters = []
        if ctx.parameterList():
            parameters = self._get_parameters(ctx.parameterList())

        # Get decorators if present
        decorators = self._get_decorators(ctx.decorator())

        # Create and add function metadata
        function_meta = Meta.FunctionMeta(
            name,
            self._current_namespace,
            return_type,
            parameters,
            decorators
        )
        self._collection.add_function(function_meta)

    def _get_parameters(
        self,
        ctx: GtdParser.GtdParser.ParameterListContext
    ) -> list[Meta.ParameterMeta]:
        """Extract function parameters from context.

        Args:
            ctx: Parameter list context

        Returns:
            List of ParameterMeta objects
        """
        parameters: list[Meta.ParameterMeta]
        param_ctx: GtdParser.GtdParser.ParameterContext
        name: str
        type_spec: str
        decorators: list[Meta.DecoratorMeta]

        parameters = []

        for param_ctx in ctx.parameter():
            type_spec = self._get_type_spec(param_ctx.typeSpec())
            name = param_ctx.IDENTIFIER().getText()

            # Parse decorators if present
            decorators = self._get_decorators(param_ctx.decorator())

            parameters.append(Meta.ParameterMeta(name, type_spec, decorators))

        return parameters

    def _get_decorators(
        self,
        decorator_contexts: list[GtdParser.GtdParser.DecoratorContext]
    ) -> list[Meta.DecoratorMeta]:
        """Extract decorators from context list.

        Args:
            decorator_contexts: List of decorator contexts

        Returns:
            List of DecoratorMeta objects
        """
        decorators: list[Meta.DecoratorMeta]
        decorator_ctx: GtdParser.GtdParser.DecoratorContext
        name: str
        arguments: list[str]
        arg_ctx: GtdParser.GtdParser.DecoratorArgumentContext

        decorators = []

        for decorator_ctx in decorator_contexts:
            name = decorator_ctx.IDENTIFIER().getText()
            arguments = []

            # Parse arguments if present
            if decorator_ctx.decoratorArguments():
                for arg_ctx in decorator_ctx.decoratorArguments().decoratorArgument():
                    # Get the text and strip quotes from string literals
                    arg_text = arg_ctx.getText()
                    if arg_ctx.STRING_LITERAL():
                        arg_text = arg_text[1:-1]  # Remove surrounding quotes
                    arguments.append(arg_text)

            decorators.append(Meta.DecoratorMeta(name, arguments))

        return decorators

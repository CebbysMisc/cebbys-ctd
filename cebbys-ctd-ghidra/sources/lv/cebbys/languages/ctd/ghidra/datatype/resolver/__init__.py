from lv.cebbys.languages.ctd.ghidra.datatype.__utility__ import (
    get_category_path
)
from lv.cebbys.languages.ctd.types.ctd import (
    Declaration,
    Interface,
    Structure,
    Namespace,
    Function,
    Builtin,
    Pointer,
    Typedef,
    Alias,
    Array,
    Enum,
    Flag,
    Class,
)
from ghidra.program.model.data import (  # type: ignore
    FunctionDefinitionDataType,
    AbstractIntegerDataType,
    ParameterDefinitionImpl,
    StructureDataType,
    LongLongDataType,
    WideCharDataType,
    IntegerDataType,
    PointerDataType,
    TypedefDataType,
    Float4DataType,
    Float8DataType,
    ArrayDataType,
    ShortDataType,
    CharDataType,
    ByteDataType,
    VoidDataType,
    EnumDataType,
    DataType,
)


class DatatypeResolver:
    __cache__: dict[Declaration, DataType] = {}

    @classmethod
    def resolve(cls, declaration: Declaration) -> DataType:
        cls.__cache__.clear()
        if declaration not in cls.__cache__:
            if isinstance(declaration, Builtin):
                cls.__cache__[declaration] = cls.resolve_builtin(declaration)
            elif isinstance(declaration, Pointer):
                base = declaration.base.value
                cls.__cache__[declaration] = PointerDataType(cls.resolve(base))
            elif isinstance(declaration, Array):
                base = declaration.base.value
                size = declaration.size
                cls.__cache__[declaration] = ArrayDataType(cls.resolve(base), size)
            elif isinstance(declaration, Alias):
                cls.__cache__[declaration] = cls.resolve(declaration.base.value)
            elif isinstance(declaration, Typedef):
                cls.__cache__[declaration] = cls.resolve_typedef(declaration)
            elif isinstance(declaration, Function):
                cls.__cache__[declaration] = cls.resolve_function(declaration)
            elif isinstance(declaration, Class):
                cls.__cache__[declaration] = cls.resolve_class(declaration)
            elif isinstance(declaration, Interface):
                cls.__cache__[declaration] = cls.resolve_interface(declaration)
            elif isinstance(declaration, Structure):
                cls.__cache__[declaration] = cls.resolve_structure(declaration)
            elif isinstance(declaration, Enum):
                cls.__cache__[declaration] = cls.resolve_enum(declaration)
            elif isinstance(declaration, Flag):
                cls.__cache__[declaration] = cls.resolve_flag(declaration)
            else:
                raise NotImplementedError(
                    f"Not implemented resolution for {type(declaration)} {declaration}"
                )
        return cls.__cache__[declaration]

    @classmethod
    def resolve_builtin(cls, declaration: Builtin) -> DataType:
        name = declaration.name
        if name == "void":
            return VoidDataType()
        if name == "byte":
            return ByteDataType()
        if name == "short":
            return ShortDataType()
        if name == "int":
            return IntegerDataType()
        if name == "long":
            return LongLongDataType()
        if name == "float":
            return Float4DataType()
        if name == "double":
            return Float8DataType()
        if name == "char":
            return CharDataType()
        if name == "wchar":
            return WideCharDataType()
        raise NotImplementedError(f"Cannot resolve builtin {declaration.name}")

    @classmethod
    def resolve_typedef(cls, declaration: Typedef) -> DataType:
        category_path = get_category_path(declaration.namespace)
        return TypedefDataType(
            category_path,
            declaration.name,
            cls.resolve_typedef_base(
                declaration.signed,
                declaration.base.value
            )
        )

    @classmethod
    def resolve_function(cls, declaration: Function) -> DataType:
        category_path = get_category_path(declaration.namespace)

        function = FunctionDefinitionDataType(
            category_path,
            declaration.name
        )

        return_type = declaration.return_type
        if return_type is not None:
            function.setReturnType(cls.resolve(return_type.value))  # type: ignore
        else:
            function.setReturnType(VoidDataType())  # type: ignore

        params: list[ParameterDefinitionImpl] = []
        for parameter in declaration.parameters:
            argument_type = cls.resolve(parameter.type.value)
            params.append(ParameterDefinitionImpl(
                parameter.name, argument_type, None))  # type: ignore
        function.setArguments(params)  # type: ignore

        return function

    @classmethod
    def resolve_structure(cls, declaration: Structure) -> DataType:
        category_path = get_category_path(declaration.namespace)
        struct = StructureDataType(category_path, declaration.name, 0)
        for member in declaration.members:
            member_type = cls.resolve(member.type.value)
            struct.add(member_type, member_type.getLength(), member.name, None)  # type: ignore
        return struct

    @classmethod
    def resolve_enum(cls, declaration: Enum) -> DataType:
        category_path = get_category_path(declaration.namespace)
        size = 4
        if declaration.base is not None:
            size = cls.resolve(declaration.base.value).getLength()
        enum = EnumDataType(category_path, declaration.name, size)
        for member in declaration.members:
            enum.add(member.name, member.value)  # type: ignore
        return enum

    @classmethod
    def resolve_flag(cls, declaration: Flag) -> DataType:
        category_path = get_category_path(declaration.namespace)
        size = 4
        if declaration.base is not None:
            size = cls.resolve(declaration.base.value).getLength()
        enum = EnumDataType(category_path, declaration.name, size)
        for member in declaration.members:
            enum.add(member.name, 1 << member.offset)  # type: ignore
        return enum

    @classmethod
    def resolve_class(cls, declaration: Class) -> DataType:
        category_path = get_category_path(declaration.namespace)

        # Build vtable struct: __vtable_<Name>
        # Includes vtable entries from all base classes/interfaces, then own methods
        vtable = StructureDataType(category_path, f"__vtable_{declaration.name}", 0)

        for base_ref in declaration.bases:
            base = base_ref.value
            if isinstance(base, Class):
                # Inherit vtable entries from base class vtable
                base_vtable_dt = cls.resolve(base)
                if isinstance(base_vtable_dt, StructureDataType):
                    # The resolved class is the main struct; resolve the vtable directly
                    base_vtable = StructureDataType(
                        category_path, f"__vtable_{base.name}", 0
                    )
                    base_vtable_ptr = PointerDataType(base_vtable)
                    vtable.add(base_vtable_ptr, base_vtable_ptr.getLength(), f"base_{base.name}", None)  # type: ignore
            elif isinstance(base, Interface):
                # Inherit vtable entries from base interface
                base_dt = cls.resolve(base)
                base_ptr = PointerDataType(base_dt)
                vtable.add(base_ptr, base_ptr.getLength(), f"base_{base.name}", None)  # type: ignore

        for method in declaration.methods:
            method_dt = cls.resolve(method)
            method_ptr = PointerDataType(method_dt)
            vtable.add(method_ptr, method_ptr.getLength(), method.meta.name, None)  # type: ignore

        # Build main struct: <Name>
        # First member is a pointer to the vtable, then all data members
        class_struct = StructureDataType(category_path, declaration.name, 0)
        vtable_ptr = PointerDataType(vtable)
        class_struct.add(vtable_ptr, vtable_ptr.getLength(), "__vtable", None)  # type: ignore

        # Include data members from bases (Structure or Class bases)
        for base_ref in declaration.bases:
            base = base_ref.value
            if isinstance(base, (Structure, Class)):
                for member in base.members:
                    member_type = cls.resolve(member.type.value)
                    class_struct.add(member_type, member_type.getLength(), f"base_{base.name}_{member.name}", None)  # type: ignore

        # Own data members
        for member in declaration.members:
            member_type = cls.resolve(member.type.value)
            class_struct.add(member_type, member_type.getLength(), member.name, None)  # type: ignore

        return class_struct

    @classmethod
    def resolve_interface(cls, declaration: Interface) -> DataType:
        category_path = get_category_path(declaration.namespace)

        vtable = StructureDataType(category_path, f"{declaration.name}Vtable", 0)

        if declaration.base is not None:
            base_dt = cls.resolve(declaration.base.value)
            base_ptr = PointerDataType(base_dt)
            vtable.add(base_ptr, base_ptr.getLength(), "base", None)  # type: ignore

        for method in declaration.methods:
            method_dt = cls.resolve(method)
            method_ptr = PointerDataType(method_dt)
            vtable.add(method_ptr, method_ptr.getLength(), method.meta.name, None)  # type: ignore

        interface_struct = StructureDataType(category_path, declaration.name, 0)
        vtable_ptr = PointerDataType(vtable)
        interface_struct.add(vtable_ptr, vtable_ptr.getLength(), "vtable", None)  # type: ignore

        return interface_struct

    @classmethod
    def resolve_typedef_base(cls, signed: bool | None, base: Declaration) -> DataType:
        base_type: DataType = cls.resolve(base)
        if signed is not None:
            while isinstance(base_type, TypedefDataType):
                typedef: TypedefDataType = base_type
                base_type = typedef.getBaseDataType()

            if not isinstance(base_type, AbstractIntegerDataType):
                raise TypeError(f"Cannot apply signedness to non-integer type {base_type}")

            return get_integer(signed, base_type)
        else:
            while isinstance(base_type, TypedefDataType):
                typedef: TypedefDataType = base_type
                base_type = typedef.getBaseDataType()

        return base_type


def get_integer(signed: bool, integer: AbstractIntegerDataType) -> AbstractIntegerDataType:
    signedness = integer.isSigned()
    if signedness == signed:
        return integer
    else:
        return integer.getOppositeSignednessDataType()

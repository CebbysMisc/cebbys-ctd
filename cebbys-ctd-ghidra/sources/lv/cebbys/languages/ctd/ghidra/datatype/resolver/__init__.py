from lv.cebbys.languages.ctd.ghidra.datatype.__utility__ import (
    get_category_path
)
from lv.cebbys.languages.ctd.types.ctd import (
    Declaration,
    Builtin,
    Pointer,
    Typedef,
    Alias,
    Array,
)
from ghidra.program.model.data import (  # type: ignore
    AbstractIntegerDataType,
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

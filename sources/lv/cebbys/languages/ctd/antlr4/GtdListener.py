# Generated from resources/grammar/Gtd.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GtdParser import GtdParser
else:
    from GtdParser import GtdParser

# This class defines a complete listener for a parse tree produced by GtdParser.
class GtdListener(ParseTreeListener):

    # Enter a parse tree produced by GtdParser#compilationUnit.
    def enterCompilationUnit(self, ctx:GtdParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by GtdParser#compilationUnit.
    def exitCompilationUnit(self, ctx:GtdParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by GtdParser#importDeclaration.
    def enterImportDeclaration(self, ctx:GtdParser.ImportDeclarationContext):
        pass

    # Exit a parse tree produced by GtdParser#importDeclaration.
    def exitImportDeclaration(self, ctx:GtdParser.ImportDeclarationContext):
        pass


    # Enter a parse tree produced by GtdParser#namespaceDeclaration.
    def enterNamespaceDeclaration(self, ctx:GtdParser.NamespaceDeclarationContext):
        pass

    # Exit a parse tree produced by GtdParser#namespaceDeclaration.
    def exitNamespaceDeclaration(self, ctx:GtdParser.NamespaceDeclarationContext):
        pass


    # Enter a parse tree produced by GtdParser#useDeclaration.
    def enterUseDeclaration(self, ctx:GtdParser.UseDeclarationContext):
        pass

    # Exit a parse tree produced by GtdParser#useDeclaration.
    def exitUseDeclaration(self, ctx:GtdParser.UseDeclarationContext):
        pass


    # Enter a parse tree produced by GtdParser#declaration.
    def enterDeclaration(self, ctx:GtdParser.DeclarationContext):
        pass

    # Exit a parse tree produced by GtdParser#declaration.
    def exitDeclaration(self, ctx:GtdParser.DeclarationContext):
        pass


    # Enter a parse tree produced by GtdParser#typedefDeclaration.
    def enterTypedefDeclaration(self, ctx:GtdParser.TypedefDeclarationContext):
        pass

    # Exit a parse tree produced by GtdParser#typedefDeclaration.
    def exitTypedefDeclaration(self, ctx:GtdParser.TypedefDeclarationContext):
        pass


    # Enter a parse tree produced by GtdParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:GtdParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by GtdParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:GtdParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by GtdParser#flagDeclaration.
    def enterFlagDeclaration(self, ctx:GtdParser.FlagDeclarationContext):
        pass

    # Exit a parse tree produced by GtdParser#flagDeclaration.
    def exitFlagDeclaration(self, ctx:GtdParser.FlagDeclarationContext):
        pass


    # Enter a parse tree produced by GtdParser#enumMemberList.
    def enterEnumMemberList(self, ctx:GtdParser.EnumMemberListContext):
        pass

    # Exit a parse tree produced by GtdParser#enumMemberList.
    def exitEnumMemberList(self, ctx:GtdParser.EnumMemberListContext):
        pass


    # Enter a parse tree produced by GtdParser#enumMember.
    def enterEnumMember(self, ctx:GtdParser.EnumMemberContext):
        pass

    # Exit a parse tree produced by GtdParser#enumMember.
    def exitEnumMember(self, ctx:GtdParser.EnumMemberContext):
        pass


    # Enter a parse tree produced by GtdParser#flagMemberList.
    def enterFlagMemberList(self, ctx:GtdParser.FlagMemberListContext):
        pass

    # Exit a parse tree produced by GtdParser#flagMemberList.
    def exitFlagMemberList(self, ctx:GtdParser.FlagMemberListContext):
        pass


    # Enter a parse tree produced by GtdParser#flagMember.
    def enterFlagMember(self, ctx:GtdParser.FlagMemberContext):
        pass

    # Exit a parse tree produced by GtdParser#flagMember.
    def exitFlagMember(self, ctx:GtdParser.FlagMemberContext):
        pass


    # Enter a parse tree produced by GtdParser#structureDeclaration.
    def enterStructureDeclaration(self, ctx:GtdParser.StructureDeclarationContext):
        pass

    # Exit a parse tree produced by GtdParser#structureDeclaration.
    def exitStructureDeclaration(self, ctx:GtdParser.StructureDeclarationContext):
        pass


    # Enter a parse tree produced by GtdParser#structureMemberList.
    def enterStructureMemberList(self, ctx:GtdParser.StructureMemberListContext):
        pass

    # Exit a parse tree produced by GtdParser#structureMemberList.
    def exitStructureMemberList(self, ctx:GtdParser.StructureMemberListContext):
        pass


    # Enter a parse tree produced by GtdParser#structureMember.
    def enterStructureMember(self, ctx:GtdParser.StructureMemberContext):
        pass

    # Exit a parse tree produced by GtdParser#structureMember.
    def exitStructureMember(self, ctx:GtdParser.StructureMemberContext):
        pass


    # Enter a parse tree produced by GtdParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:GtdParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by GtdParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:GtdParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by GtdParser#annotation.
    def enterAnnotation(self, ctx:GtdParser.AnnotationContext):
        pass

    # Exit a parse tree produced by GtdParser#annotation.
    def exitAnnotation(self, ctx:GtdParser.AnnotationContext):
        pass


    # Enter a parse tree produced by GtdParser#parameterList.
    def enterParameterList(self, ctx:GtdParser.ParameterListContext):
        pass

    # Exit a parse tree produced by GtdParser#parameterList.
    def exitParameterList(self, ctx:GtdParser.ParameterListContext):
        pass


    # Enter a parse tree produced by GtdParser#parameter.
    def enterParameter(self, ctx:GtdParser.ParameterContext):
        pass

    # Exit a parse tree produced by GtdParser#parameter.
    def exitParameter(self, ctx:GtdParser.ParameterContext):
        pass


    # Enter a parse tree produced by GtdParser#typeSpec.
    def enterTypeSpec(self, ctx:GtdParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by GtdParser#typeSpec.
    def exitTypeSpec(self, ctx:GtdParser.TypeSpecContext):
        pass


    # Enter a parse tree produced by GtdParser#typeReference.
    def enterTypeReference(self, ctx:GtdParser.TypeReferenceContext):
        pass

    # Exit a parse tree produced by GtdParser#typeReference.
    def exitTypeReference(self, ctx:GtdParser.TypeReferenceContext):
        pass


    # Enter a parse tree produced by GtdParser#signModifier.
    def enterSignModifier(self, ctx:GtdParser.SignModifierContext):
        pass

    # Exit a parse tree produced by GtdParser#signModifier.
    def exitSignModifier(self, ctx:GtdParser.SignModifierContext):
        pass


    # Enter a parse tree produced by GtdParser#primitiveType.
    def enterPrimitiveType(self, ctx:GtdParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by GtdParser#primitiveType.
    def exitPrimitiveType(self, ctx:GtdParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by GtdParser#pointerModifier.
    def enterPointerModifier(self, ctx:GtdParser.PointerModifierContext):
        pass

    # Exit a parse tree produced by GtdParser#pointerModifier.
    def exitPointerModifier(self, ctx:GtdParser.PointerModifierContext):
        pass


    # Enter a parse tree produced by GtdParser#qualifiedName.
    def enterQualifiedName(self, ctx:GtdParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by GtdParser#qualifiedName.
    def exitQualifiedName(self, ctx:GtdParser.QualifiedNameContext):
        pass



del GtdParser
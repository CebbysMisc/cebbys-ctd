# Generated from resources/grammar/Gtd.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GtdParser import GtdParser
else:
    from GtdParser import GtdParser

# This class defines a complete generic visitor for a parse tree produced by GtdParser.

class GtdVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GtdParser#compilationUnit.
    def visitCompilationUnit(self, ctx:GtdParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#importDeclaration.
    def visitImportDeclaration(self, ctx:GtdParser.ImportDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#namespaceDeclaration.
    def visitNamespaceDeclaration(self, ctx:GtdParser.NamespaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#useDeclaration.
    def visitUseDeclaration(self, ctx:GtdParser.UseDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#declaration.
    def visitDeclaration(self, ctx:GtdParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#typedefDeclaration.
    def visitTypedefDeclaration(self, ctx:GtdParser.TypedefDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#enumDeclaration.
    def visitEnumDeclaration(self, ctx:GtdParser.EnumDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#flagDeclaration.
    def visitFlagDeclaration(self, ctx:GtdParser.FlagDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#enumMemberList.
    def visitEnumMemberList(self, ctx:GtdParser.EnumMemberListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#enumMember.
    def visitEnumMember(self, ctx:GtdParser.EnumMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#flagMemberList.
    def visitFlagMemberList(self, ctx:GtdParser.FlagMemberListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#flagMember.
    def visitFlagMember(self, ctx:GtdParser.FlagMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#structureDeclaration.
    def visitStructureDeclaration(self, ctx:GtdParser.StructureDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#structureMemberList.
    def visitStructureMemberList(self, ctx:GtdParser.StructureMemberListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#structureMember.
    def visitStructureMember(self, ctx:GtdParser.StructureMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:GtdParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#annotation.
    def visitAnnotation(self, ctx:GtdParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#parameterList.
    def visitParameterList(self, ctx:GtdParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#parameter.
    def visitParameter(self, ctx:GtdParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#typeSpec.
    def visitTypeSpec(self, ctx:GtdParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#typeReference.
    def visitTypeReference(self, ctx:GtdParser.TypeReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#signModifier.
    def visitSignModifier(self, ctx:GtdParser.SignModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#primitiveType.
    def visitPrimitiveType(self, ctx:GtdParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#pointerModifier.
    def visitPointerModifier(self, ctx:GtdParser.PointerModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GtdParser#qualifiedName.
    def visitQualifiedName(self, ctx:GtdParser.QualifiedNameContext):
        return self.visitChildren(ctx)



del GtdParser
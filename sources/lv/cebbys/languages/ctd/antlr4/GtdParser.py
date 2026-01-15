# Generated from resources/grammar/Gtd.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,106,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,39,8,1,10,1,
        12,1,42,9,1,1,1,1,1,1,2,1,2,3,2,48,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,3,4,58,8,4,1,4,1,4,3,4,62,8,4,1,4,1,4,1,5,1,5,5,5,68,8,5,10,
        5,12,5,71,9,5,1,6,1,6,1,6,3,6,76,8,6,1,7,3,7,79,8,7,1,7,1,7,3,7,
        83,8,7,1,7,3,7,86,8,7,1,8,1,8,3,8,90,8,8,1,9,1,9,1,10,1,10,1,11,
        1,11,1,12,1,12,1,12,5,12,101,8,12,10,12,12,12,104,9,12,1,12,0,0,
        13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,2,1,0,8,9,1,0,10,14,104,0,
        29,1,0,0,0,2,34,1,0,0,0,4,47,1,0,0,0,6,49,1,0,0,0,8,53,1,0,0,0,10,
        65,1,0,0,0,12,72,1,0,0,0,14,85,1,0,0,0,16,87,1,0,0,0,18,91,1,0,0,
        0,20,93,1,0,0,0,22,95,1,0,0,0,24,97,1,0,0,0,26,28,3,2,1,0,27,26,
        1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,
        31,29,1,0,0,0,32,33,5,0,0,1,33,1,1,0,0,0,34,35,5,1,0,0,35,36,3,24,
        12,0,36,40,5,2,0,0,37,39,3,4,2,0,38,37,1,0,0,0,39,42,1,0,0,0,40,
        38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,40,1,0,0,0,43,44,5,3,0,
        0,44,3,1,0,0,0,45,48,3,6,3,0,46,48,3,8,4,0,47,45,1,0,0,0,47,46,1,
        0,0,0,48,5,1,0,0,0,49,50,5,4,0,0,50,51,3,14,7,0,51,52,5,17,0,0,52,
        7,1,0,0,0,53,54,5,5,0,0,54,57,5,17,0,0,55,56,5,6,0,0,56,58,3,14,
        7,0,57,55,1,0,0,0,57,58,1,0,0,0,58,59,1,0,0,0,59,61,5,2,0,0,60,62,
        3,10,5,0,61,60,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,64,5,3,0,0,
        64,9,1,0,0,0,65,69,3,12,6,0,66,68,3,12,6,0,67,66,1,0,0,0,68,71,1,
        0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,11,1,0,0,0,71,69,1,0,0,0,72,
        75,5,17,0,0,73,74,5,7,0,0,74,76,5,18,0,0,75,73,1,0,0,0,75,76,1,0,
        0,0,76,13,1,0,0,0,77,79,3,18,9,0,78,77,1,0,0,0,78,79,1,0,0,0,79,
        80,1,0,0,0,80,82,3,20,10,0,81,83,3,22,11,0,82,81,1,0,0,0,82,83,1,
        0,0,0,83,86,1,0,0,0,84,86,3,16,8,0,85,78,1,0,0,0,85,84,1,0,0,0,86,
        15,1,0,0,0,87,89,5,17,0,0,88,90,3,22,11,0,89,88,1,0,0,0,89,90,1,
        0,0,0,90,17,1,0,0,0,91,92,7,0,0,0,92,19,1,0,0,0,93,94,7,1,0,0,94,
        21,1,0,0,0,95,96,5,15,0,0,96,23,1,0,0,0,97,102,5,17,0,0,98,99,5,
        16,0,0,99,101,5,17,0,0,100,98,1,0,0,0,101,104,1,0,0,0,102,100,1,
        0,0,0,102,103,1,0,0,0,103,25,1,0,0,0,104,102,1,0,0,0,12,29,40,47,
        57,61,69,75,78,82,85,89,102
    ]

class GtdParser ( Parser ):

    grammarFileName = "Gtd.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'namespace'", "'{'", "'}'", "'typedef'", 
                     "'enum'", "':'", "'='", "'signed'", "'unsigned'", "'char'", 
                     "'short'", "'int'", "'long'", "'void'", "'*'", "'::'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENTIFIER", "INTEGER_LITERAL", "WHITESPACE", 
                      "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_compilationUnit = 0
    RULE_namespaceDeclaration = 1
    RULE_declaration = 2
    RULE_typedefDeclaration = 3
    RULE_enumDeclaration = 4
    RULE_enumMemberList = 5
    RULE_enumMember = 6
    RULE_typeSpec = 7
    RULE_typeReference = 8
    RULE_signModifier = 9
    RULE_primitiveType = 10
    RULE_pointerModifier = 11
    RULE_qualifiedName = 12

    ruleNames =  [ "compilationUnit", "namespaceDeclaration", "declaration", 
                   "typedefDeclaration", "enumDeclaration", "enumMemberList", 
                   "enumMember", "typeSpec", "typeReference", "signModifier", 
                   "primitiveType", "pointerModifier", "qualifiedName" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    IDENTIFIER=17
    INTEGER_LITERAL=18
    WHITESPACE=19
    LINE_COMMENT=20
    BLOCK_COMMENT=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GtdParser.EOF, 0)

        def namespaceDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.NamespaceDeclarationContext)
            else:
                return self.getTypedRuleContext(GtdParser.NamespaceDeclarationContext,i)


        def getRuleIndex(self):
            return GtdParser.RULE_compilationUnit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompilationUnit" ):
                return visitor.visitCompilationUnit(self)
            else:
                return visitor.visitChildren(self)




    def compilationUnit(self):

        localctx = GtdParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 26
                self.namespaceDeclaration()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(GtdParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamespaceDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualifiedName(self):
            return self.getTypedRuleContext(GtdParser.QualifiedNameContext,0)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(GtdParser.DeclarationContext,i)


        def getRuleIndex(self):
            return GtdParser.RULE_namespaceDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespaceDeclaration" ):
                return visitor.visitNamespaceDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def namespaceDeclaration(self):

        localctx = GtdParser.NamespaceDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_namespaceDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(GtdParser.T__0)
            self.state = 35
            self.qualifiedName()
            self.state = 36
            self.match(GtdParser.T__1)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 37
                self.declaration()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.match(GtdParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typedefDeclaration(self):
            return self.getTypedRuleContext(GtdParser.TypedefDeclarationContext,0)


        def enumDeclaration(self):
            return self.getTypedRuleContext(GtdParser.EnumDeclarationContext,0)


        def getRuleIndex(self):
            return GtdParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = GtdParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.typedefDeclaration()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.enumDeclaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedefDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpec(self):
            return self.getTypedRuleContext(GtdParser.TypeSpecContext,0)


        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GtdParser.RULE_typedefDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedefDeclaration" ):
                return visitor.visitTypedefDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def typedefDeclaration(self):

        localctx = GtdParser.TypedefDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_typedefDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(GtdParser.T__3)
            self.state = 50
            self.typeSpec()
            self.state = 51
            self.match(GtdParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def typeSpec(self):
            return self.getTypedRuleContext(GtdParser.TypeSpecContext,0)


        def enumMemberList(self):
            return self.getTypedRuleContext(GtdParser.EnumMemberListContext,0)


        def getRuleIndex(self):
            return GtdParser.RULE_enumDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumDeclaration" ):
                return visitor.visitEnumDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def enumDeclaration(self):

        localctx = GtdParser.EnumDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_enumDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(GtdParser.T__4)
            self.state = 54
            self.match(GtdParser.IDENTIFIER)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 55
                self.match(GtdParser.T__5)
                self.state = 56
                self.typeSpec()


            self.state = 59
            self.match(GtdParser.T__1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 60
                self.enumMemberList()


            self.state = 63
            self.match(GtdParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumMemberListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enumMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.EnumMemberContext)
            else:
                return self.getTypedRuleContext(GtdParser.EnumMemberContext,i)


        def getRuleIndex(self):
            return GtdParser.RULE_enumMemberList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumMemberList" ):
                return visitor.visitEnumMemberList(self)
            else:
                return visitor.visitChildren(self)




    def enumMemberList(self):

        localctx = GtdParser.EnumMemberListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_enumMemberList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.enumMember()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 66
                self.enumMember()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(GtdParser.INTEGER_LITERAL, 0)

        def getRuleIndex(self):
            return GtdParser.RULE_enumMember

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumMember" ):
                return visitor.visitEnumMember(self)
            else:
                return visitor.visitChildren(self)




    def enumMember(self):

        localctx = GtdParser.EnumMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_enumMember)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(GtdParser.IDENTIFIER)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 73
                self.match(GtdParser.T__6)
                self.state = 74
                self.match(GtdParser.INTEGER_LITERAL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(GtdParser.PrimitiveTypeContext,0)


        def signModifier(self):
            return self.getTypedRuleContext(GtdParser.SignModifierContext,0)


        def pointerModifier(self):
            return self.getTypedRuleContext(GtdParser.PointerModifierContext,0)


        def typeReference(self):
            return self.getTypedRuleContext(GtdParser.TypeReferenceContext,0)


        def getRuleIndex(self):
            return GtdParser.RULE_typeSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpec" ):
                return visitor.visitTypeSpec(self)
            else:
                return visitor.visitChildren(self)




    def typeSpec(self):

        localctx = GtdParser.TypeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11, 12, 13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8 or _la==9:
                    self.state = 77
                    self.signModifier()


                self.state = 80
                self.primitiveType()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 81
                    self.pointerModifier()


                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.typeReference()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def pointerModifier(self):
            return self.getTypedRuleContext(GtdParser.PointerModifierContext,0)


        def getRuleIndex(self):
            return GtdParser.RULE_typeReference

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeReference" ):
                return visitor.visitTypeReference(self)
            else:
                return visitor.visitChildren(self)




    def typeReference(self):

        localctx = GtdParser.TypeReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typeReference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(GtdParser.IDENTIFIER)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 88
                self.pointerModifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GtdParser.RULE_signModifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignModifier" ):
                return visitor.visitSignModifier(self)
            else:
                return visitor.visitChildren(self)




    def signModifier(self):

        localctx = GtdParser.SignModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_signModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GtdParser.RULE_primitiveType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = GtdParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GtdParser.RULE_pointerModifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointerModifier" ):
                return visitor.visitPointerModifier(self)
            else:
                return visitor.visitChildren(self)




    def pointerModifier(self):

        localctx = GtdParser.PointerModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_pointerModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(GtdParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifiedNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GtdParser.IDENTIFIER)
            else:
                return self.getToken(GtdParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return GtdParser.RULE_qualifiedName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualifiedName" ):
                return visitor.visitQualifiedName(self)
            else:
                return visitor.visitChildren(self)




    def qualifiedName(self):

        localctx = GtdParser.QualifiedNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_qualifiedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(GtdParser.IDENTIFIER)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 98
                self.match(GtdParser.T__15)
                self.state = 99
                self.match(GtdParser.IDENTIFIER)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






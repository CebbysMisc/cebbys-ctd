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
        4,1,31,221,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,1,0,1,1,1,1,1,1,
        1,2,1,2,1,2,1,2,5,2,72,8,2,10,2,12,2,75,9,2,1,2,5,2,78,8,2,10,2,
        12,2,81,9,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,93,8,4,1,
        5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,103,8,6,1,6,1,6,3,6,107,8,6,1,
        6,1,6,1,7,1,7,1,7,1,7,3,7,115,8,7,1,7,1,7,3,7,119,8,7,1,7,1,7,1,
        8,1,8,5,8,125,8,8,10,8,12,8,128,9,8,1,9,1,9,1,9,3,9,133,8,9,1,10,
        1,10,5,10,137,8,10,10,10,12,10,140,9,10,1,11,1,11,1,11,3,11,145,
        8,11,1,12,1,12,1,12,1,12,3,12,151,8,12,1,12,1,12,1,13,1,13,5,13,
        157,8,13,10,13,12,13,160,9,13,1,14,1,14,1,14,1,15,3,15,166,8,15,
        1,15,1,15,1,15,1,15,3,15,172,8,15,1,15,1,15,1,16,1,16,1,16,1,17,
        1,17,1,17,5,17,182,8,17,10,17,12,17,185,9,17,1,18,3,18,188,8,18,
        1,18,1,18,1,18,1,19,3,19,194,8,19,1,19,1,19,3,19,198,8,19,1,19,3,
        19,201,8,19,1,20,1,20,3,20,205,8,20,1,21,1,21,1,22,1,22,1,23,1,23,
        1,24,1,24,1,24,5,24,216,8,24,10,24,12,24,219,9,24,1,24,0,0,25,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,0,2,1,0,16,17,1,0,18,22,222,0,53,1,0,0,0,2,64,1,0,0,0,4,67,1,
        0,0,0,6,84,1,0,0,0,8,92,1,0,0,0,10,94,1,0,0,0,12,98,1,0,0,0,14,110,
        1,0,0,0,16,122,1,0,0,0,18,129,1,0,0,0,20,134,1,0,0,0,22,141,1,0,
        0,0,24,146,1,0,0,0,26,154,1,0,0,0,28,161,1,0,0,0,30,165,1,0,0,0,
        32,175,1,0,0,0,34,178,1,0,0,0,36,187,1,0,0,0,38,200,1,0,0,0,40,202,
        1,0,0,0,42,206,1,0,0,0,44,208,1,0,0,0,46,210,1,0,0,0,48,212,1,0,
        0,0,50,52,3,2,1,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,
        1,0,0,0,54,59,1,0,0,0,55,53,1,0,0,0,56,58,3,4,2,0,57,56,1,0,0,0,
        58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,
        0,0,0,62,63,5,0,0,1,63,1,1,0,0,0,64,65,5,1,0,0,65,66,5,28,0,0,66,
        3,1,0,0,0,67,68,5,2,0,0,68,69,3,48,24,0,69,73,5,3,0,0,70,72,3,6,
        3,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,79,
        1,0,0,0,75,73,1,0,0,0,76,78,3,8,4,0,77,76,1,0,0,0,78,81,1,0,0,0,
        79,77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,79,1,0,0,0,82,83,5,
        4,0,0,83,5,1,0,0,0,84,85,5,5,0,0,85,86,3,48,24,0,86,7,1,0,0,0,87,
        93,3,10,5,0,88,93,3,12,6,0,89,93,3,14,7,0,90,93,3,24,12,0,91,93,
        3,30,15,0,92,87,1,0,0,0,92,88,1,0,0,0,92,89,1,0,0,0,92,90,1,0,0,
        0,92,91,1,0,0,0,93,9,1,0,0,0,94,95,5,6,0,0,95,96,3,38,19,0,96,97,
        5,25,0,0,97,11,1,0,0,0,98,99,5,7,0,0,99,102,5,25,0,0,100,101,5,8,
        0,0,101,103,3,38,19,0,102,100,1,0,0,0,102,103,1,0,0,0,103,104,1,
        0,0,0,104,106,5,3,0,0,105,107,3,16,8,0,106,105,1,0,0,0,106,107,1,
        0,0,0,107,108,1,0,0,0,108,109,5,4,0,0,109,13,1,0,0,0,110,111,5,9,
        0,0,111,114,5,25,0,0,112,113,5,8,0,0,113,115,3,38,19,0,114,112,1,
        0,0,0,114,115,1,0,0,0,115,116,1,0,0,0,116,118,5,3,0,0,117,119,3,
        20,10,0,118,117,1,0,0,0,118,119,1,0,0,0,119,120,1,0,0,0,120,121,
        5,4,0,0,121,15,1,0,0,0,122,126,3,18,9,0,123,125,3,18,9,0,124,123,
        1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,17,1,
        0,0,0,128,126,1,0,0,0,129,132,5,25,0,0,130,131,5,10,0,0,131,133,
        5,26,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,19,1,0,0,0,134,138,
        3,22,11,0,135,137,3,22,11,0,136,135,1,0,0,0,137,140,1,0,0,0,138,
        136,1,0,0,0,138,139,1,0,0,0,139,21,1,0,0,0,140,138,1,0,0,0,141,144,
        5,25,0,0,142,143,5,10,0,0,143,145,5,27,0,0,144,142,1,0,0,0,144,145,
        1,0,0,0,145,23,1,0,0,0,146,147,5,11,0,0,147,148,5,25,0,0,148,150,
        5,3,0,0,149,151,3,26,13,0,150,149,1,0,0,0,150,151,1,0,0,0,151,152,
        1,0,0,0,152,153,5,4,0,0,153,25,1,0,0,0,154,158,3,28,14,0,155,157,
        3,28,14,0,156,155,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,
        1,0,0,0,159,27,1,0,0,0,160,158,1,0,0,0,161,162,3,38,19,0,162,163,
        5,25,0,0,163,29,1,0,0,0,164,166,3,32,16,0,165,164,1,0,0,0,165,166,
        1,0,0,0,166,167,1,0,0,0,167,168,3,38,19,0,168,169,5,25,0,0,169,171,
        5,12,0,0,170,172,3,34,17,0,171,170,1,0,0,0,171,172,1,0,0,0,172,173,
        1,0,0,0,173,174,5,13,0,0,174,31,1,0,0,0,175,176,5,14,0,0,176,177,
        5,25,0,0,177,33,1,0,0,0,178,183,3,36,18,0,179,180,5,15,0,0,180,182,
        3,36,18,0,181,179,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,
        1,0,0,0,184,35,1,0,0,0,185,183,1,0,0,0,186,188,3,32,16,0,187,186,
        1,0,0,0,187,188,1,0,0,0,188,189,1,0,0,0,189,190,3,38,19,0,190,191,
        5,25,0,0,191,37,1,0,0,0,192,194,3,42,21,0,193,192,1,0,0,0,193,194,
        1,0,0,0,194,195,1,0,0,0,195,197,3,44,22,0,196,198,3,46,23,0,197,
        196,1,0,0,0,197,198,1,0,0,0,198,201,1,0,0,0,199,201,3,40,20,0,200,
        193,1,0,0,0,200,199,1,0,0,0,201,39,1,0,0,0,202,204,5,25,0,0,203,
        205,3,46,23,0,204,203,1,0,0,0,204,205,1,0,0,0,205,41,1,0,0,0,206,
        207,7,0,0,0,207,43,1,0,0,0,208,209,7,1,0,0,209,45,1,0,0,0,210,211,
        5,23,0,0,211,47,1,0,0,0,212,217,5,25,0,0,213,214,5,24,0,0,214,216,
        5,25,0,0,215,213,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,218,
        1,0,0,0,218,49,1,0,0,0,219,217,1,0,0,0,24,53,59,73,79,92,102,106,
        114,118,126,132,138,144,150,158,165,171,183,187,193,197,200,204,
        217
    ]

class GtdParser ( Parser ):

    grammarFileName = "Gtd.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'import'", "'namespace'", "'{'", "'}'", 
                     "'use'", "'typedef'", "'enum'", "':'", "'flag'", "'='", 
                     "'structure'", "'('", "')'", "'@'", "','", "'signed'", 
                     "'unsigned'", "'char'", "'short'", "'int'", "'long'", 
                     "'void'", "'*'", "'::'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENTIFIER", "INTEGER_LITERAL", "HEX_LITERAL", 
                      "STRING_LITERAL", "WHITESPACE", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_compilationUnit = 0
    RULE_importDeclaration = 1
    RULE_namespaceDeclaration = 2
    RULE_useDeclaration = 3
    RULE_declaration = 4
    RULE_typedefDeclaration = 5
    RULE_enumDeclaration = 6
    RULE_flagDeclaration = 7
    RULE_enumMemberList = 8
    RULE_enumMember = 9
    RULE_flagMemberList = 10
    RULE_flagMember = 11
    RULE_structureDeclaration = 12
    RULE_structureMemberList = 13
    RULE_structureMember = 14
    RULE_functionDeclaration = 15
    RULE_annotation = 16
    RULE_parameterList = 17
    RULE_parameter = 18
    RULE_typeSpec = 19
    RULE_typeReference = 20
    RULE_signModifier = 21
    RULE_primitiveType = 22
    RULE_pointerModifier = 23
    RULE_qualifiedName = 24

    ruleNames =  [ "compilationUnit", "importDeclaration", "namespaceDeclaration", 
                   "useDeclaration", "declaration", "typedefDeclaration", 
                   "enumDeclaration", "flagDeclaration", "enumMemberList", 
                   "enumMember", "flagMemberList", "flagMember", "structureDeclaration", 
                   "structureMemberList", "structureMember", "functionDeclaration", 
                   "annotation", "parameterList", "parameter", "typeSpec", 
                   "typeReference", "signModifier", "primitiveType", "pointerModifier", 
                   "qualifiedName" ]

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
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    IDENTIFIER=25
    INTEGER_LITERAL=26
    HEX_LITERAL=27
    STRING_LITERAL=28
    WHITESPACE=29
    LINE_COMMENT=30
    BLOCK_COMMENT=31

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

        def importDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.ImportDeclarationContext)
            else:
                return self.getTypedRuleContext(GtdParser.ImportDeclarationContext,i)


        def namespaceDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.NamespaceDeclarationContext)
            else:
                return self.getTypedRuleContext(GtdParser.NamespaceDeclarationContext,i)


        def getRuleIndex(self):
            return GtdParser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)

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
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 50
                self.importDeclaration()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 56
                self.namespaceDeclaration()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(GtdParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(GtdParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return GtdParser.RULE_importDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportDeclaration" ):
                listener.enterImportDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportDeclaration" ):
                listener.exitImportDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportDeclaration" ):
                return visitor.visitImportDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def importDeclaration(self):

        localctx = GtdParser.ImportDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_importDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(GtdParser.T__0)
            self.state = 65
            self.match(GtdParser.STRING_LITERAL)
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


        def useDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.UseDeclarationContext)
            else:
                return self.getTypedRuleContext(GtdParser.UseDeclarationContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(GtdParser.DeclarationContext,i)


        def getRuleIndex(self):
            return GtdParser.RULE_namespaceDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespaceDeclaration" ):
                listener.enterNamespaceDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespaceDeclaration" ):
                listener.exitNamespaceDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespaceDeclaration" ):
                return visitor.visitNamespaceDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def namespaceDeclaration(self):

        localctx = GtdParser.NamespaceDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_namespaceDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(GtdParser.T__1)
            self.state = 68
            self.qualifiedName()
            self.state = 69
            self.match(GtdParser.T__2)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 70
                self.useDeclaration()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 41896640) != 0):
                self.state = 76
                self.declaration()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self.match(GtdParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualifiedName(self):
            return self.getTypedRuleContext(GtdParser.QualifiedNameContext,0)


        def getRuleIndex(self):
            return GtdParser.RULE_useDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUseDeclaration" ):
                listener.enterUseDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUseDeclaration" ):
                listener.exitUseDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUseDeclaration" ):
                return visitor.visitUseDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def useDeclaration(self):

        localctx = GtdParser.UseDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_useDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(GtdParser.T__4)
            self.state = 85
            self.qualifiedName()
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


        def flagDeclaration(self):
            return self.getTypedRuleContext(GtdParser.FlagDeclarationContext,0)


        def structureDeclaration(self):
            return self.getTypedRuleContext(GtdParser.StructureDeclarationContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(GtdParser.FunctionDeclarationContext,0)


        def getRuleIndex(self):
            return GtdParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = GtdParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaration)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.typedefDeclaration()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.enumDeclaration()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.flagDeclaration()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.structureDeclaration()
                pass
            elif token in [14, 16, 17, 18, 19, 20, 21, 22, 25]:
                self.enterOuterAlt(localctx, 5)
                self.state = 91
                self.functionDeclaration()
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedefDeclaration" ):
                listener.enterTypedefDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedefDeclaration" ):
                listener.exitTypedefDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedefDeclaration" ):
                return visitor.visitTypedefDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def typedefDeclaration(self):

        localctx = GtdParser.TypedefDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typedefDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(GtdParser.T__5)
            self.state = 95
            self.typeSpec()
            self.state = 96
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumDeclaration" ):
                listener.enterEnumDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumDeclaration" ):
                listener.exitEnumDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumDeclaration" ):
                return visitor.visitEnumDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def enumDeclaration(self):

        localctx = GtdParser.EnumDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_enumDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(GtdParser.T__6)
            self.state = 99
            self.match(GtdParser.IDENTIFIER)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 100
                self.match(GtdParser.T__7)
                self.state = 101
                self.typeSpec()


            self.state = 104
            self.match(GtdParser.T__2)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 105
                self.enumMemberList()


            self.state = 108
            self.match(GtdParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def typeSpec(self):
            return self.getTypedRuleContext(GtdParser.TypeSpecContext,0)


        def flagMemberList(self):
            return self.getTypedRuleContext(GtdParser.FlagMemberListContext,0)


        def getRuleIndex(self):
            return GtdParser.RULE_flagDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlagDeclaration" ):
                listener.enterFlagDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlagDeclaration" ):
                listener.exitFlagDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlagDeclaration" ):
                return visitor.visitFlagDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def flagDeclaration(self):

        localctx = GtdParser.FlagDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_flagDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(GtdParser.T__8)
            self.state = 111
            self.match(GtdParser.IDENTIFIER)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 112
                self.match(GtdParser.T__7)
                self.state = 113
                self.typeSpec()


            self.state = 116
            self.match(GtdParser.T__2)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 117
                self.flagMemberList()


            self.state = 120
            self.match(GtdParser.T__3)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumMemberList" ):
                listener.enterEnumMemberList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumMemberList" ):
                listener.exitEnumMemberList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumMemberList" ):
                return visitor.visitEnumMemberList(self)
            else:
                return visitor.visitChildren(self)




    def enumMemberList(self):

        localctx = GtdParser.EnumMemberListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_enumMemberList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.enumMember()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 123
                self.enumMember()
                self.state = 128
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumMember" ):
                listener.enterEnumMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumMember" ):
                listener.exitEnumMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumMember" ):
                return visitor.visitEnumMember(self)
            else:
                return visitor.visitChildren(self)




    def enumMember(self):

        localctx = GtdParser.EnumMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_enumMember)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(GtdParser.IDENTIFIER)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 130
                self.match(GtdParser.T__9)
                self.state = 131
                self.match(GtdParser.INTEGER_LITERAL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagMemberListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def flagMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.FlagMemberContext)
            else:
                return self.getTypedRuleContext(GtdParser.FlagMemberContext,i)


        def getRuleIndex(self):
            return GtdParser.RULE_flagMemberList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlagMemberList" ):
                listener.enterFlagMemberList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlagMemberList" ):
                listener.exitFlagMemberList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlagMemberList" ):
                return visitor.visitFlagMemberList(self)
            else:
                return visitor.visitChildren(self)




    def flagMemberList(self):

        localctx = GtdParser.FlagMemberListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_flagMemberList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.flagMember()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 135
                self.flagMember()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def HEX_LITERAL(self):
            return self.getToken(GtdParser.HEX_LITERAL, 0)

        def getRuleIndex(self):
            return GtdParser.RULE_flagMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlagMember" ):
                listener.enterFlagMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlagMember" ):
                listener.exitFlagMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlagMember" ):
                return visitor.visitFlagMember(self)
            else:
                return visitor.visitChildren(self)




    def flagMember(self):

        localctx = GtdParser.FlagMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_flagMember)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(GtdParser.IDENTIFIER)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 142
                self.match(GtdParser.T__9)
                self.state = 143
                self.match(GtdParser.HEX_LITERAL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructureDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def structureMemberList(self):
            return self.getTypedRuleContext(GtdParser.StructureMemberListContext,0)


        def getRuleIndex(self):
            return GtdParser.RULE_structureDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructureDeclaration" ):
                listener.enterStructureDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructureDeclaration" ):
                listener.exitStructureDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructureDeclaration" ):
                return visitor.visitStructureDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def structureDeclaration(self):

        localctx = GtdParser.StructureDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_structureDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(GtdParser.T__10)
            self.state = 147
            self.match(GtdParser.IDENTIFIER)
            self.state = 148
            self.match(GtdParser.T__2)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 41877504) != 0):
                self.state = 149
                self.structureMemberList()


            self.state = 152
            self.match(GtdParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructureMemberListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structureMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.StructureMemberContext)
            else:
                return self.getTypedRuleContext(GtdParser.StructureMemberContext,i)


        def getRuleIndex(self):
            return GtdParser.RULE_structureMemberList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructureMemberList" ):
                listener.enterStructureMemberList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructureMemberList" ):
                listener.exitStructureMemberList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructureMemberList" ):
                return visitor.visitStructureMemberList(self)
            else:
                return visitor.visitChildren(self)




    def structureMemberList(self):

        localctx = GtdParser.StructureMemberListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_structureMemberList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.structureMember()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 41877504) != 0):
                self.state = 155
                self.structureMember()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructureMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpec(self):
            return self.getTypedRuleContext(GtdParser.TypeSpecContext,0)


        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GtdParser.RULE_structureMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructureMember" ):
                listener.enterStructureMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructureMember" ):
                listener.exitStructureMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructureMember" ):
                return visitor.visitStructureMember(self)
            else:
                return visitor.visitChildren(self)




    def structureMember(self):

        localctx = GtdParser.StructureMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_structureMember)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.typeSpec()
            self.state = 162
            self.match(GtdParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpec(self):
            return self.getTypedRuleContext(GtdParser.TypeSpecContext,0)


        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def annotation(self):
            return self.getTypedRuleContext(GtdParser.AnnotationContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(GtdParser.ParameterListContext,0)


        def getRuleIndex(self):
            return GtdParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = GtdParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 164
                self.annotation()


            self.state = 167
            self.typeSpec()
            self.state = 168
            self.match(GtdParser.IDENTIFIER)
            self.state = 169
            self.match(GtdParser.T__11)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 41893888) != 0):
                self.state = 170
                self.parameterList()


            self.state = 173
            self.match(GtdParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GtdParser.RULE_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotation" ):
                listener.enterAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotation" ):
                listener.exitAnnotation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnnotation" ):
                return visitor.visitAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def annotation(self):

        localctx = GtdParser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_annotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(GtdParser.T__13)
            self.state = 176
            self.match(GtdParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.ParameterContext)
            else:
                return self.getTypedRuleContext(GtdParser.ParameterContext,i)


        def getRuleIndex(self):
            return GtdParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = GtdParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.parameter()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 179
                self.match(GtdParser.T__14)
                self.state = 180
                self.parameter()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpec(self):
            return self.getTypedRuleContext(GtdParser.TypeSpecContext,0)


        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def annotation(self):
            return self.getTypedRuleContext(GtdParser.AnnotationContext,0)


        def getRuleIndex(self):
            return GtdParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = GtdParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 186
                self.annotation()


            self.state = 189
            self.typeSpec()
            self.state = 190
            self.match(GtdParser.IDENTIFIER)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpec" ):
                listener.enterTypeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpec" ):
                listener.exitTypeSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpec" ):
                return visitor.visitTypeSpec(self)
            else:
                return visitor.visitChildren(self)




    def typeSpec(self):

        localctx = GtdParser.TypeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 18, 19, 20, 21, 22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16 or _la==17:
                    self.state = 192
                    self.signModifier()


                self.state = 195
                self.primitiveType()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 196
                    self.pointerModifier()


                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeReference" ):
                listener.enterTypeReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeReference" ):
                listener.exitTypeReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeReference" ):
                return visitor.visitTypeReference(self)
            else:
                return visitor.visitChildren(self)




    def typeReference(self):

        localctx = GtdParser.TypeReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_typeReference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(GtdParser.IDENTIFIER)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 203
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignModifier" ):
                listener.enterSignModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignModifier" ):
                listener.exitSignModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignModifier" ):
                return visitor.visitSignModifier(self)
            else:
                return visitor.visitChildren(self)




    def signModifier(self):

        localctx = GtdParser.SignModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_signModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = GtdParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8126464) != 0)):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointerModifier" ):
                listener.enterPointerModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointerModifier" ):
                listener.exitPointerModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointerModifier" ):
                return visitor.visitPointerModifier(self)
            else:
                return visitor.visitChildren(self)




    def pointerModifier(self):

        localctx = GtdParser.PointerModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_pointerModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(GtdParser.T__22)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedName" ):
                listener.enterQualifiedName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedName" ):
                listener.exitQualifiedName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualifiedName" ):
                return visitor.visitQualifiedName(self)
            else:
                return visitor.visitChildren(self)




    def qualifiedName(self):

        localctx = GtdParser.QualifiedNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_qualifiedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(GtdParser.IDENTIFIER)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 213
                self.match(GtdParser.T__23)
                self.state = 214
                self.match(GtdParser.IDENTIFIER)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






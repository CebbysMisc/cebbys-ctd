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
        4,1,31,255,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,5,0,54,
        8,0,10,0,12,0,57,9,0,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,1,0,1,1,
        1,1,1,1,1,2,3,2,71,8,2,1,2,1,2,1,2,1,2,5,2,77,8,2,10,2,12,2,80,9,
        2,1,2,5,2,83,8,2,10,2,12,2,86,9,2,1,2,1,2,1,3,3,3,91,8,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,3,4,101,8,4,1,5,3,5,104,8,5,1,5,1,5,1,5,
        1,5,1,6,3,6,111,8,6,1,6,1,6,1,6,1,6,3,6,117,8,6,1,6,1,6,3,6,121,
        8,6,1,6,1,6,1,7,3,7,126,8,7,1,7,1,7,1,7,1,7,3,7,132,8,7,1,7,1,7,
        3,7,136,8,7,1,7,1,7,1,8,1,8,5,8,142,8,8,10,8,12,8,145,9,8,1,9,1,
        9,1,9,3,9,150,8,9,1,10,1,10,5,10,154,8,10,10,10,12,10,157,9,10,1,
        11,1,11,1,11,3,11,162,8,11,1,12,3,12,165,8,12,1,12,1,12,1,12,1,12,
        3,12,171,8,12,1,12,1,12,1,13,1,13,5,13,177,8,13,10,13,12,13,180,
        9,13,1,14,1,14,1,14,1,15,3,15,186,8,15,1,15,1,15,1,15,1,15,3,15,
        192,8,15,1,15,1,15,1,16,1,16,1,16,1,16,3,16,200,8,16,1,16,3,16,203,
        8,16,1,17,1,17,1,17,5,17,208,8,17,10,17,12,17,211,9,17,1,18,1,18,
        1,18,5,18,216,8,18,10,18,12,18,219,9,18,1,19,3,19,222,8,19,1,19,
        1,19,1,19,1,20,3,20,228,8,20,1,20,1,20,3,20,232,8,20,1,20,3,20,235,
        8,20,1,21,1,21,3,21,239,8,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,
        1,25,1,25,5,25,250,8,25,10,25,12,25,253,9,25,1,25,0,0,26,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        0,3,1,0,26,27,1,0,16,17,1,0,18,22,264,0,55,1,0,0,0,2,66,1,0,0,0,
        4,70,1,0,0,0,6,90,1,0,0,0,8,100,1,0,0,0,10,103,1,0,0,0,12,110,1,
        0,0,0,14,125,1,0,0,0,16,139,1,0,0,0,18,146,1,0,0,0,20,151,1,0,0,
        0,22,158,1,0,0,0,24,164,1,0,0,0,26,174,1,0,0,0,28,181,1,0,0,0,30,
        185,1,0,0,0,32,195,1,0,0,0,34,204,1,0,0,0,36,212,1,0,0,0,38,221,
        1,0,0,0,40,234,1,0,0,0,42,236,1,0,0,0,44,240,1,0,0,0,46,242,1,0,
        0,0,48,244,1,0,0,0,50,246,1,0,0,0,52,54,3,2,1,0,53,52,1,0,0,0,54,
        57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,61,1,0,0,0,57,55,1,0,0,
        0,58,60,3,4,2,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,
        1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,5,0,0,1,65,1,1,0,0,0,66,
        67,5,1,0,0,67,68,5,28,0,0,68,3,1,0,0,0,69,71,3,32,16,0,70,69,1,0,
        0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,73,5,2,0,0,73,74,3,50,25,0,74,
        78,5,3,0,0,75,77,3,6,3,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,
        0,78,79,1,0,0,0,79,84,1,0,0,0,80,78,1,0,0,0,81,83,3,8,4,0,82,81,
        1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,
        86,84,1,0,0,0,87,88,5,4,0,0,88,5,1,0,0,0,89,91,3,32,16,0,90,89,1,
        0,0,0,90,91,1,0,0,0,91,92,1,0,0,0,92,93,5,5,0,0,93,94,3,50,25,0,
        94,7,1,0,0,0,95,101,3,10,5,0,96,101,3,12,6,0,97,101,3,14,7,0,98,
        101,3,24,12,0,99,101,3,30,15,0,100,95,1,0,0,0,100,96,1,0,0,0,100,
        97,1,0,0,0,100,98,1,0,0,0,100,99,1,0,0,0,101,9,1,0,0,0,102,104,3,
        32,16,0,103,102,1,0,0,0,103,104,1,0,0,0,104,105,1,0,0,0,105,106,
        5,6,0,0,106,107,3,40,20,0,107,108,5,25,0,0,108,11,1,0,0,0,109,111,
        3,32,16,0,110,109,1,0,0,0,110,111,1,0,0,0,111,112,1,0,0,0,112,113,
        5,7,0,0,113,116,5,25,0,0,114,115,5,8,0,0,115,117,3,40,20,0,116,114,
        1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,120,5,3,0,0,119,121,
        3,16,8,0,120,119,1,0,0,0,120,121,1,0,0,0,121,122,1,0,0,0,122,123,
        5,4,0,0,123,13,1,0,0,0,124,126,3,32,16,0,125,124,1,0,0,0,125,126,
        1,0,0,0,126,127,1,0,0,0,127,128,5,9,0,0,128,131,5,25,0,0,129,130,
        5,8,0,0,130,132,3,40,20,0,131,129,1,0,0,0,131,132,1,0,0,0,132,133,
        1,0,0,0,133,135,5,3,0,0,134,136,3,20,10,0,135,134,1,0,0,0,135,136,
        1,0,0,0,136,137,1,0,0,0,137,138,5,4,0,0,138,15,1,0,0,0,139,143,3,
        18,9,0,140,142,3,18,9,0,141,140,1,0,0,0,142,145,1,0,0,0,143,141,
        1,0,0,0,143,144,1,0,0,0,144,17,1,0,0,0,145,143,1,0,0,0,146,149,5,
        25,0,0,147,148,5,10,0,0,148,150,7,0,0,0,149,147,1,0,0,0,149,150,
        1,0,0,0,150,19,1,0,0,0,151,155,3,22,11,0,152,154,3,22,11,0,153,152,
        1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,21,1,
        0,0,0,157,155,1,0,0,0,158,161,5,25,0,0,159,160,5,10,0,0,160,162,
        5,27,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,23,1,0,0,0,163,165,
        3,32,16,0,164,163,1,0,0,0,164,165,1,0,0,0,165,166,1,0,0,0,166,167,
        5,11,0,0,167,168,5,25,0,0,168,170,5,3,0,0,169,171,3,26,13,0,170,
        169,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,173,5,4,0,0,173,
        25,1,0,0,0,174,178,3,28,14,0,175,177,3,28,14,0,176,175,1,0,0,0,177,
        180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,27,1,0,0,0,180,178,
        1,0,0,0,181,182,3,40,20,0,182,183,5,25,0,0,183,29,1,0,0,0,184,186,
        3,32,16,0,185,184,1,0,0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,188,
        3,40,20,0,188,189,5,25,0,0,189,191,5,12,0,0,190,192,3,36,18,0,191,
        190,1,0,0,0,191,192,1,0,0,0,192,193,1,0,0,0,193,194,5,13,0,0,194,
        31,1,0,0,0,195,196,5,14,0,0,196,202,5,25,0,0,197,199,5,12,0,0,198,
        200,3,34,17,0,199,198,1,0,0,0,199,200,1,0,0,0,200,201,1,0,0,0,201,
        203,5,13,0,0,202,197,1,0,0,0,202,203,1,0,0,0,203,33,1,0,0,0,204,
        209,5,28,0,0,205,206,5,15,0,0,206,208,5,28,0,0,207,205,1,0,0,0,208,
        211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,35,1,0,0,0,211,209,
        1,0,0,0,212,217,3,38,19,0,213,214,5,15,0,0,214,216,3,38,19,0,215,
        213,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,0,218,
        37,1,0,0,0,219,217,1,0,0,0,220,222,3,32,16,0,221,220,1,0,0,0,221,
        222,1,0,0,0,222,223,1,0,0,0,223,224,3,40,20,0,224,225,5,25,0,0,225,
        39,1,0,0,0,226,228,3,44,22,0,227,226,1,0,0,0,227,228,1,0,0,0,228,
        229,1,0,0,0,229,231,3,46,23,0,230,232,3,48,24,0,231,230,1,0,0,0,
        231,232,1,0,0,0,232,235,1,0,0,0,233,235,3,42,21,0,234,227,1,0,0,
        0,234,233,1,0,0,0,235,41,1,0,0,0,236,238,3,50,25,0,237,239,3,48,
        24,0,238,237,1,0,0,0,238,239,1,0,0,0,239,43,1,0,0,0,240,241,7,1,
        0,0,241,45,1,0,0,0,242,243,7,2,0,0,243,47,1,0,0,0,244,245,5,23,0,
        0,245,49,1,0,0,0,246,251,5,25,0,0,247,248,5,24,0,0,248,250,5,25,
        0,0,249,247,1,0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,251,252,1,0,
        0,0,252,51,1,0,0,0,253,251,1,0,0,0,33,55,61,70,78,84,90,100,103,
        110,116,120,125,131,135,143,149,155,161,164,170,178,185,191,199,
        202,209,217,221,227,231,234,238,251
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
    RULE_annotationArguments = 17
    RULE_parameterList = 18
    RULE_parameter = 19
    RULE_typeSpec = 20
    RULE_typeReference = 21
    RULE_signModifier = 22
    RULE_primitiveType = 23
    RULE_pointerModifier = 24
    RULE_qualifiedName = 25

    ruleNames =  [ "compilationUnit", "importDeclaration", "namespaceDeclaration", 
                   "useDeclaration", "declaration", "typedefDeclaration", 
                   "enumDeclaration", "flagDeclaration", "enumMemberList", 
                   "enumMember", "flagMemberList", "flagMember", "structureDeclaration", 
                   "structureMemberList", "structureMember", "functionDeclaration", 
                   "annotation", "annotationArguments", "parameterList", 
                   "parameter", "typeSpec", "typeReference", "signModifier", 
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
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 52
                self.importDeclaration()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==14:
                self.state = 58
                self.namespaceDeclaration()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
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
            self.state = 66
            self.match(GtdParser.T__0)
            self.state = 67
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


        def annotation(self):
            return self.getTypedRuleContext(GtdParser.AnnotationContext,0)


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
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 69
                self.annotation()


            self.state = 72
            self.match(GtdParser.T__1)
            self.state = 73
            self.qualifiedName()
            self.state = 74
            self.match(GtdParser.T__2)
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 75
                    self.useDeclaration() 
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 41896640) != 0):
                self.state = 81
                self.declaration()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
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


        def annotation(self):
            return self.getTypedRuleContext(GtdParser.AnnotationContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 89
                self.annotation()


            self.state = 92
            self.match(GtdParser.T__4)
            self.state = 93
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
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.typedefDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.enumDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.flagDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.structureDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 99
                self.functionDeclaration()
                pass


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

        def annotation(self):
            return self.getTypedRuleContext(GtdParser.AnnotationContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 102
                self.annotation()


            self.state = 105
            self.match(GtdParser.T__5)
            self.state = 106
            self.typeSpec()
            self.state = 107
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

        def annotation(self):
            return self.getTypedRuleContext(GtdParser.AnnotationContext,0)


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
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 109
                self.annotation()


            self.state = 112
            self.match(GtdParser.T__6)
            self.state = 113
            self.match(GtdParser.IDENTIFIER)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 114
                self.match(GtdParser.T__7)
                self.state = 115
                self.typeSpec()


            self.state = 118
            self.match(GtdParser.T__2)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 119
                self.enumMemberList()


            self.state = 122
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

        def annotation(self):
            return self.getTypedRuleContext(GtdParser.AnnotationContext,0)


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
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 124
                self.annotation()


            self.state = 127
            self.match(GtdParser.T__8)
            self.state = 128
            self.match(GtdParser.IDENTIFIER)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 129
                self.match(GtdParser.T__7)
                self.state = 130
                self.typeSpec()


            self.state = 133
            self.match(GtdParser.T__2)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 134
                self.flagMemberList()


            self.state = 137
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
            self.state = 139
            self.enumMember()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 140
                self.enumMember()
                self.state = 145
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

        def HEX_LITERAL(self):
            return self.getToken(GtdParser.HEX_LITERAL, 0)

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
            self.state = 146
            self.match(GtdParser.IDENTIFIER)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 147
                self.match(GtdParser.T__9)
                self.state = 148
                _la = self._input.LA(1)
                if not(_la==26 or _la==27):
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
            self.state = 151
            self.flagMember()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 152
                self.flagMember()
                self.state = 157
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
            self.state = 158
            self.match(GtdParser.IDENTIFIER)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 159
                self.match(GtdParser.T__9)
                self.state = 160
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

        def annotation(self):
            return self.getTypedRuleContext(GtdParser.AnnotationContext,0)


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
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 163
                self.annotation()


            self.state = 166
            self.match(GtdParser.T__10)
            self.state = 167
            self.match(GtdParser.IDENTIFIER)
            self.state = 168
            self.match(GtdParser.T__2)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 41877504) != 0):
                self.state = 169
                self.structureMemberList()


            self.state = 172
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
            self.state = 174
            self.structureMember()
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 41877504) != 0):
                self.state = 175
                self.structureMember()
                self.state = 180
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
            self.state = 181
            self.typeSpec()
            self.state = 182
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
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 184
                self.annotation()


            self.state = 187
            self.typeSpec()
            self.state = 188
            self.match(GtdParser.IDENTIFIER)
            self.state = 189
            self.match(GtdParser.T__11)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 41893888) != 0):
                self.state = 190
                self.parameterList()


            self.state = 193
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

        def annotationArguments(self):
            return self.getTypedRuleContext(GtdParser.AnnotationArgumentsContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(GtdParser.T__13)
            self.state = 196
            self.match(GtdParser.IDENTIFIER)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 197
                self.match(GtdParser.T__11)
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 198
                    self.annotationArguments()


                self.state = 201
                self.match(GtdParser.T__12)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(GtdParser.STRING_LITERAL)
            else:
                return self.getToken(GtdParser.STRING_LITERAL, i)

        def getRuleIndex(self):
            return GtdParser.RULE_annotationArguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationArguments" ):
                listener.enterAnnotationArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationArguments" ):
                listener.exitAnnotationArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnnotationArguments" ):
                return visitor.visitAnnotationArguments(self)
            else:
                return visitor.visitChildren(self)




    def annotationArguments(self):

        localctx = GtdParser.AnnotationArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_annotationArguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(GtdParser.STRING_LITERAL)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 205
                self.match(GtdParser.T__14)
                self.state = 206
                self.match(GtdParser.STRING_LITERAL)
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 36, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.parameter()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 213
                self.match(GtdParser.T__14)
                self.state = 214
                self.parameter()
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
        self.enterRule(localctx, 38, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 220
                self.annotation()


            self.state = 223
            self.typeSpec()
            self.state = 224
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
        self.enterRule(localctx, 40, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 18, 19, 20, 21, 22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16 or _la==17:
                    self.state = 226
                    self.signModifier()


                self.state = 229
                self.primitiveType()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 230
                    self.pointerModifier()


                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
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

        def qualifiedName(self):
            return self.getTypedRuleContext(GtdParser.QualifiedNameContext,0)


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
        self.enterRule(localctx, 42, self.RULE_typeReference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.qualifiedName()
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 237
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
        self.enterRule(localctx, 44, self.RULE_signModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
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
        self.enterRule(localctx, 46, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
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
        self.enterRule(localctx, 48, self.RULE_pointerModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
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
        self.enterRule(localctx, 50, self.RULE_qualifiedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(GtdParser.IDENTIFIER)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 247
                self.match(GtdParser.T__23)
                self.state = 248
                self.match(GtdParser.IDENTIFIER)
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






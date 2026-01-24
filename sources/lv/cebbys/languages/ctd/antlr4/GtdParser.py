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
        4,1,35,340,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,5,0,64,8,0,10,0,12,0,
        67,9,0,1,0,5,0,70,8,0,10,0,12,0,73,9,0,1,0,1,0,1,1,1,1,1,1,1,2,5,
        2,81,8,2,10,2,12,2,84,9,2,1,2,1,2,1,2,1,2,5,2,90,8,2,10,2,12,2,93,
        9,2,1,2,5,2,96,8,2,10,2,12,2,99,9,2,1,2,1,2,1,3,5,3,104,8,3,10,3,
        12,3,107,9,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,119,8,4,
        1,5,5,5,122,8,5,10,5,12,5,125,9,5,1,5,1,5,1,5,1,5,1,6,5,6,132,8,
        6,10,6,12,6,135,9,6,1,6,1,6,1,6,1,6,1,7,5,7,142,8,7,10,7,12,7,145,
        9,7,1,7,1,7,1,7,1,7,3,7,151,8,7,1,7,1,7,3,7,155,8,7,1,7,1,7,1,8,
        5,8,160,8,8,10,8,12,8,163,9,8,1,8,1,8,1,8,1,8,3,8,169,8,8,1,8,1,
        8,3,8,173,8,8,1,8,1,8,1,9,1,9,5,9,179,8,9,10,9,12,9,182,9,9,1,10,
        1,10,1,10,3,10,187,8,10,1,11,1,11,5,11,191,8,11,10,11,12,11,194,
        9,11,1,12,1,12,1,12,3,12,199,8,12,1,13,5,13,202,8,13,10,13,12,13,
        205,9,13,1,13,1,13,1,13,1,13,3,13,211,8,13,1,13,1,13,1,14,5,14,216,
        8,14,10,14,12,14,219,9,14,1,14,1,14,1,14,1,14,3,14,225,8,14,1,14,
        1,14,1,15,1,15,5,15,231,8,15,10,15,12,15,234,9,15,1,16,1,16,5,16,
        238,8,16,10,16,12,16,241,9,16,1,17,1,17,1,17,1,18,5,18,247,8,18,
        10,18,12,18,250,9,18,1,18,1,18,1,18,1,18,3,18,256,8,18,1,18,1,18,
        1,19,1,19,1,19,5,19,263,8,19,10,19,12,19,266,9,19,1,19,3,19,269,
        8,19,1,20,5,20,272,8,20,10,20,12,20,275,9,20,1,20,1,20,1,20,1,21,
        1,21,1,21,1,21,3,21,284,8,21,1,21,3,21,287,8,21,1,22,1,22,1,22,5,
        22,292,8,22,10,22,12,22,295,9,22,1,23,1,23,1,24,3,24,300,8,24,1,
        24,1,24,3,24,304,8,24,1,24,3,24,307,8,24,1,24,3,24,310,8,24,1,25,
        1,25,3,25,314,8,25,1,25,3,25,317,8,25,1,26,1,26,1,26,1,26,1,27,1,
        27,1,28,1,28,1,29,4,29,328,8,29,11,29,12,29,329,1,30,1,30,1,30,5,
        30,335,8,30,10,30,12,30,338,9,30,1,30,0,0,31,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,0,4,1,0,30,31,1,0,29,32,1,0,20,21,1,0,22,26,354,0,65,1,0,0,0,
        2,76,1,0,0,0,4,82,1,0,0,0,6,105,1,0,0,0,8,118,1,0,0,0,10,123,1,0,
        0,0,12,133,1,0,0,0,14,143,1,0,0,0,16,161,1,0,0,0,18,176,1,0,0,0,
        20,183,1,0,0,0,22,188,1,0,0,0,24,195,1,0,0,0,26,203,1,0,0,0,28,217,
        1,0,0,0,30,228,1,0,0,0,32,235,1,0,0,0,34,242,1,0,0,0,36,248,1,0,
        0,0,38,259,1,0,0,0,40,273,1,0,0,0,42,279,1,0,0,0,44,288,1,0,0,0,
        46,296,1,0,0,0,48,309,1,0,0,0,50,311,1,0,0,0,52,318,1,0,0,0,54,322,
        1,0,0,0,56,324,1,0,0,0,58,327,1,0,0,0,60,331,1,0,0,0,62,64,3,2,1,
        0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,71,
        1,0,0,0,67,65,1,0,0,0,68,70,3,4,2,0,69,68,1,0,0,0,70,73,1,0,0,0,
        71,69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,74,75,5,
        0,0,1,75,1,1,0,0,0,76,77,5,1,0,0,77,78,5,32,0,0,78,3,1,0,0,0,79,
        81,3,42,21,0,80,79,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,
        0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,86,5,2,0,0,86,87,3,60,30,0,87,
        91,5,3,0,0,88,90,3,6,3,0,89,88,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,
        0,91,92,1,0,0,0,92,97,1,0,0,0,93,91,1,0,0,0,94,96,3,8,4,0,95,94,
        1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,
        99,97,1,0,0,0,100,101,5,4,0,0,101,5,1,0,0,0,102,104,3,42,21,0,103,
        102,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,
        108,1,0,0,0,107,105,1,0,0,0,108,109,5,5,0,0,109,110,3,60,30,0,110,
        7,1,0,0,0,111,119,3,10,5,0,112,119,3,12,6,0,113,119,3,14,7,0,114,
        119,3,16,8,0,115,119,3,26,13,0,116,119,3,28,14,0,117,119,3,36,18,
        0,118,111,1,0,0,0,118,112,1,0,0,0,118,113,1,0,0,0,118,114,1,0,0,
        0,118,115,1,0,0,0,118,116,1,0,0,0,118,117,1,0,0,0,119,9,1,0,0,0,
        120,122,3,42,21,0,121,120,1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,
        0,123,124,1,0,0,0,124,126,1,0,0,0,125,123,1,0,0,0,126,127,5,6,0,
        0,127,128,3,48,24,0,128,129,5,29,0,0,129,11,1,0,0,0,130,132,3,42,
        21,0,131,130,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,
        0,0,134,136,1,0,0,0,135,133,1,0,0,0,136,137,5,7,0,0,137,138,3,48,
        24,0,138,139,5,29,0,0,139,13,1,0,0,0,140,142,3,42,21,0,141,140,1,
        0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,146,1,
        0,0,0,145,143,1,0,0,0,146,147,5,8,0,0,147,150,5,29,0,0,148,149,5,
        9,0,0,149,151,3,48,24,0,150,148,1,0,0,0,150,151,1,0,0,0,151,152,
        1,0,0,0,152,154,5,3,0,0,153,155,3,18,9,0,154,153,1,0,0,0,154,155,
        1,0,0,0,155,156,1,0,0,0,156,157,5,4,0,0,157,15,1,0,0,0,158,160,3,
        42,21,0,159,158,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,
        1,0,0,0,162,164,1,0,0,0,163,161,1,0,0,0,164,165,5,10,0,0,165,168,
        5,29,0,0,166,167,5,9,0,0,167,169,3,48,24,0,168,166,1,0,0,0,168,169,
        1,0,0,0,169,170,1,0,0,0,170,172,5,3,0,0,171,173,3,22,11,0,172,171,
        1,0,0,0,172,173,1,0,0,0,173,174,1,0,0,0,174,175,5,4,0,0,175,17,1,
        0,0,0,176,180,3,20,10,0,177,179,3,20,10,0,178,177,1,0,0,0,179,182,
        1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,19,1,0,0,0,182,180,1,
        0,0,0,183,186,5,29,0,0,184,185,5,11,0,0,185,187,7,0,0,0,186,184,
        1,0,0,0,186,187,1,0,0,0,187,21,1,0,0,0,188,192,3,24,12,0,189,191,
        3,24,12,0,190,189,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,
        1,0,0,0,193,23,1,0,0,0,194,192,1,0,0,0,195,198,5,29,0,0,196,197,
        5,11,0,0,197,199,7,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,25,
        1,0,0,0,200,202,3,42,21,0,201,200,1,0,0,0,202,205,1,0,0,0,203,201,
        1,0,0,0,203,204,1,0,0,0,204,206,1,0,0,0,205,203,1,0,0,0,206,207,
        5,12,0,0,207,208,5,29,0,0,208,210,5,3,0,0,209,211,3,32,16,0,210,
        209,1,0,0,0,210,211,1,0,0,0,211,212,1,0,0,0,212,213,5,4,0,0,213,
        27,1,0,0,0,214,216,3,42,21,0,215,214,1,0,0,0,216,219,1,0,0,0,217,
        215,1,0,0,0,217,218,1,0,0,0,218,220,1,0,0,0,219,217,1,0,0,0,220,
        221,5,13,0,0,221,222,5,29,0,0,222,224,5,3,0,0,223,225,3,30,15,0,
        224,223,1,0,0,0,224,225,1,0,0,0,225,226,1,0,0,0,226,227,5,4,0,0,
        227,29,1,0,0,0,228,232,3,36,18,0,229,231,3,36,18,0,230,229,1,0,0,
        0,231,234,1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,31,1,0,0,0,
        234,232,1,0,0,0,235,239,3,34,17,0,236,238,3,34,17,0,237,236,1,0,
        0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,33,1,0,0,
        0,241,239,1,0,0,0,242,243,3,48,24,0,243,244,5,29,0,0,244,35,1,0,
        0,0,245,247,3,42,21,0,246,245,1,0,0,0,247,250,1,0,0,0,248,246,1,
        0,0,0,248,249,1,0,0,0,249,251,1,0,0,0,250,248,1,0,0,0,251,252,3,
        48,24,0,252,253,5,29,0,0,253,255,5,14,0,0,254,256,3,38,19,0,255,
        254,1,0,0,0,255,256,1,0,0,0,256,257,1,0,0,0,257,258,5,15,0,0,258,
        37,1,0,0,0,259,264,3,40,20,0,260,261,5,16,0,0,261,263,3,40,20,0,
        262,260,1,0,0,0,263,266,1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,
        265,268,1,0,0,0,266,264,1,0,0,0,267,269,5,16,0,0,268,267,1,0,0,0,
        268,269,1,0,0,0,269,39,1,0,0,0,270,272,3,42,21,0,271,270,1,0,0,0,
        272,275,1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,0,274,276,1,0,0,0,
        275,273,1,0,0,0,276,277,3,48,24,0,277,278,5,29,0,0,278,41,1,0,0,
        0,279,280,5,17,0,0,280,286,5,29,0,0,281,283,5,14,0,0,282,284,3,44,
        22,0,283,282,1,0,0,0,283,284,1,0,0,0,284,285,1,0,0,0,285,287,5,15,
        0,0,286,281,1,0,0,0,286,287,1,0,0,0,287,43,1,0,0,0,288,293,3,46,
        23,0,289,290,5,16,0,0,290,292,3,46,23,0,291,289,1,0,0,0,292,295,
        1,0,0,0,293,291,1,0,0,0,293,294,1,0,0,0,294,45,1,0,0,0,295,293,1,
        0,0,0,296,297,7,1,0,0,297,47,1,0,0,0,298,300,3,54,27,0,299,298,1,
        0,0,0,299,300,1,0,0,0,300,301,1,0,0,0,301,303,3,56,28,0,302,304,
        3,52,26,0,303,302,1,0,0,0,303,304,1,0,0,0,304,306,1,0,0,0,305,307,
        3,58,29,0,306,305,1,0,0,0,306,307,1,0,0,0,307,310,1,0,0,0,308,310,
        3,50,25,0,309,299,1,0,0,0,309,308,1,0,0,0,310,49,1,0,0,0,311,313,
        3,60,30,0,312,314,3,52,26,0,313,312,1,0,0,0,313,314,1,0,0,0,314,
        316,1,0,0,0,315,317,3,58,29,0,316,315,1,0,0,0,316,317,1,0,0,0,317,
        51,1,0,0,0,318,319,5,18,0,0,319,320,5,30,0,0,320,321,5,19,0,0,321,
        53,1,0,0,0,322,323,7,2,0,0,323,55,1,0,0,0,324,325,7,3,0,0,325,57,
        1,0,0,0,326,328,5,27,0,0,327,326,1,0,0,0,328,329,1,0,0,0,329,327,
        1,0,0,0,329,330,1,0,0,0,330,59,1,0,0,0,331,336,5,29,0,0,332,333,
        5,28,0,0,333,335,5,29,0,0,334,332,1,0,0,0,335,338,1,0,0,0,336,334,
        1,0,0,0,336,337,1,0,0,0,337,61,1,0,0,0,338,336,1,0,0,0,41,65,71,
        82,91,97,105,118,123,133,143,150,154,161,168,172,180,186,192,198,
        203,210,217,224,232,239,248,255,264,268,273,283,286,293,299,303,
        306,309,313,316,329,336
    ]

class GtdParser ( Parser ):

    grammarFileName = "Gtd.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'import'", "'namespace'", "'{'", "'}'", 
                     "'use'", "'typedef'", "'alias'", "'enum'", "':'", "'flag'", 
                     "'='", "'structure'", "'interface'", "'('", "')'", 
                     "','", "'@'", "'['", "']'", "'signed'", "'unsigned'", 
                     "'char'", "'short'", "'int'", "'long'", "'void'", "'*'", 
                     "'::'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    RULE_aliasDeclaration = 6
    RULE_enumDeclaration = 7
    RULE_flagDeclaration = 8
    RULE_enumMemberList = 9
    RULE_enumMember = 10
    RULE_flagMemberList = 11
    RULE_flagMember = 12
    RULE_structureDeclaration = 13
    RULE_interfaceDeclaration = 14
    RULE_interfaceMethodList = 15
    RULE_structureMemberList = 16
    RULE_structureMember = 17
    RULE_functionDeclaration = 18
    RULE_parameterList = 19
    RULE_parameter = 20
    RULE_decorator = 21
    RULE_decoratorArguments = 22
    RULE_decoratorArgument = 23
    RULE_typeSpec = 24
    RULE_typeReference = 25
    RULE_arrayModifier = 26
    RULE_signModifier = 27
    RULE_primitiveType = 28
    RULE_pointerModifier = 29
    RULE_qualifiedName = 30

    ruleNames =  [ "compilationUnit", "importDeclaration", "namespaceDeclaration", 
                   "useDeclaration", "declaration", "typedefDeclaration", 
                   "aliasDeclaration", "enumDeclaration", "flagDeclaration", 
                   "enumMemberList", "enumMember", "flagMemberList", "flagMember", 
                   "structureDeclaration", "interfaceDeclaration", "interfaceMethodList", 
                   "structureMemberList", "structureMember", "functionDeclaration", 
                   "parameterList", "parameter", "decorator", "decoratorArguments", 
                   "decoratorArgument", "typeSpec", "typeReference", "arrayModifier", 
                   "signModifier", "primitiveType", "pointerModifier", "qualifiedName" ]

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
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    IDENTIFIER=29
    INTEGER_LITERAL=30
    HEX_LITERAL=31
    STRING_LITERAL=32
    WHITESPACE=33
    LINE_COMMENT=34
    BLOCK_COMMENT=35

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
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 62
                self.importDeclaration()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==17:
                self.state = 68
                self.namespaceDeclaration()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
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
            self.state = 76
            self.match(GtdParser.T__0)
            self.state = 77
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


        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.DecoratorContext)
            else:
                return self.getTypedRuleContext(GtdParser.DecoratorContext,i)


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
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 79
                self.decorator()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(GtdParser.T__1)
            self.state = 86
            self.qualifiedName()
            self.state = 87
            self.match(GtdParser.T__2)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 88
                    self.useDeclaration() 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 670184896) != 0):
                self.state = 94
                self.declaration()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
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


        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.DecoratorContext)
            else:
                return self.getTypedRuleContext(GtdParser.DecoratorContext,i)


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
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 102
                self.decorator()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.match(GtdParser.T__4)
            self.state = 109
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


        def aliasDeclaration(self):
            return self.getTypedRuleContext(GtdParser.AliasDeclarationContext,0)


        def enumDeclaration(self):
            return self.getTypedRuleContext(GtdParser.EnumDeclarationContext,0)


        def flagDeclaration(self):
            return self.getTypedRuleContext(GtdParser.FlagDeclarationContext,0)


        def structureDeclaration(self):
            return self.getTypedRuleContext(GtdParser.StructureDeclarationContext,0)


        def interfaceDeclaration(self):
            return self.getTypedRuleContext(GtdParser.InterfaceDeclarationContext,0)


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
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.typedefDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.aliasDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.enumDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 114
                self.flagDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 115
                self.structureDeclaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 116
                self.interfaceDeclaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 117
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

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.DecoratorContext)
            else:
                return self.getTypedRuleContext(GtdParser.DecoratorContext,i)


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
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 120
                self.decorator()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self.match(GtdParser.T__5)
            self.state = 127
            self.typeSpec()
            self.state = 128
            self.match(GtdParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AliasDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpec(self):
            return self.getTypedRuleContext(GtdParser.TypeSpecContext,0)


        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.DecoratorContext)
            else:
                return self.getTypedRuleContext(GtdParser.DecoratorContext,i)


        def getRuleIndex(self):
            return GtdParser.RULE_aliasDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAliasDeclaration" ):
                listener.enterAliasDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAliasDeclaration" ):
                listener.exitAliasDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAliasDeclaration" ):
                return visitor.visitAliasDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def aliasDeclaration(self):

        localctx = GtdParser.AliasDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_aliasDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 130
                self.decorator()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self.match(GtdParser.T__6)
            self.state = 137
            self.typeSpec()
            self.state = 138
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

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.DecoratorContext)
            else:
                return self.getTypedRuleContext(GtdParser.DecoratorContext,i)


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
        self.enterRule(localctx, 14, self.RULE_enumDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 140
                self.decorator()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self.match(GtdParser.T__7)
            self.state = 147
            self.match(GtdParser.IDENTIFIER)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 148
                self.match(GtdParser.T__8)
                self.state = 149
                self.typeSpec()


            self.state = 152
            self.match(GtdParser.T__2)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 153
                self.enumMemberList()


            self.state = 156
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

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.DecoratorContext)
            else:
                return self.getTypedRuleContext(GtdParser.DecoratorContext,i)


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
        self.enterRule(localctx, 16, self.RULE_flagDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 158
                self.decorator()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self.match(GtdParser.T__9)
            self.state = 165
            self.match(GtdParser.IDENTIFIER)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 166
                self.match(GtdParser.T__8)
                self.state = 167
                self.typeSpec()


            self.state = 170
            self.match(GtdParser.T__2)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 171
                self.flagMemberList()


            self.state = 174
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
        self.enterRule(localctx, 18, self.RULE_enumMemberList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.enumMember()
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 177
                self.enumMember()
                self.state = 182
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
        self.enterRule(localctx, 20, self.RULE_enumMember)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(GtdParser.IDENTIFIER)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 184
                self.match(GtdParser.T__10)
                self.state = 185
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
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
        self.enterRule(localctx, 22, self.RULE_flagMemberList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.flagMember()
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 189
                self.flagMember()
                self.state = 194
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

        def INTEGER_LITERAL(self):
            return self.getToken(GtdParser.INTEGER_LITERAL, 0)

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
        self.enterRule(localctx, 24, self.RULE_flagMember)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(GtdParser.IDENTIFIER)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 196
                self.match(GtdParser.T__10)
                self.state = 197
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
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


    class StructureDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.DecoratorContext)
            else:
                return self.getTypedRuleContext(GtdParser.DecoratorContext,i)


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
        self.enterRule(localctx, 26, self.RULE_structureDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 200
                self.decorator()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206
            self.match(GtdParser.T__11)
            self.state = 207
            self.match(GtdParser.IDENTIFIER)
            self.state = 208
            self.match(GtdParser.T__2)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 670040064) != 0):
                self.state = 209
                self.structureMemberList()


            self.state = 212
            self.match(GtdParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.DecoratorContext)
            else:
                return self.getTypedRuleContext(GtdParser.DecoratorContext,i)


        def interfaceMethodList(self):
            return self.getTypedRuleContext(GtdParser.InterfaceMethodListContext,0)


        def getRuleIndex(self):
            return GtdParser.RULE_interfaceDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceDeclaration" ):
                listener.enterInterfaceDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceDeclaration" ):
                listener.exitInterfaceDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDeclaration" ):
                return visitor.visitInterfaceDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDeclaration(self):

        localctx = GtdParser.InterfaceDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_interfaceDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 214
                self.decorator()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 220
            self.match(GtdParser.T__12)
            self.state = 221
            self.match(GtdParser.IDENTIFIER)
            self.state = 222
            self.match(GtdParser.T__2)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 670171136) != 0):
                self.state = 223
                self.interfaceMethodList()


            self.state = 226
            self.match(GtdParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceMethodListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.FunctionDeclarationContext)
            else:
                return self.getTypedRuleContext(GtdParser.FunctionDeclarationContext,i)


        def getRuleIndex(self):
            return GtdParser.RULE_interfaceMethodList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceMethodList" ):
                listener.enterInterfaceMethodList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceMethodList" ):
                listener.exitInterfaceMethodList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceMethodList" ):
                return visitor.visitInterfaceMethodList(self)
            else:
                return visitor.visitChildren(self)




    def interfaceMethodList(self):

        localctx = GtdParser.InterfaceMethodListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_interfaceMethodList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.functionDeclaration()
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 670171136) != 0):
                self.state = 229
                self.functionDeclaration()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 32, self.RULE_structureMemberList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.structureMember()
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 670040064) != 0):
                self.state = 236
                self.structureMember()
                self.state = 241
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
        self.enterRule(localctx, 34, self.RULE_structureMember)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.typeSpec()
            self.state = 243
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

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.DecoratorContext)
            else:
                return self.getTypedRuleContext(GtdParser.DecoratorContext,i)


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
        self.enterRule(localctx, 36, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 245
                self.decorator()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 251
            self.typeSpec()
            self.state = 252
            self.match(GtdParser.IDENTIFIER)
            self.state = 253
            self.match(GtdParser.T__13)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 670171136) != 0):
                self.state = 254
                self.parameterList()


            self.state = 257
            self.match(GtdParser.T__14)
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
        self.enterRule(localctx, 38, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.parameter()
            self.state = 264
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 260
                    self.match(GtdParser.T__15)
                    self.state = 261
                    self.parameter() 
                self.state = 266
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 267
                self.match(GtdParser.T__15)


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

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.DecoratorContext)
            else:
                return self.getTypedRuleContext(GtdParser.DecoratorContext,i)


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
        self.enterRule(localctx, 40, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 270
                self.decorator()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 276
            self.typeSpec()
            self.state = 277
            self.match(GtdParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecoratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def decoratorArguments(self):
            return self.getTypedRuleContext(GtdParser.DecoratorArgumentsContext,0)


        def getRuleIndex(self):
            return GtdParser.RULE_decorator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecorator" ):
                listener.enterDecorator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecorator" ):
                listener.exitDecorator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecorator" ):
                return visitor.visitDecorator(self)
            else:
                return visitor.visitChildren(self)




    def decorator(self):

        localctx = GtdParser.DecoratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_decorator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(GtdParser.T__16)
            self.state = 280
            self.match(GtdParser.IDENTIFIER)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 281
                self.match(GtdParser.T__13)
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0):
                    self.state = 282
                    self.decoratorArguments()


                self.state = 285
                self.match(GtdParser.T__14)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecoratorArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decoratorArgument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GtdParser.DecoratorArgumentContext)
            else:
                return self.getTypedRuleContext(GtdParser.DecoratorArgumentContext,i)


        def getRuleIndex(self):
            return GtdParser.RULE_decoratorArguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecoratorArguments" ):
                listener.enterDecoratorArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecoratorArguments" ):
                listener.exitDecoratorArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecoratorArguments" ):
                return visitor.visitDecoratorArguments(self)
            else:
                return visitor.visitChildren(self)




    def decoratorArguments(self):

        localctx = GtdParser.DecoratorArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_decoratorArguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.decoratorArgument()
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 289
                self.match(GtdParser.T__15)
                self.state = 290
                self.decoratorArgument()
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecoratorArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(GtdParser.STRING_LITERAL, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(GtdParser.INTEGER_LITERAL, 0)

        def HEX_LITERAL(self):
            return self.getToken(GtdParser.HEX_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(GtdParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GtdParser.RULE_decoratorArgument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecoratorArgument" ):
                listener.enterDecoratorArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecoratorArgument" ):
                listener.exitDecoratorArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecoratorArgument" ):
                return visitor.visitDecoratorArgument(self)
            else:
                return visitor.visitChildren(self)




    def decoratorArgument(self):

        localctx = GtdParser.DecoratorArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_decoratorArgument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0)):
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


    class TypeSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(GtdParser.PrimitiveTypeContext,0)


        def signModifier(self):
            return self.getTypedRuleContext(GtdParser.SignModifierContext,0)


        def arrayModifier(self):
            return self.getTypedRuleContext(GtdParser.ArrayModifierContext,0)


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
        self.enterRule(localctx, 48, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 24, 25, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20 or _la==21:
                    self.state = 298
                    self.signModifier()


                self.state = 301
                self.primitiveType()
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 302
                    self.arrayModifier()


                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 305
                    self.pointerModifier()


                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
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


        def arrayModifier(self):
            return self.getTypedRuleContext(GtdParser.ArrayModifierContext,0)


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
        self.enterRule(localctx, 50, self.RULE_typeReference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.qualifiedName()
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 312
                self.arrayModifier()


            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 315
                self.pointerModifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(GtdParser.INTEGER_LITERAL, 0)

        def getRuleIndex(self):
            return GtdParser.RULE_arrayModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayModifier" ):
                listener.enterArrayModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayModifier" ):
                listener.exitArrayModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayModifier" ):
                return visitor.visitArrayModifier(self)
            else:
                return visitor.visitChildren(self)




    def arrayModifier(self):

        localctx = GtdParser.ArrayModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_arrayModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(GtdParser.T__17)
            self.state = 319
            self.match(GtdParser.INTEGER_LITERAL)
            self.state = 320
            self.match(GtdParser.T__18)
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
        self.enterRule(localctx, 54, self.RULE_signModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
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
        self.enterRule(localctx, 56, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 130023424) != 0)):
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
        self.enterRule(localctx, 58, self.RULE_pointerModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 326
                self.match(GtdParser.T__26)
                self.state = 329 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==27):
                    break

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
        self.enterRule(localctx, 60, self.RULE_qualifiedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(GtdParser.IDENTIFIER)
            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 332
                self.match(GtdParser.T__27)
                self.state = 333
                self.match(GtdParser.IDENTIFIER)
                self.state = 338
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






grammar Ctd;

// Parser rules
moduleDeclaration: importDeclaration* namespaceDeclaration* EOF;

importDeclaration: 'import' STRING_LITERAL;

namespaceDeclaration:
    decorator* 'namespace' qualifiedName '{' useDeclaration* declaration* '}';

useDeclaration: decorator* 'use' qualifiedName;

declaration:
    typedefDeclaration
    | aliasDeclaration
    | enumDeclaration
    | flagDeclaration
    | structureDeclaration
    | interfaceDeclaration
    | functionDeclaration
    | classDeclaration;

typedefDeclaration: decorator* 'typedef' typeSpec IDENTIFIER;

aliasDeclaration: decorator* 'alias' typeSpec IDENTIFIER;

enumDeclaration:
    decorator* 'enum' IDENTIFIER ':' typeSpec '{' enumMemberList? '}';

flagDeclaration:
    decorator* 'flag' IDENTIFIER ':' typeSpec '{' flagMemberList? '}';

enumMemberList: enumMember enumMember*;

enumMember: IDENTIFIER ('=' (INTEGER_LITERAL | HEX_LITERAL))?;

flagMemberList: flagMember flagMember*;

flagMember: IDENTIFIER ('=' (INTEGER_LITERAL | HEX_LITERAL))?;

structureDeclaration:
    decorator* 'structure' IDENTIFIER (':' typeSpec)? '{' structureMemberList? '}';

interfaceDeclaration:
    decorator* 'interface' IDENTIFIER (':' typeSpec)? '{' interfaceMethodList? '}';

interfaceMethodList: functionDeclaration functionDeclaration*;

classDeclaration:
    decorator* 'class' IDENTIFIER (':' typeSpec (',' typeSpec)*)? '{' classMemberList? classMethodList? '}';

classMemberList: classMember classMember*;

classMember: decorator* typeSpec IDENTIFIER;

classMethodList: functionDeclaration functionDeclaration*;

structureMemberList: structureMember structureMember*;

structureMember: typeSpec IDENTIFIER;

functionDeclaration:
    decorator* typeSpec IDENTIFIER '(' parameterList? ')';

parameterList: parameter (',' parameter)* ','?;

parameter: decorator* typeSpec IDENTIFIER;

decorator: '@' IDENTIFIER ('(' decoratorArguments? ')')?;

decoratorArguments: decoratorArgument (',' decoratorArgument)*;

decoratorArgument:
    STRING_LITERAL
    | INTEGER_LITERAL
    | HEX_LITERAL
    | IDENTIFIER;

typeSpec: signModifier? typeReference;

typeReference: qualifiedName typeExtension*;

typeExtension: arrayModifier | pointerModifier;

arrayModifier: '[' INTEGER_LITERAL ']';

signModifier: 'signed' | 'unsigned';

pointerModifier: '*';

qualifiedName: IDENTIFIER ('::' IDENTIFIER)*;

// Lexer rules
IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;

INTEGER_LITERAL: [0-9]+;

HEX_LITERAL: '0x' [0-9a-fA-F]+;

STRING_LITERAL: '"' ~["\r\n]* '"';

WHITESPACE: [ \t\r\n]+ -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;

BLOCK_COMMENT: '/*' .*? '*/' -> skip;
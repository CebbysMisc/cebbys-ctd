grammar Gtd;

// Parser rules
compilationUnit: importDeclaration* namespaceDeclaration* EOF;

importDeclaration: 'import' STRING_LITERAL;

namespaceDeclaration:
    annotation? 'namespace' qualifiedName '{' useDeclaration* declaration* '}';

useDeclaration: annotation? 'use' qualifiedName;

declaration: 
    typedefDeclaration 
    | enumDeclaration
    | flagDeclaration
    | structureDeclaration
    | functionDeclaration;

typedefDeclaration: annotation? 'typedef' typeSpec IDENTIFIER;

enumDeclaration:
    annotation? 'enum' IDENTIFIER (':' typeSpec)? '{' enumMemberList? '}';

flagDeclaration:
    annotation? 'flag' IDENTIFIER (':' typeSpec)? '{' flagMemberList? '}';

enumMemberList: enumMember enumMember*;

enumMember: IDENTIFIER ('=' (INTEGER_LITERAL | HEX_LITERAL))?;

flagMemberList: flagMember flagMember*;

flagMember: IDENTIFIER ('=' HEX_LITERAL)?;

structureDeclaration:
    annotation? 'structure' IDENTIFIER '{' structureMemberList? '}';

structureMemberList: structureMember structureMember*;

structureMember: typeSpec IDENTIFIER;

functionDeclaration:
    annotation? typeSpec IDENTIFIER '(' parameterList? ')';

annotation: '@' IDENTIFIER ('(' annotationArguments? ')')?;

annotationArguments: STRING_LITERAL (',' STRING_LITERAL)*;

parameterList: parameter (',' parameter)*;

parameter: annotation? typeSpec IDENTIFIER;

typeSpec:
    signModifier? primitiveType pointerModifier?
    | typeReference;

typeReference: qualifiedName pointerModifier?;

signModifier: 'signed' | 'unsigned';

primitiveType: 'char' | 'short' | 'int' | 'long' | 'void';

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
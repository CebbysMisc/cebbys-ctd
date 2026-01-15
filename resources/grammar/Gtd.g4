grammar Gtd;

// Parser rules
compilationUnit: importDeclaration* namespaceDeclaration* EOF;

importDeclaration: 'import' STRING_LITERAL;

namespaceDeclaration:
    'namespace' qualifiedName '{' useDeclaration* declaration* '}';

useDeclaration: 'use' qualifiedName;

declaration: 
    typedefDeclaration 
    | enumDeclaration 
    | structureDeclaration
    | functionDeclaration;

typedefDeclaration: 'typedef' typeSpec IDENTIFIER;

enumDeclaration:
    'enum' IDENTIFIER (':' typeSpec)? '{' enumMemberList? '}';

enumMemberList: enumMember enumMember*;

enumMember: IDENTIFIER ('=' INTEGER_LITERAL)?;

structureDeclaration:
    'structure' IDENTIFIER '{' structureMemberList? '}';

structureMemberList: structureMember structureMember*;

structureMember: typeSpec IDENTIFIER;

functionDeclaration:
    annotation? typeSpec IDENTIFIER '(' parameterList? ')';

annotation: '@' IDENTIFIER;

parameterList: parameter (',' parameter)*;

parameter: typeSpec IDENTIFIER;

typeSpec:
    signModifier? primitiveType pointerModifier?
    | typeReference;

typeReference: IDENTIFIER pointerModifier?;

signModifier: 'signed' | 'unsigned';

primitiveType: 'char' | 'short' | 'int' | 'long' | 'void';

pointerModifier: '*';

qualifiedName: IDENTIFIER ('::' IDENTIFIER)*;

// Lexer rules
IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;

INTEGER_LITERAL: [0-9]+;

STRING_LITERAL: '"' ~["\r\n]* '"';

WHITESPACE: [ \t\r\n]+ -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;

BLOCK_COMMENT: '/*' .*? '*/' -> skip;
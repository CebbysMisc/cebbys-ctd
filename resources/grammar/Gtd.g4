grammar Gtd;

// Parser rules
compilationUnit: namespaceDeclaration* EOF;

namespaceDeclaration:
    'namespace' qualifiedName '{' declaration* '}';

declaration: typedefDeclaration | enumDeclaration;

typedefDeclaration: 'typedef' typeSpec IDENTIFIER;

enumDeclaration:
    'enum' IDENTIFIER (':' typeSpec)? '{' enumMemberList? '}';

enumMemberList: enumMember enumMember*;

enumMember: IDENTIFIER ('=' INTEGER_LITERAL)?;

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

WHITESPACE: [ \t\r\n]+ -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;

BLOCK_COMMENT: '/*' .*? '*/' -> skip;
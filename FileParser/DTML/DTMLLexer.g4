lexer grammar DTMLLexer;

// Skip
WHITESPACE          : [ \t\r\n]+    -> skip;
BLOCK_COMMENT       : '/*' .*? '*/' ->  channel(HIDDEN);
LINE_COMMENT        : '--' .*? ('\n'|EOF) -> channel(HIDDEN);

TAG_OPEN            : '<';
TAG_CLOSE           : '>';
SLASH               : '/';

DTML_TAG_KEY        : 'dtml-';
DTML_TAG_SPEC                
    : 'var' | 'sqlvar' | 'sqlgroup' | 'and' | 'if' | 'in' | 'sqltest' | 'let'
    ;

EQ                  : '=';

STRING_LITERAL  
    : DQUOTA_STRING
    | SQUOTA_STRING
    | BQUOTA_STRING
    ;

fragment DQUOTA_STRING                : '"' ( '\\'. | '""' | ~('"' | '\\') )* '"';
fragment SQUOTA_STRING                : '\'' ('\\'. | '\'\'' | ~('\'' | '\\'))* '\'';
fragment BQUOTA_STRING                : '`' ( '\\'. | '``' | ~('`' | '\\'))* '`';

IDENTIFIER                           
    : '"' (~'"' | '""')* '"'
	| '`' (~'`' | '``')* '`'
	| '[' ~']'* ']'
	| [a-zA-Z_] [a-zA-Z_0-9$]*
    ;

UNEXPECTED_CHAR: .;

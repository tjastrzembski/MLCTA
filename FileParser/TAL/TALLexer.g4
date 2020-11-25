lexer grammar TALLexer;

// Skip
WHITESPACE          : [ \t\r\n]+    -> skip;
BLOCK_COMMENT       : '<!--' .*? '-->' ->  channel(HIDDEN);

TAG_OPEN_SLASH      : '</';
TAG_OPEN            : '<';
TAG_CLOSE           : '>';


TAL_TAG_KEY          : 'tal:';
METAL_TAG_KEY        : 'metal:';
NOT_KEY              : 'not:';
PYTHON_KEY           : 'python:';
STRING_KEY           : 'string:';

NOTHING_EXPR         : '|nothing';
ZOPE_KEY             : 'context';

ATTR_CONTENT        : 'content=';
ATTR_DEFINE         : 'define=';
ATTR_CONDITION      : 'condition=';
ATTR_DEFINE_MACRO   : 'define-macro=';
ATTR_USE_MACRO      : 'use-macro=';

DQUOTA              : '"';
SEMICOLON           : ';';


IDENTIFIER                           
    : '`' (~'`' | '``')* '`'
	| '[' ~']'* ']'
	| [a-zA-Z_] [a-zA-Z_0-9$]*
    ;

UNEXPECTED_CHAR: .;

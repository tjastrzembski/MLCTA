parser grammar TALParser;

options { tokenVocab=TALLexer; }


parse: stmt* EOF;

stmt
    : tag
    ;

tag
    : ( TAG_OPEN_SLASH close_tag | TAG_OPEN open_tag ) TAG_CLOSE 
    ;


open_tag
    : other_tag
    | tal_tag
    ;

close_tag
    :  tag_specifier? IDENTIFIER
    ;

tal_tag
    :  tag_specifier identifier tag_attr* 
    ;

other_tag
    : identifier  (TAL_TAG_KEY? tag_attr)* 
    ;


tag_specifier
    : TAL_TAG_KEY
    | METAL_TAG_KEY
    ;


tag_attr
    : tag_attr_key tag_attr_value?
    ;

tag_attr_key
    : ATTR_DEFINE
    | ATTR_CONDITION
    | ATTR_DEFINE_MACRO
    | ATTR_USE_MACRO
    | identifier
    ;

tag_attr_value
    : DQUOTA tag_attr_value_def (SEMICOLON tag_attr_value_def)* SEMICOLON? DQUOTA
    ;

tag_attr_value_def
    : identifier? NOT_KEY? tag_attr_expr NOTHING_EXPR?
    ;

tag_attr_expr
    : (PYTHON_KEY | STRING_KEY)? ZOPE_KEY function_ref 
    | identifier+
    ;

function_ref
    : identifier+
    ;

identifier
    : IDENTIFIER
    | UNEXPECTED_CHAR
    ;
    
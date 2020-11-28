parser grammar DTMLParser;

options { tokenVocab=DTMLLexer; }


parse: stmt* EOF;

stmt
    : dtml_tag
    | identifier+
    ;

dtml_tag
    : TAG_OPEN SLASH? dtml_tag_specifier dtml_tag_attr* TAG_CLOSE
    ;

dtml_tag_specifier
    : DTML_TAG_KEY DTML_TAG_SPEC
    ;

dtml_tag_attr
    : dtml_tag_var
    | dtml_tag_expr_stmt
    ;

dtml_tag_expr_stmt
    : dtml_tag_expr_keyword dtml_tag_expr_val
    ;

dtml_tag_expr_keyword
    : identifier EQ
    ;
    
dtml_tag_expr_val
    : STRING_LITERAL
    ;

dtml_tag_var
    : IDENTIFIER
    ;

identifier
    : STRING_LITERAL
    | IDENTIFIER
    | UNEXPECTED_CHAR
    | DTML_TAG_SPEC
    ;

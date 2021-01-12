# Generated from DTMLParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DTMLParser import DTMLParser
else:
    from DTMLParser import DTMLParser

# This class defines a complete listener for a parse tree produced by DTMLParser.
class DTMLParserListener(ParseTreeListener):

    # Enter a parse tree produced by DTMLParser#parse.
    def enterParse(self, ctx:DTMLParser.ParseContext):
        pass

    # Exit a parse tree produced by DTMLParser#parse.
    def exitParse(self, ctx:DTMLParser.ParseContext):
        pass


    # Enter a parse tree produced by DTMLParser#stmt.
    def enterStmt(self, ctx:DTMLParser.StmtContext):
        pass

    # Exit a parse tree produced by DTMLParser#stmt.
    def exitStmt(self, ctx:DTMLParser.StmtContext):
        pass


    # Enter a parse tree produced by DTMLParser#dtml_tag.
    def enterDtml_tag(self, ctx:DTMLParser.Dtml_tagContext):
        pass

    # Exit a parse tree produced by DTMLParser#dtml_tag.
    def exitDtml_tag(self, ctx:DTMLParser.Dtml_tagContext):
        pass


    # Enter a parse tree produced by DTMLParser#dtml_tag_specifier.
    def enterDtml_tag_specifier(self, ctx:DTMLParser.Dtml_tag_specifierContext):
        pass

    # Exit a parse tree produced by DTMLParser#dtml_tag_specifier.
    def exitDtml_tag_specifier(self, ctx:DTMLParser.Dtml_tag_specifierContext):
        pass


    # Enter a parse tree produced by DTMLParser#dtml_tag_attr.
    def enterDtml_tag_attr(self, ctx:DTMLParser.Dtml_tag_attrContext):
        pass

    # Exit a parse tree produced by DTMLParser#dtml_tag_attr.
    def exitDtml_tag_attr(self, ctx:DTMLParser.Dtml_tag_attrContext):
        pass


    # Enter a parse tree produced by DTMLParser#dtml_tag_expr_stmt.
    def enterDtml_tag_expr_stmt(self, ctx:DTMLParser.Dtml_tag_expr_stmtContext):
        pass

    # Exit a parse tree produced by DTMLParser#dtml_tag_expr_stmt.
    def exitDtml_tag_expr_stmt(self, ctx:DTMLParser.Dtml_tag_expr_stmtContext):
        pass


    # Enter a parse tree produced by DTMLParser#dtml_tag_expr_keyword.
    def enterDtml_tag_expr_keyword(self, ctx:DTMLParser.Dtml_tag_expr_keywordContext):
        pass

    # Exit a parse tree produced by DTMLParser#dtml_tag_expr_keyword.
    def exitDtml_tag_expr_keyword(self, ctx:DTMLParser.Dtml_tag_expr_keywordContext):
        pass


    # Enter a parse tree produced by DTMLParser#dtml_tag_expr_val.
    def enterDtml_tag_expr_val(self, ctx:DTMLParser.Dtml_tag_expr_valContext):
        pass

    # Exit a parse tree produced by DTMLParser#dtml_tag_expr_val.
    def exitDtml_tag_expr_val(self, ctx:DTMLParser.Dtml_tag_expr_valContext):
        pass


    # Enter a parse tree produced by DTMLParser#dtml_tag_var.
    def enterDtml_tag_var(self, ctx:DTMLParser.Dtml_tag_varContext):
        pass

    # Exit a parse tree produced by DTMLParser#dtml_tag_var.
    def exitDtml_tag_var(self, ctx:DTMLParser.Dtml_tag_varContext):
        pass


    # Enter a parse tree produced by DTMLParser#identifier.
    def enterIdentifier(self, ctx:DTMLParser.IdentifierContext):
        pass

    # Exit a parse tree produced by DTMLParser#identifier.
    def exitIdentifier(self, ctx:DTMLParser.IdentifierContext):
        pass



del DTMLParser
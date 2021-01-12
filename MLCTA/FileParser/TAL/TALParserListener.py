# Generated from TALParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TALParser import TALParser
else:
    from TALParser import TALParser

# This class defines a complete listener for a parse tree produced by TALParser.
class TALParserListener(ParseTreeListener):

    # Enter a parse tree produced by TALParser#parse.
    def enterParse(self, ctx:TALParser.ParseContext):
        pass

    # Exit a parse tree produced by TALParser#parse.
    def exitParse(self, ctx:TALParser.ParseContext):
        pass


    # Enter a parse tree produced by TALParser#stmt.
    def enterStmt(self, ctx:TALParser.StmtContext):
        pass

    # Exit a parse tree produced by TALParser#stmt.
    def exitStmt(self, ctx:TALParser.StmtContext):
        pass


    # Enter a parse tree produced by TALParser#open_tag.
    def enterOpen_tag(self, ctx:TALParser.Open_tagContext):
        pass

    # Exit a parse tree produced by TALParser#open_tag.
    def exitOpen_tag(self, ctx:TALParser.Open_tagContext):
        pass


    # Enter a parse tree produced by TALParser#close_tag.
    def enterClose_tag(self, ctx:TALParser.Close_tagContext):
        pass

    # Exit a parse tree produced by TALParser#close_tag.
    def exitClose_tag(self, ctx:TALParser.Close_tagContext):
        pass


    # Enter a parse tree produced by TALParser#tal_tag.
    def enterTal_tag(self, ctx:TALParser.Tal_tagContext):
        pass

    # Exit a parse tree produced by TALParser#tal_tag.
    def exitTal_tag(self, ctx:TALParser.Tal_tagContext):
        pass


    # Enter a parse tree produced by TALParser#other_tag.
    def enterOther_tag(self, ctx:TALParser.Other_tagContext):
        pass

    # Exit a parse tree produced by TALParser#other_tag.
    def exitOther_tag(self, ctx:TALParser.Other_tagContext):
        pass


    # Enter a parse tree produced by TALParser#tag_specifier.
    def enterTag_specifier(self, ctx:TALParser.Tag_specifierContext):
        pass

    # Exit a parse tree produced by TALParser#tag_specifier.
    def exitTag_specifier(self, ctx:TALParser.Tag_specifierContext):
        pass


    # Enter a parse tree produced by TALParser#tag_attr.
    def enterTag_attr(self, ctx:TALParser.Tag_attrContext):
        pass

    # Exit a parse tree produced by TALParser#tag_attr.
    def exitTag_attr(self, ctx:TALParser.Tag_attrContext):
        pass


    # Enter a parse tree produced by TALParser#tag_attr_key.
    def enterTag_attr_key(self, ctx:TALParser.Tag_attr_keyContext):
        pass

    # Exit a parse tree produced by TALParser#tag_attr_key.
    def exitTag_attr_key(self, ctx:TALParser.Tag_attr_keyContext):
        pass


    # Enter a parse tree produced by TALParser#tag_attr_value.
    def enterTag_attr_value(self, ctx:TALParser.Tag_attr_valueContext):
        pass

    # Exit a parse tree produced by TALParser#tag_attr_value.
    def exitTag_attr_value(self, ctx:TALParser.Tag_attr_valueContext):
        pass


    # Enter a parse tree produced by TALParser#tag_attr_value_def.
    def enterTag_attr_value_def(self, ctx:TALParser.Tag_attr_value_defContext):
        pass

    # Exit a parse tree produced by TALParser#tag_attr_value_def.
    def exitTag_attr_value_def(self, ctx:TALParser.Tag_attr_value_defContext):
        pass


    # Enter a parse tree produced by TALParser#tag_attr_expr.
    def enterTag_attr_expr(self, ctx:TALParser.Tag_attr_exprContext):
        pass

    # Exit a parse tree produced by TALParser#tag_attr_expr.
    def exitTag_attr_expr(self, ctx:TALParser.Tag_attr_exprContext):
        pass


    # Enter a parse tree produced by TALParser#function_ref.
    def enterFunction_ref(self, ctx:TALParser.Function_refContext):
        pass

    # Exit a parse tree produced by TALParser#function_ref.
    def exitFunction_ref(self, ctx:TALParser.Function_refContext):
        pass


    # Enter a parse tree produced by TALParser#identifier.
    def enterIdentifier(self, ctx:TALParser.IdentifierContext):
        pass

    # Exit a parse tree produced by TALParser#identifier.
    def exitIdentifier(self, ctx:TALParser.IdentifierContext):
        pass



del TALParser
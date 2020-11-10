# Generated from DTMLParser.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("D\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\2\3\2\3\3\3\3\6\3\37\n\3\r\3\16\3 \5\3#\n\3\3\4\3\4\5")
        buf.write("\4\'\n\4\3\4\3\4\7\4+\n\4\f\4\16\4.\13\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\5\69\n\6\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\3\3\2")
        buf.write("\f\17\2A\2\27\3\2\2\2\4\"\3\2\2\2\6$\3\2\2\2\b\61\3\2")
        buf.write("\2\2\n8\3\2\2\2\f:\3\2\2\2\16=\3\2\2\2\20?\3\2\2\2\22")
        buf.write("A\3\2\2\2\24\26\5\4\3\2\25\24\3\2\2\2\26\31\3\2\2\2\27")
        buf.write("\25\3\2\2\2\27\30\3\2\2\2\30\32\3\2\2\2\31\27\3\2\2\2")
        buf.write("\32\33\7\2\2\3\33\3\3\2\2\2\34#\5\6\4\2\35\37\5\22\n\2")
        buf.write("\36\35\3\2\2\2\37 \3\2\2\2 \36\3\2\2\2 !\3\2\2\2!#\3\2")
        buf.write("\2\2\"\34\3\2\2\2\"\36\3\2\2\2#\5\3\2\2\2$&\7\6\2\2%\'")
        buf.write("\7\b\2\2&%\3\2\2\2&\'\3\2\2\2\'(\3\2\2\2(,\5\b\5\2)+\5")
        buf.write("\n\6\2*)\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3\2\2\2-/\3\2\2")
        buf.write("\2.,\3\2\2\2/\60\7\7\2\2\60\7\3\2\2\2\61\62\7\t\2\2\62")
        buf.write("\63\7\f\2\2\63\t\3\2\2\2\649\5\20\t\2\659\5\f\7\2\66\67")
        buf.write("\7\13\2\2\679\7\r\2\28\64\3\2\2\28\65\3\2\2\28\66\3\2")
        buf.write("\2\29\13\3\2\2\2:;\7\n\2\2;<\5\16\b\2<\r\3\2\2\2=>\7\r")
        buf.write("\2\2>\17\3\2\2\2?@\7\16\2\2@\21\3\2\2\2AB\t\2\2\2B\23")
        buf.write("\3\2\2\2\b\27 \"&,8")
        return buf.getvalue()


class DTMLParser ( Parser ):

    grammarFileName = "DTMLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'<'", "'>'", "'/'", "'dtml-'", "'expr='", "'type='" ]

    symbolicNames = [ "<INVALID>", "WHITESPACE", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "TAG_OPEN", "TAG_CLOSE", "SLASH", "DTML_TAG_KEY", 
                      "DTML_TAG_EXPR", "DTML_TAG_TYPE", "DTML_TAG_SPEC", 
                      "STRING_LITERAL", "IDENTIFIER", "UNEXPECTED_CHAR" ]

    RULE_parse = 0
    RULE_stmt = 1
    RULE_dtml_tag = 2
    RULE_dtml_tag_specifier = 3
    RULE_dtml_tag_attr = 4
    RULE_dtml_tag_expr_stmt = 5
    RULE_dtml_tag_expr_val = 6
    RULE_dtml_tag_var = 7
    RULE_identifier = 8

    ruleNames =  [ "parse", "stmt", "dtml_tag", "dtml_tag_specifier", "dtml_tag_attr", 
                   "dtml_tag_expr_stmt", "dtml_tag_expr_val", "dtml_tag_var", 
                   "identifier" ]

    EOF = Token.EOF
    WHITESPACE=1
    BLOCK_COMMENT=2
    LINE_COMMENT=3
    TAG_OPEN=4
    TAG_CLOSE=5
    SLASH=6
    DTML_TAG_KEY=7
    DTML_TAG_EXPR=8
    DTML_TAG_TYPE=9
    DTML_TAG_SPEC=10
    STRING_LITERAL=11
    IDENTIFIER=12
    UNEXPECTED_CHAR=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DTMLParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DTMLParser.StmtContext)
            else:
                return self.getTypedRuleContext(DTMLParser.StmtContext,i)


        def getRuleIndex(self):
            return DTMLParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)




    def parse(self):

        localctx = DTMLParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DTMLParser.TAG_OPEN) | (1 << DTMLParser.DTML_TAG_SPEC) | (1 << DTMLParser.STRING_LITERAL) | (1 << DTMLParser.IDENTIFIER) | (1 << DTMLParser.UNEXPECTED_CHAR))) != 0):
                self.state = 18
                self.stmt()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(DTMLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dtml_tag(self):
            return self.getTypedRuleContext(DTMLParser.Dtml_tagContext,0)


        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DTMLParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(DTMLParser.IdentifierContext,i)


        def getRuleIndex(self):
            return DTMLParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = DTMLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DTMLParser.TAG_OPEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.dtml_tag()
                pass
            elif token in [DTMLParser.DTML_TAG_SPEC, DTMLParser.STRING_LITERAL, DTMLParser.IDENTIFIER, DTMLParser.UNEXPECTED_CHAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 27
                        self.identifier()

                    else:
                        raise NoViableAltException(self)
                    self.state = 30 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dtml_tagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAG_OPEN(self):
            return self.getToken(DTMLParser.TAG_OPEN, 0)

        def dtml_tag_specifier(self):
            return self.getTypedRuleContext(DTMLParser.Dtml_tag_specifierContext,0)


        def TAG_CLOSE(self):
            return self.getToken(DTMLParser.TAG_CLOSE, 0)

        def SLASH(self):
            return self.getToken(DTMLParser.SLASH, 0)

        def dtml_tag_attr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DTMLParser.Dtml_tag_attrContext)
            else:
                return self.getTypedRuleContext(DTMLParser.Dtml_tag_attrContext,i)


        def getRuleIndex(self):
            return DTMLParser.RULE_dtml_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDtml_tag" ):
                listener.enterDtml_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDtml_tag" ):
                listener.exitDtml_tag(self)




    def dtml_tag(self):

        localctx = DTMLParser.Dtml_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dtml_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(DTMLParser.TAG_OPEN)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DTMLParser.SLASH:
                self.state = 35
                self.match(DTMLParser.SLASH)


            self.state = 38
            self.dtml_tag_specifier()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DTMLParser.DTML_TAG_EXPR) | (1 << DTMLParser.DTML_TAG_TYPE) | (1 << DTMLParser.IDENTIFIER))) != 0):
                self.state = 39
                self.dtml_tag_attr()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(DTMLParser.TAG_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dtml_tag_specifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DTML_TAG_KEY(self):
            return self.getToken(DTMLParser.DTML_TAG_KEY, 0)

        def DTML_TAG_SPEC(self):
            return self.getToken(DTMLParser.DTML_TAG_SPEC, 0)

        def getRuleIndex(self):
            return DTMLParser.RULE_dtml_tag_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDtml_tag_specifier" ):
                listener.enterDtml_tag_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDtml_tag_specifier" ):
                listener.exitDtml_tag_specifier(self)




    def dtml_tag_specifier(self):

        localctx = DTMLParser.Dtml_tag_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dtml_tag_specifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(DTMLParser.DTML_TAG_KEY)
            self.state = 48
            self.match(DTMLParser.DTML_TAG_SPEC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dtml_tag_attrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dtml_tag_var(self):
            return self.getTypedRuleContext(DTMLParser.Dtml_tag_varContext,0)


        def dtml_tag_expr_stmt(self):
            return self.getTypedRuleContext(DTMLParser.Dtml_tag_expr_stmtContext,0)


        def DTML_TAG_TYPE(self):
            return self.getToken(DTMLParser.DTML_TAG_TYPE, 0)

        def STRING_LITERAL(self):
            return self.getToken(DTMLParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return DTMLParser.RULE_dtml_tag_attr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDtml_tag_attr" ):
                listener.enterDtml_tag_attr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDtml_tag_attr" ):
                listener.exitDtml_tag_attr(self)




    def dtml_tag_attr(self):

        localctx = DTMLParser.Dtml_tag_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dtml_tag_attr)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DTMLParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.dtml_tag_var()
                pass
            elif token in [DTMLParser.DTML_TAG_EXPR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.dtml_tag_expr_stmt()
                pass
            elif token in [DTMLParser.DTML_TAG_TYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.match(DTMLParser.DTML_TAG_TYPE)
                self.state = 53
                self.match(DTMLParser.STRING_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dtml_tag_expr_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DTML_TAG_EXPR(self):
            return self.getToken(DTMLParser.DTML_TAG_EXPR, 0)

        def dtml_tag_expr_val(self):
            return self.getTypedRuleContext(DTMLParser.Dtml_tag_expr_valContext,0)


        def getRuleIndex(self):
            return DTMLParser.RULE_dtml_tag_expr_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDtml_tag_expr_stmt" ):
                listener.enterDtml_tag_expr_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDtml_tag_expr_stmt" ):
                listener.exitDtml_tag_expr_stmt(self)




    def dtml_tag_expr_stmt(self):

        localctx = DTMLParser.Dtml_tag_expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dtml_tag_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(DTMLParser.DTML_TAG_EXPR)
            self.state = 57
            self.dtml_tag_expr_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dtml_tag_expr_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(DTMLParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return DTMLParser.RULE_dtml_tag_expr_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDtml_tag_expr_val" ):
                listener.enterDtml_tag_expr_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDtml_tag_expr_val" ):
                listener.exitDtml_tag_expr_val(self)




    def dtml_tag_expr_val(self):

        localctx = DTMLParser.Dtml_tag_expr_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dtml_tag_expr_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(DTMLParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dtml_tag_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(DTMLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return DTMLParser.RULE_dtml_tag_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDtml_tag_var" ):
                listener.enterDtml_tag_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDtml_tag_var" ):
                listener.exitDtml_tag_var(self)




    def dtml_tag_var(self):

        localctx = DTMLParser.Dtml_tag_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dtml_tag_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(DTMLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(DTMLParser.STRING_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(DTMLParser.IDENTIFIER, 0)

        def UNEXPECTED_CHAR(self):
            return self.getToken(DTMLParser.UNEXPECTED_CHAR, 0)

        def DTML_TAG_SPEC(self):
            return self.getToken(DTMLParser.DTML_TAG_SPEC, 0)

        def getRuleIndex(self):
            return DTMLParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = DTMLParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DTMLParser.DTML_TAG_SPEC) | (1 << DTMLParser.STRING_LITERAL) | (1 << DTMLParser.IDENTIFIER) | (1 << DTMLParser.UNEXPECTED_CHAR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






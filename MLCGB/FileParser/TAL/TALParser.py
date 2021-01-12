# Generated from TALParser.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("\u0084\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\7\2 \n\2\f\2\16\2#\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3+\n\3\3\3\3\3\3\4\3\4\5\4\61\n\4\3\5")
        buf.write("\5\5\64\n\5\3\5\3\5\3\6\3\6\3\6\7\6;\n\6\f\6\16\6>\13")
        buf.write("\6\3\7\3\7\5\7B\n\7\3\7\7\7E\n\7\f\7\16\7H\13\7\3\b\3")
        buf.write("\b\3\t\3\t\5\tN\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nW\n")
        buf.write("\n\3\13\3\13\3\13\3\13\7\13]\n\13\f\13\16\13`\13\13\3")
        buf.write("\13\5\13c\n\13\3\13\3\13\3\f\5\fh\n\f\3\f\5\fk\n\f\3\f")
        buf.write("\3\f\5\fo\n\f\3\r\5\rr\n\r\3\r\3\r\3\r\6\rw\n\r\r\r\16")
        buf.write("\rx\5\r{\n\r\3\16\6\16~\n\16\r\16\16\16\177\3\17\3\17")
        buf.write("\3\17\2\2\20\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\5\3")
        buf.write("\2\b\t\3\2\13\f\3\2\27\30\2\u008c\2!\3\2\2\2\4*\3\2\2")
        buf.write("\2\6\60\3\2\2\2\b\63\3\2\2\2\n\67\3\2\2\2\f?\3\2\2\2\16")
        buf.write("I\3\2\2\2\20K\3\2\2\2\22V\3\2\2\2\24X\3\2\2\2\26g\3\2")
        buf.write("\2\2\30z\3\2\2\2\32}\3\2\2\2\34\u0081\3\2\2\2\36 \5\4")
        buf.write("\3\2\37\36\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"")
        buf.write("$\3\2\2\2#!\3\2\2\2$%\7\2\2\3%\3\3\2\2\2&\'\7\5\2\2\'")
        buf.write("+\5\b\5\2()\7\6\2\2)+\5\6\4\2*&\3\2\2\2*(\3\2\2\2+,\3")
        buf.write("\2\2\2,-\7\7\2\2-\5\3\2\2\2.\61\5\f\7\2/\61\5\n\6\2\60")
        buf.write(".\3\2\2\2\60/\3\2\2\2\61\7\3\2\2\2\62\64\5\16\b\2\63\62")
        buf.write("\3\2\2\2\63\64\3\2\2\2\64\65\3\2\2\2\65\66\7\27\2\2\66")
        buf.write("\t\3\2\2\2\678\5\16\b\28<\5\34\17\29;\5\20\t\2:9\3\2\2")
        buf.write("\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\13\3\2\2\2><\3\2\2\2")
        buf.write("?F\5\34\17\2@B\7\b\2\2A@\3\2\2\2AB\3\2\2\2BC\3\2\2\2C")
        buf.write("E\5\20\t\2DA\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\r")
        buf.write("\3\2\2\2HF\3\2\2\2IJ\t\2\2\2J\17\3\2\2\2KM\5\22\n\2LN")
        buf.write("\5\24\13\2ML\3\2\2\2MN\3\2\2\2N\21\3\2\2\2OW\7\20\2\2")
        buf.write("PW\7\21\2\2QW\7\17\2\2RW\7\22\2\2SW\7\23\2\2TW\7\24\2")
        buf.write("\2UW\5\34\17\2VO\3\2\2\2VP\3\2\2\2VQ\3\2\2\2VR\3\2\2\2")
        buf.write("VS\3\2\2\2VT\3\2\2\2VU\3\2\2\2W\23\3\2\2\2XY\7\25\2\2")
        buf.write("Y^\5\26\f\2Z[\7\26\2\2[]\5\26\f\2\\Z\3\2\2\2]`\3\2\2\2")
        buf.write("^\\\3\2\2\2^_\3\2\2\2_b\3\2\2\2`^\3\2\2\2ac\7\26\2\2b")
        buf.write("a\3\2\2\2bc\3\2\2\2cd\3\2\2\2de\7\25\2\2e\25\3\2\2\2f")
        buf.write("h\5\34\17\2gf\3\2\2\2gh\3\2\2\2hj\3\2\2\2ik\7\n\2\2ji")
        buf.write("\3\2\2\2jk\3\2\2\2kl\3\2\2\2ln\5\30\r\2mo\7\r\2\2nm\3")
        buf.write("\2\2\2no\3\2\2\2o\27\3\2\2\2pr\t\3\2\2qp\3\2\2\2qr\3\2")
        buf.write("\2\2rs\3\2\2\2st\7\16\2\2t{\5\32\16\2uw\5\34\17\2vu\3")
        buf.write("\2\2\2wx\3\2\2\2xv\3\2\2\2xy\3\2\2\2y{\3\2\2\2zq\3\2\2")
        buf.write("\2zv\3\2\2\2{\31\3\2\2\2|~\5\34\17\2}|\3\2\2\2~\177\3")
        buf.write("\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\33\3\2\2\2")
        buf.write("\u0081\u0082\t\4\2\2\u0082\35\3\2\2\2\24!*\60\63<AFMV")
        buf.write("^bgjnqxz\177")
        return buf.getvalue()


class TALParser ( Parser ):

    grammarFileName = "TALParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'</'", "'<'", 
                     "'>'", "'tal:'", "'metal:'", "'not:'", "'python:'", 
                     "'string:'", "'|nothing'", "'context'", "'content='", 
                     "'define='", "'condition='", "'repeat='", "'define-macro='", 
                     "'use-macro='", "'\"'", "';'" ]

    symbolicNames = [ "<INVALID>", "WHITESPACE", "BLOCK_COMMENT", "TAG_OPEN_SLASH", 
                      "TAG_OPEN", "TAG_CLOSE", "TAL_TAG_KEY", "METAL_TAG_KEY", 
                      "NOT_KEY", "PYTHON_KEY", "STRING_KEY", "NOTHING_EXPR", 
                      "ZOPE_KEY", "ATTR_CONTENT", "ATTR_DEFINE", "ATTR_CONDITION", 
                      "ATTR_REPEAT", "ATTR_DEFINE_MACRO", "ATTR_USE_MACRO", 
                      "DQUOTA", "SEMICOLON", "IDENTIFIER", "UNEXPECTED_CHAR" ]

    RULE_parse = 0
    RULE_stmt = 1
    RULE_open_tag = 2
    RULE_close_tag = 3
    RULE_tal_tag = 4
    RULE_other_tag = 5
    RULE_tag_specifier = 6
    RULE_tag_attr = 7
    RULE_tag_attr_key = 8
    RULE_tag_attr_value = 9
    RULE_tag_attr_value_def = 10
    RULE_tag_attr_expr = 11
    RULE_function_ref = 12
    RULE_identifier = 13

    ruleNames =  [ "parse", "stmt", "open_tag", "close_tag", "tal_tag", 
                   "other_tag", "tag_specifier", "tag_attr", "tag_attr_key", 
                   "tag_attr_value", "tag_attr_value_def", "tag_attr_expr", 
                   "function_ref", "identifier" ]

    EOF = Token.EOF
    WHITESPACE=1
    BLOCK_COMMENT=2
    TAG_OPEN_SLASH=3
    TAG_OPEN=4
    TAG_CLOSE=5
    TAL_TAG_KEY=6
    METAL_TAG_KEY=7
    NOT_KEY=8
    PYTHON_KEY=9
    STRING_KEY=10
    NOTHING_EXPR=11
    ZOPE_KEY=12
    ATTR_CONTENT=13
    ATTR_DEFINE=14
    ATTR_CONDITION=15
    ATTR_REPEAT=16
    ATTR_DEFINE_MACRO=17
    ATTR_USE_MACRO=18
    DQUOTA=19
    SEMICOLON=20
    IDENTIFIER=21
    UNEXPECTED_CHAR=22

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
            return self.getToken(TALParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TALParser.StmtContext)
            else:
                return self.getTypedRuleContext(TALParser.StmtContext,i)


        def getRuleIndex(self):
            return TALParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)




    def parse(self):

        localctx = TALParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TALParser.TAG_OPEN_SLASH or _la==TALParser.TAG_OPEN:
                self.state = 28
                self.stmt()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(TALParser.EOF)
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

        def TAG_CLOSE(self):
            return self.getToken(TALParser.TAG_CLOSE, 0)

        def TAG_OPEN_SLASH(self):
            return self.getToken(TALParser.TAG_OPEN_SLASH, 0)

        def close_tag(self):
            return self.getTypedRuleContext(TALParser.Close_tagContext,0)


        def TAG_OPEN(self):
            return self.getToken(TALParser.TAG_OPEN, 0)

        def open_tag(self):
            return self.getTypedRuleContext(TALParser.Open_tagContext,0)


        def getRuleIndex(self):
            return TALParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = TALParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TALParser.TAG_OPEN_SLASH]:
                self.state = 36
                self.match(TALParser.TAG_OPEN_SLASH)
                self.state = 37
                self.close_tag()
                pass
            elif token in [TALParser.TAG_OPEN]:
                self.state = 38
                self.match(TALParser.TAG_OPEN)
                self.state = 39
                self.open_tag()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 42
            self.match(TALParser.TAG_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Open_tagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def other_tag(self):
            return self.getTypedRuleContext(TALParser.Other_tagContext,0)


        def tal_tag(self):
            return self.getTypedRuleContext(TALParser.Tal_tagContext,0)


        def getRuleIndex(self):
            return TALParser.RULE_open_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpen_tag" ):
                listener.enterOpen_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpen_tag" ):
                listener.exitOpen_tag(self)




    def open_tag(self):

        localctx = TALParser.Open_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_open_tag)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TALParser.IDENTIFIER, TALParser.UNEXPECTED_CHAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.other_tag()
                pass
            elif token in [TALParser.TAL_TAG_KEY, TALParser.METAL_TAG_KEY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.tal_tag()
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


    class Close_tagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TALParser.IDENTIFIER, 0)

        def tag_specifier(self):
            return self.getTypedRuleContext(TALParser.Tag_specifierContext,0)


        def getRuleIndex(self):
            return TALParser.RULE_close_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClose_tag" ):
                listener.enterClose_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClose_tag" ):
                listener.exitClose_tag(self)




    def close_tag(self):

        localctx = TALParser.Close_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_close_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TALParser.TAL_TAG_KEY or _la==TALParser.METAL_TAG_KEY:
                self.state = 48
                self.tag_specifier()


            self.state = 51
            self.match(TALParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tal_tagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tag_specifier(self):
            return self.getTypedRuleContext(TALParser.Tag_specifierContext,0)


        def identifier(self):
            return self.getTypedRuleContext(TALParser.IdentifierContext,0)


        def tag_attr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TALParser.Tag_attrContext)
            else:
                return self.getTypedRuleContext(TALParser.Tag_attrContext,i)


        def getRuleIndex(self):
            return TALParser.RULE_tal_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTal_tag" ):
                listener.enterTal_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTal_tag" ):
                listener.exitTal_tag(self)




    def tal_tag(self):

        localctx = TALParser.Tal_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tal_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.tag_specifier()
            self.state = 54
            self.identifier()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TALParser.ATTR_CONTENT) | (1 << TALParser.ATTR_DEFINE) | (1 << TALParser.ATTR_CONDITION) | (1 << TALParser.ATTR_REPEAT) | (1 << TALParser.ATTR_DEFINE_MACRO) | (1 << TALParser.ATTR_USE_MACRO) | (1 << TALParser.IDENTIFIER) | (1 << TALParser.UNEXPECTED_CHAR))) != 0):
                self.state = 55
                self.tag_attr()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Other_tagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(TALParser.IdentifierContext,0)


        def tag_attr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TALParser.Tag_attrContext)
            else:
                return self.getTypedRuleContext(TALParser.Tag_attrContext,i)


        def TAL_TAG_KEY(self, i:int=None):
            if i is None:
                return self.getTokens(TALParser.TAL_TAG_KEY)
            else:
                return self.getToken(TALParser.TAL_TAG_KEY, i)

        def getRuleIndex(self):
            return TALParser.RULE_other_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOther_tag" ):
                listener.enterOther_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOther_tag" ):
                listener.exitOther_tag(self)




    def other_tag(self):

        localctx = TALParser.Other_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_other_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.identifier()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TALParser.TAL_TAG_KEY) | (1 << TALParser.ATTR_CONTENT) | (1 << TALParser.ATTR_DEFINE) | (1 << TALParser.ATTR_CONDITION) | (1 << TALParser.ATTR_REPEAT) | (1 << TALParser.ATTR_DEFINE_MACRO) | (1 << TALParser.ATTR_USE_MACRO) | (1 << TALParser.IDENTIFIER) | (1 << TALParser.UNEXPECTED_CHAR))) != 0):
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TALParser.TAL_TAG_KEY:
                    self.state = 62
                    self.match(TALParser.TAL_TAG_KEY)


                self.state = 65
                self.tag_attr()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_specifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAL_TAG_KEY(self):
            return self.getToken(TALParser.TAL_TAG_KEY, 0)

        def METAL_TAG_KEY(self):
            return self.getToken(TALParser.METAL_TAG_KEY, 0)

        def getRuleIndex(self):
            return TALParser.RULE_tag_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag_specifier" ):
                listener.enterTag_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag_specifier" ):
                listener.exitTag_specifier(self)




    def tag_specifier(self):

        localctx = TALParser.Tag_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tag_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            _la = self._input.LA(1)
            if not(_la==TALParser.TAL_TAG_KEY or _la==TALParser.METAL_TAG_KEY):
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


    class Tag_attrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tag_attr_key(self):
            return self.getTypedRuleContext(TALParser.Tag_attr_keyContext,0)


        def tag_attr_value(self):
            return self.getTypedRuleContext(TALParser.Tag_attr_valueContext,0)


        def getRuleIndex(self):
            return TALParser.RULE_tag_attr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag_attr" ):
                listener.enterTag_attr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag_attr" ):
                listener.exitTag_attr(self)




    def tag_attr(self):

        localctx = TALParser.Tag_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tag_attr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.tag_attr_key()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TALParser.DQUOTA:
                self.state = 74
                self.tag_attr_value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_attr_keyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATTR_DEFINE(self):
            return self.getToken(TALParser.ATTR_DEFINE, 0)

        def ATTR_CONDITION(self):
            return self.getToken(TALParser.ATTR_CONDITION, 0)

        def ATTR_CONTENT(self):
            return self.getToken(TALParser.ATTR_CONTENT, 0)

        def ATTR_REPEAT(self):
            return self.getToken(TALParser.ATTR_REPEAT, 0)

        def ATTR_DEFINE_MACRO(self):
            return self.getToken(TALParser.ATTR_DEFINE_MACRO, 0)

        def ATTR_USE_MACRO(self):
            return self.getToken(TALParser.ATTR_USE_MACRO, 0)

        def identifier(self):
            return self.getTypedRuleContext(TALParser.IdentifierContext,0)


        def getRuleIndex(self):
            return TALParser.RULE_tag_attr_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag_attr_key" ):
                listener.enterTag_attr_key(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag_attr_key" ):
                listener.exitTag_attr_key(self)




    def tag_attr_key(self):

        localctx = TALParser.Tag_attr_keyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tag_attr_key)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TALParser.ATTR_DEFINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(TALParser.ATTR_DEFINE)
                pass
            elif token in [TALParser.ATTR_CONDITION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(TALParser.ATTR_CONDITION)
                pass
            elif token in [TALParser.ATTR_CONTENT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.match(TALParser.ATTR_CONTENT)
                pass
            elif token in [TALParser.ATTR_REPEAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 80
                self.match(TALParser.ATTR_REPEAT)
                pass
            elif token in [TALParser.ATTR_DEFINE_MACRO]:
                self.enterOuterAlt(localctx, 5)
                self.state = 81
                self.match(TALParser.ATTR_DEFINE_MACRO)
                pass
            elif token in [TALParser.ATTR_USE_MACRO]:
                self.enterOuterAlt(localctx, 6)
                self.state = 82
                self.match(TALParser.ATTR_USE_MACRO)
                pass
            elif token in [TALParser.IDENTIFIER, TALParser.UNEXPECTED_CHAR]:
                self.enterOuterAlt(localctx, 7)
                self.state = 83
                self.identifier()
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


    class Tag_attr_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DQUOTA(self, i:int=None):
            if i is None:
                return self.getTokens(TALParser.DQUOTA)
            else:
                return self.getToken(TALParser.DQUOTA, i)

        def tag_attr_value_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TALParser.Tag_attr_value_defContext)
            else:
                return self.getTypedRuleContext(TALParser.Tag_attr_value_defContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(TALParser.SEMICOLON)
            else:
                return self.getToken(TALParser.SEMICOLON, i)

        def getRuleIndex(self):
            return TALParser.RULE_tag_attr_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag_attr_value" ):
                listener.enterTag_attr_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag_attr_value" ):
                listener.exitTag_attr_value(self)




    def tag_attr_value(self):

        localctx = TALParser.Tag_attr_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tag_attr_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(TALParser.DQUOTA)
            self.state = 87
            self.tag_attr_value_def()
            self.state = 92
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 88
                    self.match(TALParser.SEMICOLON)
                    self.state = 89
                    self.tag_attr_value_def() 
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TALParser.SEMICOLON:
                self.state = 95
                self.match(TALParser.SEMICOLON)


            self.state = 98
            self.match(TALParser.DQUOTA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_attr_value_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tag_attr_expr(self):
            return self.getTypedRuleContext(TALParser.Tag_attr_exprContext,0)


        def identifier(self):
            return self.getTypedRuleContext(TALParser.IdentifierContext,0)


        def NOT_KEY(self):
            return self.getToken(TALParser.NOT_KEY, 0)

        def NOTHING_EXPR(self):
            return self.getToken(TALParser.NOTHING_EXPR, 0)

        def getRuleIndex(self):
            return TALParser.RULE_tag_attr_value_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag_attr_value_def" ):
                listener.enterTag_attr_value_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag_attr_value_def" ):
                listener.exitTag_attr_value_def(self)




    def tag_attr_value_def(self):

        localctx = TALParser.Tag_attr_value_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_tag_attr_value_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 100
                self.identifier()


            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TALParser.NOT_KEY:
                self.state = 103
                self.match(TALParser.NOT_KEY)


            self.state = 106
            self.tag_attr_expr()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TALParser.NOTHING_EXPR:
                self.state = 107
                self.match(TALParser.NOTHING_EXPR)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_attr_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZOPE_KEY(self):
            return self.getToken(TALParser.ZOPE_KEY, 0)

        def function_ref(self):
            return self.getTypedRuleContext(TALParser.Function_refContext,0)


        def PYTHON_KEY(self):
            return self.getToken(TALParser.PYTHON_KEY, 0)

        def STRING_KEY(self):
            return self.getToken(TALParser.STRING_KEY, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TALParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(TALParser.IdentifierContext,i)


        def getRuleIndex(self):
            return TALParser.RULE_tag_attr_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag_attr_expr" ):
                listener.enterTag_attr_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag_attr_expr" ):
                listener.exitTag_attr_expr(self)




    def tag_attr_expr(self):

        localctx = TALParser.Tag_attr_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_tag_attr_expr)
        self._la = 0 # Token type
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TALParser.PYTHON_KEY, TALParser.STRING_KEY, TALParser.ZOPE_KEY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TALParser.PYTHON_KEY or _la==TALParser.STRING_KEY:
                    self.state = 110
                    _la = self._input.LA(1)
                    if not(_la==TALParser.PYTHON_KEY or _la==TALParser.STRING_KEY):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 113
                self.match(TALParser.ZOPE_KEY)
                self.state = 114
                self.function_ref()
                pass
            elif token in [TALParser.IDENTIFIER, TALParser.UNEXPECTED_CHAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 116 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 115
                    self.identifier()
                    self.state = 118 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==TALParser.IDENTIFIER or _la==TALParser.UNEXPECTED_CHAR):
                        break

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


    class Function_refContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TALParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(TALParser.IdentifierContext,i)


        def getRuleIndex(self):
            return TALParser.RULE_function_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_ref" ):
                listener.enterFunction_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_ref" ):
                listener.exitFunction_ref(self)




    def function_ref(self):

        localctx = TALParser.Function_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_function_ref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 122
                self.identifier()
                self.state = 125 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==TALParser.IDENTIFIER or _la==TALParser.UNEXPECTED_CHAR):
                    break

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

        def IDENTIFIER(self):
            return self.getToken(TALParser.IDENTIFIER, 0)

        def UNEXPECTED_CHAR(self):
            return self.getToken(TALParser.UNEXPECTED_CHAR, 0)

        def getRuleIndex(self):
            return TALParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = TALParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            _la = self._input.LA(1)
            if not(_la==TALParser.IDENTIFIER or _la==TALParser.UNEXPECTED_CHAR):
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






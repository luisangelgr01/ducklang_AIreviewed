# Generated from ducklang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,39,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,3,0,18,8,0,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,1,1,1,
        1,1,1,2,1,2,3,2,31,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,
        8,0,1,1,0,3,4,36,0,10,1,0,0,0,2,19,1,0,0,0,4,30,1,0,0,0,6,32,1,0,
        0,0,8,36,1,0,0,0,10,11,5,1,0,0,11,12,5,5,0,0,12,13,3,8,4,0,13,14,
        5,6,0,0,14,17,3,2,1,0,15,16,5,2,0,0,16,18,3,2,1,0,17,15,1,0,0,0,
        17,18,1,0,0,0,18,1,1,0,0,0,19,23,5,7,0,0,20,22,3,4,2,0,21,20,1,0,
        0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,
        1,0,0,0,26,27,5,8,0,0,27,3,1,0,0,0,28,31,3,0,0,0,29,31,3,6,3,0,30,
        28,1,0,0,0,30,29,1,0,0,0,31,5,1,0,0,0,32,33,5,3,0,0,33,34,5,9,0,
        0,34,35,3,8,4,0,35,7,1,0,0,0,36,37,7,0,0,0,37,9,1,0,0,0,3,17,23,
        30
    ]

class ducklangParser ( Parser ):

    grammarFileName = "ducklang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "ID", "NUMBER", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "EQ", "WS" ]

    RULE_ifStatement = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_assignment = 3
    RULE_expression = 4

    ruleNames =  [ "ifStatement", "block", "statement", "assignment", "expression" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    ID=3
    NUMBER=4
    LPAREN=5
    RPAREN=6
    LBRACE=7
    RBRACE=8
    EQ=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ducklangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ducklangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ducklangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ducklangParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ducklangParser.BlockContext)
            else:
                return self.getTypedRuleContext(ducklangParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(ducklangParser.ELSE, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = ducklangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(ducklangParser.IF)
            self.state = 11
            self.match(ducklangParser.LPAREN)
            self.state = 12
            self.expression()
            self.state = 13
            self.match(ducklangParser.RPAREN)
            self.state = 14
            self.block()
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 15
                self.match(ducklangParser.ELSE)
                self.state = 16
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ducklangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ducklangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ducklangParser.StatementContext)
            else:
                return self.getTypedRuleContext(ducklangParser.StatementContext,i)


        def getRuleIndex(self):
            return ducklangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = ducklangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(ducklangParser.LBRACE)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==3:
                self.state = 20
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(ducklangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(ducklangParser.IfStatementContext,0)


        def assignment(self):
            return self.getTypedRuleContext(ducklangParser.AssignmentContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ducklangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.ifStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.assignment()
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ducklangParser.ID, 0)

        def EQ(self):
            return self.getToken(ducklangParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(ducklangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = ducklangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(ducklangParser.ID)
            self.state = 33
            self.match(ducklangParser.EQ)
            self.state = 34
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ducklangParser.ID, 0)

        def NUMBER(self):
            return self.getToken(ducklangParser.NUMBER, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = ducklangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
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






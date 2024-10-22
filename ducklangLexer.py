# Generated from ducklang.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,58,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        2,1,2,5,2,32,8,2,10,2,12,2,35,9,2,1,3,4,3,38,8,3,11,3,12,3,39,1,
        4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,4,9,53,8,9,11,9,12,9,54,
        1,9,1,9,0,0,10,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,1,0,
        4,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,1,0,48,57,
        3,0,9,10,13,13,32,32,60,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,
        1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,
        1,0,0,0,0,19,1,0,0,0,1,21,1,0,0,0,3,24,1,0,0,0,5,29,1,0,0,0,7,37,
        1,0,0,0,9,41,1,0,0,0,11,43,1,0,0,0,13,45,1,0,0,0,15,47,1,0,0,0,17,
        49,1,0,0,0,19,52,1,0,0,0,21,22,5,105,0,0,22,23,5,102,0,0,23,2,1,
        0,0,0,24,25,5,101,0,0,25,26,5,108,0,0,26,27,5,115,0,0,27,28,5,101,
        0,0,28,4,1,0,0,0,29,33,7,0,0,0,30,32,7,1,0,0,31,30,1,0,0,0,32,35,
        1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,6,1,0,0,0,35,33,1,0,0,0,36,
        38,7,2,0,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,
        0,40,8,1,0,0,0,41,42,5,40,0,0,42,10,1,0,0,0,43,44,5,41,0,0,44,12,
        1,0,0,0,45,46,5,123,0,0,46,14,1,0,0,0,47,48,5,125,0,0,48,16,1,0,
        0,0,49,50,5,61,0,0,50,18,1,0,0,0,51,53,7,3,0,0,52,51,1,0,0,0,53,
        54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,56,1,0,0,0,56,57,6,9,0,
        0,57,20,1,0,0,0,4,0,33,39,54,1,6,0,0
    ]

class ducklangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    ID = 3
    NUMBER = 4
    LPAREN = 5
    RPAREN = 6
    LBRACE = 7
    RBRACE = 8
    EQ = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'('", "')'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "ID", "NUMBER", "LPAREN", "RPAREN", "LBRACE", 
            "RBRACE", "EQ", "WS" ]

    ruleNames = [ "IF", "ELSE", "ID", "NUMBER", "LPAREN", "RPAREN", "LBRACE", 
                  "RBRACE", "EQ", "WS" ]

    grammarFileName = "ducklang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


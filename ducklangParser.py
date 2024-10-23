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
        4,1,33,277,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,1,1,1,3,1,86,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,95,8,3,
        1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,106,8,5,1,6,1,6,1,7,1,7,
        1,7,1,7,3,7,114,8,7,1,8,1,8,1,8,1,8,3,8,120,8,8,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,3,10,135,8,10,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,146,8,11,1,12,1,12,1,12,1,
        12,1,13,1,13,3,13,154,8,13,1,14,1,14,1,14,1,14,3,14,160,8,14,1,15,
        1,15,1,15,1,15,1,15,3,15,167,8,15,1,16,1,16,1,16,1,16,1,16,1,17,
        1,17,1,17,1,18,1,18,1,18,1,18,3,18,181,8,18,1,19,1,19,1,20,1,20,
        1,20,1,20,1,20,3,20,190,8,20,1,21,1,21,1,22,1,22,1,22,1,22,1,22,
        3,22,199,8,22,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,
        210,8,24,1,25,1,25,3,25,214,8,25,1,26,1,26,3,26,218,8,26,1,27,1,
        27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,3,29,233,
        8,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,
        1,31,1,31,1,32,1,32,3,32,251,8,32,1,33,1,33,1,33,1,33,1,33,3,33,
        258,8,33,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,
        3,35,271,8,35,1,36,1,36,3,36,275,8,36,1,36,0,0,37,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,0,5,1,0,5,6,1,0,25,28,1,0,29,30,1,0,31,32,
        1,0,15,16,263,0,74,1,0,0,0,2,85,1,0,0,0,4,87,1,0,0,0,6,94,1,0,0,
        0,8,96,1,0,0,0,10,105,1,0,0,0,12,107,1,0,0,0,14,113,1,0,0,0,16,119,
        1,0,0,0,18,121,1,0,0,0,20,134,1,0,0,0,22,145,1,0,0,0,24,147,1,0,
        0,0,26,153,1,0,0,0,28,159,1,0,0,0,30,166,1,0,0,0,32,168,1,0,0,0,
        34,173,1,0,0,0,36,180,1,0,0,0,38,182,1,0,0,0,40,189,1,0,0,0,42,191,
        1,0,0,0,44,198,1,0,0,0,46,200,1,0,0,0,48,209,1,0,0,0,50,213,1,0,
        0,0,52,217,1,0,0,0,54,219,1,0,0,0,56,221,1,0,0,0,58,232,1,0,0,0,
        60,234,1,0,0,0,62,242,1,0,0,0,64,250,1,0,0,0,66,257,1,0,0,0,68,259,
        1,0,0,0,70,270,1,0,0,0,72,274,1,0,0,0,74,75,5,1,0,0,75,76,5,13,0,
        0,76,77,5,17,0,0,77,78,3,2,1,0,78,79,3,14,7,0,79,80,5,2,0,0,80,81,
        3,24,12,0,81,82,5,3,0,0,82,1,1,0,0,0,83,86,1,0,0,0,84,86,3,4,2,0,
        85,83,1,0,0,0,85,84,1,0,0,0,86,3,1,0,0,0,87,88,5,4,0,0,88,89,3,6,
        3,0,89,5,1,0,0,0,90,95,3,8,4,0,91,92,3,8,4,0,92,93,3,6,3,0,93,95,
        1,0,0,0,94,90,1,0,0,0,94,91,1,0,0,0,95,7,1,0,0,0,96,97,3,10,5,0,
        97,98,5,19,0,0,98,99,3,12,6,0,99,100,5,17,0,0,100,9,1,0,0,0,101,
        106,5,13,0,0,102,103,5,13,0,0,103,104,5,18,0,0,104,106,3,10,5,0,
        105,101,1,0,0,0,105,102,1,0,0,0,106,11,1,0,0,0,107,108,7,0,0,0,108,
        13,1,0,0,0,109,114,1,0,0,0,110,111,3,16,8,0,111,112,3,14,7,0,112,
        114,1,0,0,0,113,109,1,0,0,0,113,110,1,0,0,0,114,15,1,0,0,0,115,120,
        3,18,9,0,116,117,3,18,9,0,117,118,3,16,8,0,118,120,1,0,0,0,119,115,
        1,0,0,0,119,116,1,0,0,0,120,17,1,0,0,0,121,122,5,12,0,0,122,123,
        5,13,0,0,123,124,5,22,0,0,124,125,3,20,10,0,125,126,5,23,0,0,126,
        127,5,20,0,0,127,128,3,2,1,0,128,129,3,24,12,0,129,130,5,21,0,0,
        130,131,5,17,0,0,131,19,1,0,0,0,132,135,1,0,0,0,133,135,3,22,11,
        0,134,132,1,0,0,0,134,133,1,0,0,0,135,21,1,0,0,0,136,137,5,13,0,
        0,137,138,5,19,0,0,138,146,3,12,6,0,139,140,5,13,0,0,140,141,5,19,
        0,0,141,142,3,12,6,0,142,143,5,18,0,0,143,144,3,22,11,0,144,146,
        1,0,0,0,145,136,1,0,0,0,145,139,1,0,0,0,146,23,1,0,0,0,147,148,5,
        20,0,0,148,149,3,26,13,0,149,150,5,21,0,0,150,25,1,0,0,0,151,154,
        1,0,0,0,152,154,3,28,14,0,153,151,1,0,0,0,153,152,1,0,0,0,154,27,
        1,0,0,0,155,160,3,30,15,0,156,157,3,30,15,0,157,158,3,28,14,0,158,
        160,1,0,0,0,159,155,1,0,0,0,159,156,1,0,0,0,160,29,1,0,0,0,161,167,
        3,32,16,0,162,167,3,56,28,0,163,167,3,60,30,0,164,167,3,62,31,0,
        165,167,3,68,34,0,166,161,1,0,0,0,166,162,1,0,0,0,166,163,1,0,0,
        0,166,164,1,0,0,0,166,165,1,0,0,0,167,31,1,0,0,0,168,169,5,13,0,
        0,169,170,5,24,0,0,170,171,3,34,17,0,171,172,5,17,0,0,172,33,1,0,
        0,0,173,174,3,40,20,0,174,175,3,36,18,0,175,35,1,0,0,0,176,181,1,
        0,0,0,177,178,3,38,19,0,178,179,3,40,20,0,179,181,1,0,0,0,180,176,
        1,0,0,0,180,177,1,0,0,0,181,37,1,0,0,0,182,183,7,1,0,0,183,39,1,
        0,0,0,184,190,3,44,22,0,185,186,3,44,22,0,186,187,3,42,21,0,187,
        188,3,40,20,0,188,190,1,0,0,0,189,184,1,0,0,0,189,185,1,0,0,0,190,
        41,1,0,0,0,191,192,7,2,0,0,192,43,1,0,0,0,193,199,3,48,24,0,194,
        195,3,48,24,0,195,196,3,46,23,0,196,197,3,44,22,0,197,199,1,0,0,
        0,198,193,1,0,0,0,198,194,1,0,0,0,199,45,1,0,0,0,200,201,7,3,0,0,
        201,47,1,0,0,0,202,203,5,22,0,0,203,204,3,34,17,0,204,205,5,23,0,
        0,205,210,1,0,0,0,206,207,3,50,25,0,207,208,3,52,26,0,208,210,1,
        0,0,0,209,202,1,0,0,0,209,206,1,0,0,0,210,49,1,0,0,0,211,214,1,0,
        0,0,212,214,3,42,21,0,213,211,1,0,0,0,213,212,1,0,0,0,214,51,1,0,
        0,0,215,218,5,13,0,0,216,218,3,54,27,0,217,215,1,0,0,0,217,216,1,
        0,0,0,218,53,1,0,0,0,219,220,7,4,0,0,220,55,1,0,0,0,221,222,5,10,
        0,0,222,223,5,22,0,0,223,224,3,34,17,0,224,225,5,23,0,0,225,226,
        3,24,12,0,226,227,3,58,29,0,227,228,5,17,0,0,228,57,1,0,0,0,229,
        233,1,0,0,0,230,231,5,11,0,0,231,233,3,24,12,0,232,229,1,0,0,0,232,
        230,1,0,0,0,233,59,1,0,0,0,234,235,5,8,0,0,235,236,5,22,0,0,236,
        237,3,34,17,0,237,238,5,23,0,0,238,239,5,9,0,0,239,240,3,24,12,0,
        240,241,5,17,0,0,241,61,1,0,0,0,242,243,5,13,0,0,243,244,5,22,0,
        0,244,245,3,64,32,0,245,246,5,23,0,0,246,247,5,17,0,0,247,63,1,0,
        0,0,248,251,1,0,0,0,249,251,3,66,33,0,250,248,1,0,0,0,250,249,1,
        0,0,0,251,65,1,0,0,0,252,258,3,34,17,0,253,254,3,34,17,0,254,255,
        5,18,0,0,255,256,3,66,33,0,256,258,1,0,0,0,257,252,1,0,0,0,257,253,
        1,0,0,0,258,67,1,0,0,0,259,260,5,7,0,0,260,261,5,22,0,0,261,262,
        3,70,35,0,262,263,5,23,0,0,263,264,5,17,0,0,264,69,1,0,0,0,265,271,
        3,72,36,0,266,267,3,72,36,0,267,268,5,18,0,0,268,269,3,70,35,0,269,
        271,1,0,0,0,270,265,1,0,0,0,270,266,1,0,0,0,271,71,1,0,0,0,272,275,
        3,34,17,0,273,275,5,14,0,0,274,272,1,0,0,0,274,273,1,0,0,0,275,73,
        1,0,0,0,21,85,94,105,113,119,134,145,153,159,166,180,189,198,209,
        213,217,232,250,257,270,274
    ]

class ducklangParser ( Parser ):

    grammarFileName = "ducklang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'programa'", "'inicio'", "'fin'", "'vars'", 
                     "'entero'", "'flotante'", "'escribe'", "'mientras'", 
                     "'haz'", "'si'", "'sino'", "'nula'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'", "','", "':'", "'{'", 
                     "'}'", "'('", "')'", "'='", "'>'", "'<'", "'!='", "'=='", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "PR_PROGRAMA", "PR_INICIO", "PR_FIN", 
                      "PR_VARS", "PR_ENTERO", "PR_FLOTANTE", "PR_ESCRIBE", 
                      "PR_MIENTRAS", "PR_HAZ", "PR_SI", "PR_SINO", "PR_NULA", 
                      "ID", "LETRERO", "CTE_ENT", "CTE_FLOT", "DEL_SEMICOLON", 
                      "DEL_COMA", "DEL_COLON", "LLAVE_OPEN", "LLAVE_CLOSE", 
                      "PARENTESIS_OPEN", "PARENTESIS_CLOSE", "ASIGNACION", 
                      "COMP_GREATER", "COMP_LESS", "COMP_NOTEQUAL", "COMP_EQUAL", 
                      "OP_PLUS", "OP_MINUS", "OP_MULTIPLY", "OP_DIVIDE", 
                      "WS" ]

    RULE_programa = 0
    RULE_pvars = 1
    RULE_vars = 2
    RULE_vidtipo = 3
    RULE_vtipo = 4
    RULE_vid = 5
    RULE_tipo = 6
    RULE_ppfuncs = 7
    RULE_pfuncs = 8
    RULE_funcs = 9
    RULE_fidtipo = 10
    RULE_fid = 11
    RULE_cuerpo = 12
    RULE_ccestatuto = 13
    RULE_cestatuto = 14
    RULE_estatuto = 15
    RULE_asigna = 16
    RULE_expresion = 17
    RULE_eexp = 18
    RULE_comp = 19
    RULE_exp = 20
    RULE_sign = 21
    RULE_termino = 22
    RULE_op = 23
    RULE_factor = 24
    RULE_fsign = 25
    RULE_faid = 26
    RULE_cte = 27
    RULE_condicion = 28
    RULE_csino = 29
    RULE_ciclo = 30
    RULE_llamada = 31
    RULE_llexpresion = 32
    RULE_lexpresion = 33
    RULE_imprime = 34
    RULE_icont = 35
    RULE_cont = 36

    ruleNames =  [ "programa", "pvars", "vars", "vidtipo", "vtipo", "vid", 
                   "tipo", "ppfuncs", "pfuncs", "funcs", "fidtipo", "fid", 
                   "cuerpo", "ccestatuto", "cestatuto", "estatuto", "asigna", 
                   "expresion", "eexp", "comp", "exp", "sign", "termino", 
                   "op", "factor", "fsign", "faid", "cte", "condicion", 
                   "csino", "ciclo", "llamada", "llexpresion", "lexpresion", 
                   "imprime", "icont", "cont" ]

    EOF = Token.EOF
    PR_PROGRAMA=1
    PR_INICIO=2
    PR_FIN=3
    PR_VARS=4
    PR_ENTERO=5
    PR_FLOTANTE=6
    PR_ESCRIBE=7
    PR_MIENTRAS=8
    PR_HAZ=9
    PR_SI=10
    PR_SINO=11
    PR_NULA=12
    ID=13
    LETRERO=14
    CTE_ENT=15
    CTE_FLOT=16
    DEL_SEMICOLON=17
    DEL_COMA=18
    DEL_COLON=19
    LLAVE_OPEN=20
    LLAVE_CLOSE=21
    PARENTESIS_OPEN=22
    PARENTESIS_CLOSE=23
    ASIGNACION=24
    COMP_GREATER=25
    COMP_LESS=26
    COMP_NOTEQUAL=27
    COMP_EQUAL=28
    OP_PLUS=29
    OP_MINUS=30
    OP_MULTIPLY=31
    OP_DIVIDE=32
    WS=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PR_PROGRAMA(self):
            return self.getToken(ducklangParser.PR_PROGRAMA, 0)

        def ID(self):
            return self.getToken(ducklangParser.ID, 0)

        def DEL_SEMICOLON(self):
            return self.getToken(ducklangParser.DEL_SEMICOLON, 0)

        def pvars(self):
            return self.getTypedRuleContext(ducklangParser.PvarsContext,0)


        def ppfuncs(self):
            return self.getTypedRuleContext(ducklangParser.PpfuncsContext,0)


        def PR_INICIO(self):
            return self.getToken(ducklangParser.PR_INICIO, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(ducklangParser.CuerpoContext,0)


        def PR_FIN(self):
            return self.getToken(ducklangParser.PR_FIN, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = ducklangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(ducklangParser.PR_PROGRAMA)
            self.state = 75
            self.match(ducklangParser.ID)
            self.state = 76
            self.match(ducklangParser.DEL_SEMICOLON)
            self.state = 77
            self.pvars()
            self.state = 78
            self.ppfuncs()
            self.state = 79
            self.match(ducklangParser.PR_INICIO)
            self.state = 80
            self.cuerpo()
            self.state = 81
            self.match(ducklangParser.PR_FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PvarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_(self):
            return self.getTypedRuleContext(ducklangParser.VarsContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_pvars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPvars" ):
                listener.enterPvars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPvars" ):
                listener.exitPvars(self)




    def pvars(self):

        localctx = ducklangParser.PvarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pvars)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 12, 20]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.vars_()
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


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PR_VARS(self):
            return self.getToken(ducklangParser.PR_VARS, 0)

        def vidtipo(self):
            return self.getTypedRuleContext(ducklangParser.VidtipoContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)




    def vars_(self):

        localctx = ducklangParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(ducklangParser.PR_VARS)
            self.state = 88
            self.vidtipo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VidtipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vtipo(self):
            return self.getTypedRuleContext(ducklangParser.VtipoContext,0)


        def vidtipo(self):
            return self.getTypedRuleContext(ducklangParser.VidtipoContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_vidtipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVidtipo" ):
                listener.enterVidtipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVidtipo" ):
                listener.exitVidtipo(self)




    def vidtipo(self):

        localctx = ducklangParser.VidtipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vidtipo)
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.vtipo()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.vtipo()
                self.state = 92
                self.vidtipo()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VtipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vid(self):
            return self.getTypedRuleContext(ducklangParser.VidContext,0)


        def DEL_COLON(self):
            return self.getToken(ducklangParser.DEL_COLON, 0)

        def tipo(self):
            return self.getTypedRuleContext(ducklangParser.TipoContext,0)


        def DEL_SEMICOLON(self):
            return self.getToken(ducklangParser.DEL_SEMICOLON, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_vtipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVtipo" ):
                listener.enterVtipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVtipo" ):
                listener.exitVtipo(self)




    def vtipo(self):

        localctx = ducklangParser.VtipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vtipo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.vid()
            self.state = 97
            self.match(ducklangParser.DEL_COLON)
            self.state = 98
            self.tipo()
            self.state = 99
            self.match(ducklangParser.DEL_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ducklangParser.ID, 0)

        def DEL_COMA(self):
            return self.getToken(ducklangParser.DEL_COMA, 0)

        def vid(self):
            return self.getTypedRuleContext(ducklangParser.VidContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_vid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVid" ):
                listener.enterVid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVid" ):
                listener.exitVid(self)




    def vid(self):

        localctx = ducklangParser.VidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vid)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(ducklangParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(ducklangParser.ID)
                self.state = 103
                self.match(ducklangParser.DEL_COMA)
                self.state = 104
                self.vid()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PR_ENTERO(self):
            return self.getToken(ducklangParser.PR_ENTERO, 0)

        def PR_FLOTANTE(self):
            return self.getToken(ducklangParser.PR_FLOTANTE, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = ducklangParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
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


    class PpfuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pfuncs(self):
            return self.getTypedRuleContext(ducklangParser.PfuncsContext,0)


        def ppfuncs(self):
            return self.getTypedRuleContext(ducklangParser.PpfuncsContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_ppfuncs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPpfuncs" ):
                listener.enterPpfuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPpfuncs" ):
                listener.exitPpfuncs(self)




    def ppfuncs(self):

        localctx = ducklangParser.PpfuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ppfuncs)
        try:
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.pfuncs()
                self.state = 111
                self.ppfuncs()
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


    class PfuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcs(self):
            return self.getTypedRuleContext(ducklangParser.FuncsContext,0)


        def pfuncs(self):
            return self.getTypedRuleContext(ducklangParser.PfuncsContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_pfuncs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPfuncs" ):
                listener.enterPfuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPfuncs" ):
                listener.exitPfuncs(self)




    def pfuncs(self):

        localctx = ducklangParser.PfuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pfuncs)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.funcs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.funcs()
                self.state = 117
                self.pfuncs()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PR_NULA(self):
            return self.getToken(ducklangParser.PR_NULA, 0)

        def ID(self):
            return self.getToken(ducklangParser.ID, 0)

        def PARENTESIS_OPEN(self):
            return self.getToken(ducklangParser.PARENTESIS_OPEN, 0)

        def fidtipo(self):
            return self.getTypedRuleContext(ducklangParser.FidtipoContext,0)


        def PARENTESIS_CLOSE(self):
            return self.getToken(ducklangParser.PARENTESIS_CLOSE, 0)

        def LLAVE_OPEN(self):
            return self.getToken(ducklangParser.LLAVE_OPEN, 0)

        def pvars(self):
            return self.getTypedRuleContext(ducklangParser.PvarsContext,0)


        def cuerpo(self):
            return self.getTypedRuleContext(ducklangParser.CuerpoContext,0)


        def LLAVE_CLOSE(self):
            return self.getToken(ducklangParser.LLAVE_CLOSE, 0)

        def DEL_SEMICOLON(self):
            return self.getToken(ducklangParser.DEL_SEMICOLON, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs" ):
                listener.enterFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs" ):
                listener.exitFuncs(self)




    def funcs(self):

        localctx = ducklangParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(ducklangParser.PR_NULA)
            self.state = 122
            self.match(ducklangParser.ID)
            self.state = 123
            self.match(ducklangParser.PARENTESIS_OPEN)
            self.state = 124
            self.fidtipo()
            self.state = 125
            self.match(ducklangParser.PARENTESIS_CLOSE)
            self.state = 126
            self.match(ducklangParser.LLAVE_OPEN)
            self.state = 127
            self.pvars()
            self.state = 128
            self.cuerpo()
            self.state = 129
            self.match(ducklangParser.LLAVE_CLOSE)
            self.state = 130
            self.match(ducklangParser.DEL_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FidtipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fid(self):
            return self.getTypedRuleContext(ducklangParser.FidContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_fidtipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFidtipo" ):
                listener.enterFidtipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFidtipo" ):
                listener.exitFidtipo(self)




    def fidtipo(self):

        localctx = ducklangParser.FidtipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_fidtipo)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.fid()
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


    class FidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ducklangParser.ID, 0)

        def DEL_COLON(self):
            return self.getToken(ducklangParser.DEL_COLON, 0)

        def tipo(self):
            return self.getTypedRuleContext(ducklangParser.TipoContext,0)


        def DEL_COMA(self):
            return self.getToken(ducklangParser.DEL_COMA, 0)

        def fid(self):
            return self.getTypedRuleContext(ducklangParser.FidContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_fid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFid" ):
                listener.enterFid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFid" ):
                listener.exitFid(self)




    def fid(self):

        localctx = ducklangParser.FidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_fid)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(ducklangParser.ID)
                self.state = 137
                self.match(ducklangParser.DEL_COLON)
                self.state = 138
                self.tipo()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.match(ducklangParser.ID)
                self.state = 140
                self.match(ducklangParser.DEL_COLON)
                self.state = 141
                self.tipo()
                self.state = 142
                self.match(ducklangParser.DEL_COMA)
                self.state = 143
                self.fid()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CuerpoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVE_OPEN(self):
            return self.getToken(ducklangParser.LLAVE_OPEN, 0)

        def ccestatuto(self):
            return self.getTypedRuleContext(ducklangParser.CcestatutoContext,0)


        def LLAVE_CLOSE(self):
            return self.getToken(ducklangParser.LLAVE_CLOSE, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_cuerpo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCuerpo" ):
                listener.enterCuerpo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCuerpo" ):
                listener.exitCuerpo(self)




    def cuerpo(self):

        localctx = ducklangParser.CuerpoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_cuerpo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(ducklangParser.LLAVE_OPEN)
            self.state = 148
            self.ccestatuto()
            self.state = 149
            self.match(ducklangParser.LLAVE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CcestatutoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cestatuto(self):
            return self.getTypedRuleContext(ducklangParser.CestatutoContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_ccestatuto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCcestatuto" ):
                listener.enterCcestatuto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCcestatuto" ):
                listener.exitCcestatuto(self)




    def ccestatuto(self):

        localctx = ducklangParser.CcestatutoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ccestatuto)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [7, 8, 10, 13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.cestatuto()
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


    class CestatutoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def estatuto(self):
            return self.getTypedRuleContext(ducklangParser.EstatutoContext,0)


        def cestatuto(self):
            return self.getTypedRuleContext(ducklangParser.CestatutoContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_cestatuto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCestatuto" ):
                listener.enterCestatuto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCestatuto" ):
                listener.exitCestatuto(self)




    def cestatuto(self):

        localctx = ducklangParser.CestatutoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_cestatuto)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.estatuto()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.estatuto()
                self.state = 157
                self.cestatuto()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstatutoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asigna(self):
            return self.getTypedRuleContext(ducklangParser.AsignaContext,0)


        def condicion(self):
            return self.getTypedRuleContext(ducklangParser.CondicionContext,0)


        def ciclo(self):
            return self.getTypedRuleContext(ducklangParser.CicloContext,0)


        def llamada(self):
            return self.getTypedRuleContext(ducklangParser.LlamadaContext,0)


        def imprime(self):
            return self.getTypedRuleContext(ducklangParser.ImprimeContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_estatuto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstatuto" ):
                listener.enterEstatuto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstatuto" ):
                listener.exitEstatuto(self)




    def estatuto(self):

        localctx = ducklangParser.EstatutoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_estatuto)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.asigna()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.condicion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 163
                self.ciclo()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 164
                self.llamada()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 165
                self.imprime()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ducklangParser.ID, 0)

        def ASIGNACION(self):
            return self.getToken(ducklangParser.ASIGNACION, 0)

        def expresion(self):
            return self.getTypedRuleContext(ducklangParser.ExpresionContext,0)


        def DEL_SEMICOLON(self):
            return self.getToken(ducklangParser.DEL_SEMICOLON, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_asigna

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsigna" ):
                listener.enterAsigna(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsigna" ):
                listener.exitAsigna(self)




    def asigna(self):

        localctx = ducklangParser.AsignaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_asigna)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ducklangParser.ID)
            self.state = 169
            self.match(ducklangParser.ASIGNACION)
            self.state = 170
            self.expresion()
            self.state = 171
            self.match(ducklangParser.DEL_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(ducklangParser.ExpContext,0)


        def eexp(self):
            return self.getTypedRuleContext(ducklangParser.EexpContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = ducklangParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.exp()
            self.state = 174
            self.eexp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comp(self):
            return self.getTypedRuleContext(ducklangParser.CompContext,0)


        def exp(self):
            return self.getTypedRuleContext(ducklangParser.ExpContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_eexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEexp" ):
                listener.enterEexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEexp" ):
                listener.exitEexp(self)




    def eexp(self):

        localctx = ducklangParser.EexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_eexp)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 23]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [25, 26, 27, 28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.comp()
                self.state = 178
                self.exp()
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


    class CompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMP_GREATER(self):
            return self.getToken(ducklangParser.COMP_GREATER, 0)

        def COMP_LESS(self):
            return self.getToken(ducklangParser.COMP_LESS, 0)

        def COMP_NOTEQUAL(self):
            return self.getToken(ducklangParser.COMP_NOTEQUAL, 0)

        def COMP_EQUAL(self):
            return self.getToken(ducklangParser.COMP_EQUAL, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)




    def comp(self):

        localctx = ducklangParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_comp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0)):
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


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(ducklangParser.TerminoContext,0)


        def sign(self):
            return self.getTypedRuleContext(ducklangParser.SignContext,0)


        def exp(self):
            return self.getTypedRuleContext(ducklangParser.ExpContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = ducklangParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exp)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.termino()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.termino()
                self.state = 186
                self.sign()
                self.state = 187
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_PLUS(self):
            return self.getToken(ducklangParser.OP_PLUS, 0)

        def OP_MINUS(self):
            return self.getToken(ducklangParser.OP_MINUS, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_sign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSign" ):
                listener.enterSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSign" ):
                listener.exitSign(self)




    def sign(self):

        localctx = ducklangParser.SignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_sign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
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


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(ducklangParser.FactorContext,0)


        def op(self):
            return self.getTypedRuleContext(ducklangParser.OpContext,0)


        def termino(self):
            return self.getTypedRuleContext(ducklangParser.TerminoContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = ducklangParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_termino)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.factor()
                self.state = 195
                self.op()
                self.state = 196
                self.termino()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MULTIPLY(self):
            return self.getToken(ducklangParser.OP_MULTIPLY, 0)

        def OP_DIVIDE(self):
            return self.getToken(ducklangParser.OP_DIVIDE, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)




    def op(self):

        localctx = ducklangParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
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


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENTESIS_OPEN(self):
            return self.getToken(ducklangParser.PARENTESIS_OPEN, 0)

        def expresion(self):
            return self.getTypedRuleContext(ducklangParser.ExpresionContext,0)


        def PARENTESIS_CLOSE(self):
            return self.getToken(ducklangParser.PARENTESIS_CLOSE, 0)

        def fsign(self):
            return self.getTypedRuleContext(ducklangParser.FsignContext,0)


        def faid(self):
            return self.getTypedRuleContext(ducklangParser.FaidContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = ducklangParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_factor)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(ducklangParser.PARENTESIS_OPEN)
                self.state = 203
                self.expresion()
                self.state = 204
                self.match(ducklangParser.PARENTESIS_CLOSE)
                pass
            elif token in [13, 15, 16, 29, 30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.fsign()
                self.state = 207
                self.faid()
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


    class FsignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sign(self):
            return self.getTypedRuleContext(ducklangParser.SignContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_fsign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFsign" ):
                listener.enterFsign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFsign" ):
                listener.exitFsign(self)




    def fsign(self):

        localctx = ducklangParser.FsignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_fsign)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 15, 16]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [29, 30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.sign()
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


    class FaidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ducklangParser.ID, 0)

        def cte(self):
            return self.getTypedRuleContext(ducklangParser.CteContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_faid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFaid" ):
                listener.enterFaid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFaid" ):
                listener.exitFaid(self)




    def faid(self):

        localctx = ducklangParser.FaidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_faid)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(ducklangParser.ID)
                pass
            elif token in [15, 16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.cte()
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


    class CteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CTE_ENT(self):
            return self.getToken(ducklangParser.CTE_ENT, 0)

        def CTE_FLOT(self):
            return self.getToken(ducklangParser.CTE_FLOT, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCte" ):
                listener.enterCte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCte" ):
                listener.exitCte(self)




    def cte(self):

        localctx = ducklangParser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
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


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PR_SI(self):
            return self.getToken(ducklangParser.PR_SI, 0)

        def PARENTESIS_OPEN(self):
            return self.getToken(ducklangParser.PARENTESIS_OPEN, 0)

        def expresion(self):
            return self.getTypedRuleContext(ducklangParser.ExpresionContext,0)


        def PARENTESIS_CLOSE(self):
            return self.getToken(ducklangParser.PARENTESIS_CLOSE, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(ducklangParser.CuerpoContext,0)


        def csino(self):
            return self.getTypedRuleContext(ducklangParser.CsinoContext,0)


        def DEL_SEMICOLON(self):
            return self.getToken(ducklangParser.DEL_SEMICOLON, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)




    def condicion(self):

        localctx = ducklangParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(ducklangParser.PR_SI)
            self.state = 222
            self.match(ducklangParser.PARENTESIS_OPEN)
            self.state = 223
            self.expresion()
            self.state = 224
            self.match(ducklangParser.PARENTESIS_CLOSE)
            self.state = 225
            self.cuerpo()
            self.state = 226
            self.csino()
            self.state = 227
            self.match(ducklangParser.DEL_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CsinoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PR_SINO(self):
            return self.getToken(ducklangParser.PR_SINO, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(ducklangParser.CuerpoContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_csino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCsino" ):
                listener.enterCsino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCsino" ):
                listener.exitCsino(self)




    def csino(self):

        localctx = ducklangParser.CsinoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_csino)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.match(ducklangParser.PR_SINO)
                self.state = 231
                self.cuerpo()
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


    class CicloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PR_MIENTRAS(self):
            return self.getToken(ducklangParser.PR_MIENTRAS, 0)

        def PARENTESIS_OPEN(self):
            return self.getToken(ducklangParser.PARENTESIS_OPEN, 0)

        def expresion(self):
            return self.getTypedRuleContext(ducklangParser.ExpresionContext,0)


        def PARENTESIS_CLOSE(self):
            return self.getToken(ducklangParser.PARENTESIS_CLOSE, 0)

        def PR_HAZ(self):
            return self.getToken(ducklangParser.PR_HAZ, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(ducklangParser.CuerpoContext,0)


        def DEL_SEMICOLON(self):
            return self.getToken(ducklangParser.DEL_SEMICOLON, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_ciclo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCiclo" ):
                listener.enterCiclo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCiclo" ):
                listener.exitCiclo(self)




    def ciclo(self):

        localctx = ducklangParser.CicloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_ciclo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(ducklangParser.PR_MIENTRAS)
            self.state = 235
            self.match(ducklangParser.PARENTESIS_OPEN)
            self.state = 236
            self.expresion()
            self.state = 237
            self.match(ducklangParser.PARENTESIS_CLOSE)
            self.state = 238
            self.match(ducklangParser.PR_HAZ)
            self.state = 239
            self.cuerpo()
            self.state = 240
            self.match(ducklangParser.DEL_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ducklangParser.ID, 0)

        def PARENTESIS_OPEN(self):
            return self.getToken(ducklangParser.PARENTESIS_OPEN, 0)

        def llexpresion(self):
            return self.getTypedRuleContext(ducklangParser.LlexpresionContext,0)


        def PARENTESIS_CLOSE(self):
            return self.getToken(ducklangParser.PARENTESIS_CLOSE, 0)

        def DEL_SEMICOLON(self):
            return self.getToken(ducklangParser.DEL_SEMICOLON, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_llamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada" ):
                listener.enterLlamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada" ):
                listener.exitLlamada(self)




    def llamada(self):

        localctx = ducklangParser.LlamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_llamada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(ducklangParser.ID)
            self.state = 243
            self.match(ducklangParser.PARENTESIS_OPEN)
            self.state = 244
            self.llexpresion()
            self.state = 245
            self.match(ducklangParser.PARENTESIS_CLOSE)
            self.state = 246
            self.match(ducklangParser.DEL_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlexpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexpresion(self):
            return self.getTypedRuleContext(ducklangParser.LexpresionContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_llexpresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlexpresion" ):
                listener.enterLlexpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlexpresion" ):
                listener.exitLlexpresion(self)




    def llexpresion(self):

        localctx = ducklangParser.LlexpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_llexpresion)
        try:
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [13, 15, 16, 22, 29, 30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.lexpresion()
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


    class LexpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(ducklangParser.ExpresionContext,0)


        def DEL_COMA(self):
            return self.getToken(ducklangParser.DEL_COMA, 0)

        def lexpresion(self):
            return self.getTypedRuleContext(ducklangParser.LexpresionContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_lexpresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexpresion" ):
                listener.enterLexpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexpresion" ):
                listener.exitLexpresion(self)




    def lexpresion(self):

        localctx = ducklangParser.LexpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_lexpresion)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.expresion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.expresion()
                self.state = 254
                self.match(ducklangParser.DEL_COMA)
                self.state = 255
                self.lexpresion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PR_ESCRIBE(self):
            return self.getToken(ducklangParser.PR_ESCRIBE, 0)

        def PARENTESIS_OPEN(self):
            return self.getToken(ducklangParser.PARENTESIS_OPEN, 0)

        def icont(self):
            return self.getTypedRuleContext(ducklangParser.IcontContext,0)


        def PARENTESIS_CLOSE(self):
            return self.getToken(ducklangParser.PARENTESIS_CLOSE, 0)

        def DEL_SEMICOLON(self):
            return self.getToken(ducklangParser.DEL_SEMICOLON, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_imprime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprime" ):
                listener.enterImprime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprime" ):
                listener.exitImprime(self)




    def imprime(self):

        localctx = ducklangParser.ImprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_imprime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(ducklangParser.PR_ESCRIBE)
            self.state = 260
            self.match(ducklangParser.PARENTESIS_OPEN)
            self.state = 261
            self.icont()
            self.state = 262
            self.match(ducklangParser.PARENTESIS_CLOSE)
            self.state = 263
            self.match(ducklangParser.DEL_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IcontContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cont(self):
            return self.getTypedRuleContext(ducklangParser.ContContext,0)


        def DEL_COMA(self):
            return self.getToken(ducklangParser.DEL_COMA, 0)

        def icont(self):
            return self.getTypedRuleContext(ducklangParser.IcontContext,0)


        def getRuleIndex(self):
            return ducklangParser.RULE_icont

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIcont" ):
                listener.enterIcont(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIcont" ):
                listener.exitIcont(self)




    def icont(self):

        localctx = ducklangParser.IcontContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_icont)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.cont()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.cont()
                self.state = 267
                self.match(ducklangParser.DEL_COMA)
                self.state = 268
                self.icont()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(ducklangParser.ExpresionContext,0)


        def LETRERO(self):
            return self.getToken(ducklangParser.LETRERO, 0)

        def getRuleIndex(self):
            return ducklangParser.RULE_cont

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCont" ):
                listener.enterCont(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCont" ):
                listener.exitCont(self)




    def cont(self):

        localctx = ducklangParser.ContContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_cont)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 15, 16, 22, 29, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.expresion()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.match(ducklangParser.LETRERO)
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






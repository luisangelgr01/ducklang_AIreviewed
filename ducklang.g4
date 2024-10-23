grammar ducklang;

//tokens (analizador léxico)
PR_PROGRAMA     : 'programa';
PR_INICIO       : 'inicio';
PR_FIN          : 'fin';
PR_VARS         : 'vars';
PR_ENTERO       : 'entero';
PR_FLOTANTE     : 'flotante';
PR_ESCRIBE      : 'escribe';
PR_MIENTRAS     : 'mientras';
PR_HAZ          : 'haz';
PR_SI           : 'si';
PR_SINO         : 'sino';
PR_NULA         : 'nula';
ID              : [a-z]+;
LETRERO         : '"' ( ~["\\] | '\\' . )* '"';
CTE_ENT         : [0-9]+;
CTE_FLOT        : [0-9]+ '.' [0-9]+;
DEL_SEMICOLON   : ';';
DEL_COMA        : ',';
DEL_COLON       : ':';
LLAVE_OPEN      : '{';
LLAVE_CLOSE     : '}';
PARENTESIS_OPEN : '(';
PARENTESIS_CLOSE: ')';
ASIGNACION      : '=';
COMP_GREATER    : '>';
COMP_LESS       : '<';
COMP_NOTEQUAL   : '!=';
COMP_EQUAL      : '==';
OP_PLUS         : '+';
OP_MINUS        : '-';
OP_MULTIPLY     : '*';
OP_DIVIDE       : '/';
WS              : [ \t\r\n]+ -> skip;  //saltar espacios

//gramática (analizador sintáctico)
programa
    : PR_PROGRAMA ID DEL_SEMICOLON pvars ppfuncs PR_INICIO cuerpo PR_FIN;
pvars
    : 
    | vars;
vars
    : PR_VARS vidtipo;
vidtipo
    : vtipo
    | vtipo vidtipo;
vtipo
    : vid DEL_COLON tipo DEL_SEMICOLON;
vid
    : ID
    | ID DEL_COMA vid;
tipo
    : PR_ENTERO
    | PR_FLOTANTE;
ppfuncs
    :
    | pfuncs ppfuncs;
pfuncs
    : funcs
    | funcs pfuncs;
funcs
    : PR_NULA ID PARENTESIS_OPEN fidtipo PARENTESIS_CLOSE LLAVE_OPEN pvars cuerpo LLAVE_CLOSE DEL_SEMICOLON;
fidtipo
    : 
    | fid;
fid
    : ID DEL_COLON tipo
    | ID DEL_COLON tipo DEL_COMA fid;
cuerpo
    : LLAVE_OPEN ccestatuto LLAVE_CLOSE;
ccestatuto
    : 
    | cestatuto;
cestatuto
    : estatuto
    | estatuto cestatuto;
estatuto
    : asigna
    | condicion
    | ciclo
    | llamada
    | imprime;
asigna
    : ID ASIGNACION expresion DEL_SEMICOLON;
expresion
    : exp eexp;
eexp
    : 
    | comp exp;
comp
    : COMP_GREATER
    | COMP_LESS
    | COMP_NOTEQUAL
    | COMP_EQUAL;
exp
    : termino
    | termino sign exp;
sign
    : OP_PLUS
    | OP_MINUS;
termino
    : factor
    | factor op termino;
op
    : OP_MULTIPLY
    | OP_DIVIDE;
factor
    : PARENTESIS_OPEN expresion PARENTESIS_CLOSE
    | fsign faid;
fsign
    : 
    | sign;
faid
    : ID
    | cte;
cte
    : CTE_ENT
    | CTE_FLOT;
condicion
    : PR_SI PARENTESIS_OPEN expresion PARENTESIS_CLOSE cuerpo csino DEL_SEMICOLON;
csino
    : 
    | PR_SINO cuerpo;
ciclo
    : PR_MIENTRAS PARENTESIS_OPEN expresion PARENTESIS_CLOSE PR_HAZ cuerpo DEL_SEMICOLON;
llamada
    : ID PARENTESIS_OPEN llexpresion PARENTESIS_CLOSE DEL_SEMICOLON;
llexpresion
    : 
    | lexpresion;
lexpresion
    : expresion
    | expresion DEL_COMA lexpresion;
imprime
    : PR_ESCRIBE PARENTESIS_OPEN icont PARENTESIS_CLOSE DEL_SEMICOLON;
icont
    : cont
    | cont DEL_COMA icont;
cont
    : expresion
    | LETRERO;
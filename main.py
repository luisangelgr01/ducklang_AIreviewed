from antlr4 import *
from ducklangLexer import ducklangLexer
from ducklangParser import ducklangParser

def main(input_txt):
    with open(input_txt, 'r') as file:
        ducklang_code = file.read()
    input_stream = InputStream(ducklang_code)   #se convierte a formato que puede leer antlr

    lexer = ducklangLexer(input_stream)         #se manda a llamar primero al lexer
    token_stream = CommonTokenStream(lexer)     #el resultado se covnierte al formato que puede leer el parser
    parser = ducklangParser(token_stream)       #se manda a llamar al parser

    arbol = parser.programa()                   #el resultado es el arbol con la raíz siendo la regla de grmática 'programa'
    print(arbol.toStringTree(recog=parser))     #se imprime el arbol resultante del parser en formato de texto

if __name__ == '__main__':
    input_txt = 'input_ducklang_code.txt'
    main(input_txt)
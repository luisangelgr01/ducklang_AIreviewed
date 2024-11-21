from antlr4 import *
from ducklangLexer import ducklangLexer
from ducklangParser import ducklangParser
from ducklangSemanticAnalyzer import ducklangSemanticAnalyzer
from VirtualMachine import VirtualMachine

def main(input_txt):
    with open(input_txt, 'r') as file:
        ducklang_code = file.read()
    input_stream = InputStream(ducklang_code)           #se convierte a formato que puede leer antlr

    lexer = ducklangLexer(input_stream)                 #se manda a llamar primero al lexer
    token_stream = CommonTokenStream(lexer)             #el resultado se covnierte al formato que puede leer el parser
    parser = ducklangParser(token_stream)               #se manda a llamar al parser

    arbol = parser.programa()                           #el resultado es el arbol con la raíz siendo la regla de grmática 'programa'
    print('\nARBOL RESULTANTE:\n')
    print(arbol.toStringTree(recog=parser))             #se imprime el arbol resultante del parser en formato de texto

    analizador_semantica = ducklangSemanticAnalyzer()   #se incializa objeto de la clase que realiza el analisis semántico
    walker = ParseTreeWalker()                          #se inicializa objeto que recorre árboles
    walker.walk(analizador_semantica, arbol)            #se recorre el árbol resultante con el analisis semántico
    quads = analizador_semantica.ovejota_quads
    funcs = analizador_semantica.ovejota_funcs

    vm = VirtualMachine(quads, funcs)
    vm.execute()

if __name__ == '__main__':
    #input_txt = 'input_ducklang_code.txt'
    input_txt = 'factorial_example.txt'
    main(input_txt)
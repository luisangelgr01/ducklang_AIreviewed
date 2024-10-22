from antlr4 import *
from ducklangLexer import ducklangLexer
from ducklangParser import ducklangParser

def main(input_file):
    # Open the input file and read the contents
    with open(input_file, 'r') as file:
        input_text = file.read()

    # Create an input stream from the file content
    input_stream = InputStream(input_text)

    # Initialize the lexer and parser
    lexer = ducklangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ducklangParser(token_stream)

    # Parse the input (starting from the 'ifStatement' rule or any top-level rule)
    tree = parser.ifStatement()  # or the top-level rule of your grammar

    # Print the parse tree (for debugging or visualization)
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    # Specify the input file path here (e.g., 'input.txt')
    input_file = 'input_ducklang_code.txt'
    main(input_file)

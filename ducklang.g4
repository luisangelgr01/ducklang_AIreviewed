grammar ducklang;  // Name of the grammar

// Lexer rules (tokens)
IF      : 'if';         // Matches the keyword 'if'
ELSE    : 'else';       // Matches the keyword 'else'
ID      : [a-zA-Z_][a-zA-Z_0-9]*; // Identifier rule similar to regex
NUMBER  : [0-9]+;       // Integer number
LPAREN  : '(';          // Left parenthesis
RPAREN  : ')';          // Right parenthesis
LBRACE  : '{';          // Left curly brace
RBRACE  : '}';          // Right curly brace
EQ      : '=';          // Assignment operator
WS      : [ \t\r\n]+ -> skip;  // Skip whitespace

// Parser rules (grammar)
ifStatement
    : IF LPAREN expression RPAREN block (ELSE block)?;  // if-else structure with optional else
block
    : LBRACE statement* RBRACE;  // Block of statements
statement
    : ifStatement                // Statement can be an if statement
    | assignment;                // Or an assignment
assignment
    : ID EQ expression;          // Assignment: ID = expression
expression
    : ID                         // Expression can be a variable (ID)
    | NUMBER;                    // Or a number

# Generated from ducklang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ducklangParser import ducklangParser
else:
    from ducklangParser import ducklangParser

# This class defines a complete listener for a parse tree produced by ducklangParser.
class ducklangListener(ParseTreeListener):

    # Enter a parse tree produced by ducklangParser#ifStatement.
    def enterIfStatement(self, ctx:ducklangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ducklangParser#ifStatement.
    def exitIfStatement(self, ctx:ducklangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ducklangParser#block.
    def enterBlock(self, ctx:ducklangParser.BlockContext):
        pass

    # Exit a parse tree produced by ducklangParser#block.
    def exitBlock(self, ctx:ducklangParser.BlockContext):
        pass


    # Enter a parse tree produced by ducklangParser#statement.
    def enterStatement(self, ctx:ducklangParser.StatementContext):
        pass

    # Exit a parse tree produced by ducklangParser#statement.
    def exitStatement(self, ctx:ducklangParser.StatementContext):
        pass


    # Enter a parse tree produced by ducklangParser#assignment.
    def enterAssignment(self, ctx:ducklangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ducklangParser#assignment.
    def exitAssignment(self, ctx:ducklangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ducklangParser#expression.
    def enterExpression(self, ctx:ducklangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ducklangParser#expression.
    def exitExpression(self, ctx:ducklangParser.ExpressionContext):
        pass



del ducklangParser
import sys
from antlr4 import *
from ComplejosLexer import ComplejosLexer
from ComplejosParser import ComplejosParser
from ComplejosVisitor import ComplejosVisitor

class ComplexEvalVisitor(ComplejosVisitor):
    def visitExpr(self, ctx):
        if ctx.op:  # Hay una operación
            left = self.visit(ctx.left)
            right = self.visit(ctx.right)
            if ctx.op.type == ComplejosParser.ADD:
                return complex(left) + complex(right)
            elif ctx.op.type == ComplejosParser.SUB:
                return complex(left) - complex(right)
        else:  # Es un solo número complejo
            return complex(ctx.getText())

def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = ComplejosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ComplejosParser(stream)
    tree = parser.expr()

    visitor = ComplexEvalVisitor()
    result = visitor.visit(tree)
    print("Resultado:", result)

if __name__ == '__main__':
    main()


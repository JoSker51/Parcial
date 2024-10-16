grammar Complejos;

@header {
    import sys
}

@members {
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
}

expr
    : left=term (op=(ADD|SUB) right=term)* EOF
    ;

term
    : COMPLEX
    ;

COMPLEX
    : '(' NUM (ADD|SUB) NUM 'i' ')'
    ;

NUM
    : [0-9]+
    ;

ADD
    : '+'
    ;

SUB
    : '-'
    ;

WS
    : [ \t\r\n]+ -> skip
    ;


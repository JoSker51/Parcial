import sys
from antlr4 import *
from MapFilterLexer import MapFilterLexer
from MapFilterParser import MapFilterParser
from MapFilterVisitor import MapFilterVisitor

# Definimos algunas funciones que el lenguaje soporta
def square(x):
    return x * x

def is_even(x):
    return x % 2 == 0

# Visitante para ejecutar el programa
class MyMapFilterVisitor(MapFilterVisitor):
    
    def visitMapFunction(self, ctx):
        function_name = ctx.ID().getText()
        function = globals()[function_name]  # Buscamos la función en el entorno global
        iterable = self.visit(ctx.iterable())  # Obtenemos el iterable (lista o tupla)
        result = list(map(function, iterable))  # Aplicamos la función con map
        print(f"MAP result: {result}")
        return result
    
    def visitFilterFunction(self, ctx):
        function_name = ctx.ID().getText()
        function = globals()[function_name]  # Buscamos la función en el entorno global
        iterable = self.visit(ctx.iterable())  # Obtenemos el iterable (lista o tupla)
        result = list(filter(function, iterable))  # Aplicamos la función con filter
        print(f"FILTER result: {result}")
        return result

    def visitListIterable(self, ctx):
        elements = self.visit(ctx.exprList())  # Evaluamos los elementos de la lista
        return elements
    
    def visitTupleIterable(self, ctx):
        elements = self.visit(ctx.exprList())  # Evaluamos los elementos de la tupla
        return elements
    
    def visitExprList(self, ctx):
        return [int(expr.getText()) for expr in ctx.expr()]  # Convertimos los elementos a enteros

# Función principal para ejecutar el programa
def main(input_text):
    input_stream = InputStream(input_text)
    lexer = MapFilterLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MapFilterParser(token_stream)
    tree = parser.program()

    visitor = MyMapFilterVisitor()
    visitor.visit(tree)  # Ejecutamos el programa visitando el árbol

if __name__ == '__main__':
    # Ejemplo de entrada
    input_text = 'MAP(square, [1, 2, 3, 4])\nFILTER(is_even, [1, 2, 3, 4])'
    main(input_text)


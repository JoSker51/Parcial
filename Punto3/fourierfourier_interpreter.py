import sympy as sp
from antlr4 import InputStream, CommonTokenStream
from FourierLexer import FourierLexer
from FourierParser import FourierParser
from FourierVisitor import FourierVisitor

class FourierInterpreter(FourierVisitor):

    def visitFourierExpr(self, ctx):
        print("Aplicando la transformada de Fourier...")
        time_func = self.visit(ctx.cosFunction())
        print(f"Función de tiempo recibida: {time_func}")

        # Definir las variables simbólicas de tiempo y frecuencia
        t, w = sp.symbols('t w', real=True)

        # Calcular la transformada de Fourier usando SymPy
        fourier_result = sp.fourier_transform(time_func, t, w)
        print(f"Resultado de la transformada de Fourier: {fourier_result}")
        return fourier_result

    def visitCosFunction(self, ctx):
        print("Visitando la función coseno")

        # Obtener el valor numérico dentro del coseno usando el token generado
        expr_value = float(ctx.getChild(2).getText())  # Obtener el tercer hijo (que es el número)
        print(f"Valor de la expresión dentro del coseno: {expr_value}")

        # Definir la variable de tiempo 't'
        t = sp.Symbol('t', real=True)

        # Crear la función coseno simbólica
        cos_func = sp.cos(expr_value * t)
        print(f"Resultado de la función coseno: {cos_func}")
        return cos_func

def main(input_text):
    print("Iniciando análisis...")
    input_stream = InputStream(input_text)
    lexer = FourierLexer(input_stream)

    # Procesar tokens
    token_stream = CommonTokenStream(lexer)
    parser = FourierParser(token_stream)

    try:
        # Parsear el input para crear el árbol
        tree = parser.program()
        visitor = FourierInterpreter()

        print("Iniciando visita del árbol...")
        result = visitor.visit(tree)  # Visitar el árbol y obtener el resultado
        print(f"Resultado final: {result}")
    except Exception as e:
        print(f"Error al procesar el árbol: {e}")

if __name__ == "__main__":
    # Solo un caso de prueba: la transformada de Fourier de cos(2)
    input_text = "F[cos(2)]"
    main(input_text)

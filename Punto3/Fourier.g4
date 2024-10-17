grammar Fourier;

// Regla principal del programa
program : fourierExpr EOF;

// Reglas para las expresiones
fourierExpr
    : 'F' '[' cosFunction ']'  // Regla para aplicar la transformada de Fourier a la función coseno
    ;

// Reglas para funciones trigonométricas
cosFunction
    : 'cos' '(' NUMBER ')'     // Función coseno
    ;

// Tokens
NUMBER  : [0-9]+ ('.' [0-9]+)? ; // Números (enteros o flotantes)
WS      : [ \t\r\n]+ -> skip;    // Ignorar espacios en blanco

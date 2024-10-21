Jose Santiago Gonzalez Enriquez

Ejercicio 1

El ejercicio de prueba que se uso fue este (2 + 7i) + (3 - 4i)

Para ejecutar el programa primero se deben generar los archivos de antlr con este comando: antlr4 -Dlanguage=Python3 -visitor Complex.g4

Y se ejecuta el main con este otro: python complex_calculator.py

Para cambiar el input del programa se debe de cambiar la linea "input_text = " que se encuentra en el main. Esta ya viene con los ejemplos mencionados

Ejercicio 2

El ejercicio de ejemnplo que se uso en este ejercicio fue este: MAP(duplicate, [1, 2, 3]) y este FILTER(multipleOfTwo, [1, 2, 3, 4])

Para ejecutar el ejercicio se necesita generar los archivos de antlr cone ste comando: antlr4 -Dlanguage=Python3 -visitor MapFilter.g4

Y se ejecuta el main con este comando: python map_filter_interpreter.py

En este ejercicio tambien se debe cambiar la variable "input_text = ", el ionput debe de tener una entrada de esta manera "MAP(duplicate, [1, 2, 3])". De igual manera esta variable ya tiene el ejemplo como input.
A su vez se puede cambiar la palabra MAP por Filter para cambiar la accion del programa.

Ejercicio 3

El ejemplo que use en este ejercicio fue este: F[cos(2)]

Para correr este ejercicio se necesita generar los archivos de antlr con este comando: antlr4 -Dlanguage=Python3 -visitor Fourier.g4

Y se ejecuta el main con este otro comando: python fourier_interpreter.py

Tambien en este ejercicio se puede cambair el input, cambiando la variable "input_text" aqui se pone un comando como en el ejemplo (F[cos(2)]) para realizar una transofrmada de fourier, a suvez se puede modificar el input para que haga una transformada a otras funciones, como en estos ejemplos "sin(2)" "rect(3)"

Recordar que la variable input_text se encuentra en el main de cada programa.


#Operadores Aritmeticos
#Asinacion de variables de prueba

a = 10
b = 15

#Operador de Suma (+)
print ("Valor de la Suma es: ", a + b) #El operador de suma (+) se utiliza para sumar dos valores. En este caso, se suman los valores de las variables a y b, y el resultado se imprime en la consola.

#Operador de Resta (-)
print ("Valor de la Resta es: ", a - b) #El operador de resta (-) se utiliza para restar dos valores. En este caso, se resta el valor de la variable b del valor de la variable a, y el resultado se imprime en la consola.

#Operador de Multiplicacion (*)
print ("Valor de la Multiplicacion es: ", a * b) #El operador de multiplicación (*) se utiliza para multiplicar dos valores. En este caso, se multiplican los valores de las variables a y b, y el resultado se imprime en la consola.

#Operador de Division (/)
print ("Valor de la Division es: ", b / a) #El operador de división (/) se utiliza para dividir dos valores. En este caso, se divide el valor de la variable a entre el valor de la variable b, y el resultado se imprime en la consola. La división siempre devuelve un valor de tipo float, incluso si ambos operandos son enteros.

#Operador Modulo (%)
print ("Valor del Modulo es: ", b % a) #El operador de módulo (%) se utiliza para obtener el residuo de la división entre dos valores. En este caso, se obtiene el residuo de la división del valor de la variable a entre el valor de la variable b, y el resultado se imprime en la consola.

#Operador de Exponente (**)
print ("Valor del Exponente es: ", a ** b) #El operador de exponente (**) se utiliza para elevar un valor a la potencia de otro valor. En este caso, se eleva el valor de la variable a a la potencia del valor de la variable b, y el resultado se imprime en la consola.

#Operador de Division Entera (//)
print ("Valor de la Division Entera es: ", b // a) #El operador de división entera (//) se utiliza para dividir dos valores y obtener el cociente entero de la división. En este caso, se divide el valor de la variable a entre el valor de la variable b, y el resultado se imprime en la consola. La división entera devuelve un valor de tipo int, incluso si ambos operandos son enteros.

#Ejemplo de uso del operador modulo para determinar si un número es par o impar
numero = 7
print(numero % 2 == 0) # Imprime True, ya que el residuo de la división de 8 entre 2 es 0, lo que indica que el número es par. Si el residuo fuera diferente de 0, el número sería impar.

#Presendencia de operadores aritmeticos en una expresion matematica

#En Python, la precedencia de los operadores aritméticos determina el orden en que se evalúan las operaciones en una expresión matemática. Los operadores con mayor precedencia se evalúan antes que los operadores con menor precedencia. La precedencia de los operadores aritméticos en Python es la siguiente (de mayor a menor):
#1. Paréntesis: ()
#2. Exponente: **
#3. Multiplicación y división: * y / divisiones entera: // y módulo: %
#4. Suma y resta: + y -
#5. comparaciones de igualdad y pertenencia: ==, !=, <, >, <=, >=, in, not in
#6. logicos and, or, not
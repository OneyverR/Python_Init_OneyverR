

#lambda: Son funciones anónimas que se pueden usar para crear funciones simples en una sola línea. Además, se pueden usar para crear funciones que se pueden pasar como argumentos a otras funciones. La sintaxis de una función lambda es la siguiente:

#Sintaxis de una función lambda:
#lambda argumentos: expresion

x = lambda a: a + 10 #Funcion lambda que recibe un parametro "a" y retorna el valor de "a" + 10
print(x(5)) #Llamada a la funcion lambda con el parametro 5.

#Lambda con dos parametros:
y = lambda a, b: a * b #Funcion lambda que recibe dos parametros "a" y "b" y retorna el valor de "a" * "b"
print(y(5, 6)) #Llamada a la funcion lambda con los parametros 5 y 6.

#Lambda para fabricar funciones:
def fabrica_funciones(n):
    return lambda x: x * n #Funcion lambda que recibe un parametro "x" y retorna el valor de "x" * "n"

multiplicador = fabrica_funciones(2) #Llamada a la funcion fabrica_funciones con el parametro 2. La funcion retorna una funcion lambda que multiplica el parametro "x" por 2.

triplicador = fabrica_funciones(3) #Llamada a la funcion fabrica_funciones con el parametro 3. La funcion retorna una funcion lambda que multiplica el parametro "x" por 3.

quintuplicador = fabrica_funciones(5)

print(multiplicador(5)) #Llamada a la funcion lambda retornada por la funcion fabrica_funciones con el parametro 5. La funcion retorna el valor de 5 * 2.

print(triplicador(5)) #Llamada a la funcion lambda retornada por la funcion fabrica_funciones con el parametro 5. La funcion retorna el valor de 5 * 3.

print(quintuplicador(100))
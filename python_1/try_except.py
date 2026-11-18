# Try and except: La sentencia try y except se utiliza para manejar errores en Python. La sentencia try contiene el codigo que puede generar un error, mientras que la sentencia except contiene el codigo que se ejecuta si se produce un error. La sentencia try y except se utiliza para evitar que el programa se detenga cuando se produce un error.
# La sintaxis de la sentencia try y except es la siguiente:

# try:
#     #Codigo que puede generar un error
# except TipoDeError:
#     #Codigo que se ejecuta si se produce un error

#Ejemplo de la sentencia try y except: division por cero. En este caso se produce un error de division por cero, por lo que se ejecuta el codigo que se encuentra en la sentencia except.

try:
    division = 10 / 0 #Codigo que puede generar un error. En este caso se produce un error de division por cero.
except ZeroDivisionError: #Tipo de error que se produce. En este caso es un error de division por cero.
    print("Error: No se puede dividir entre cero") #Codigo que se ejecuta si se produce un error. En este caso se imprime un mensaje de error.

#Ejemplo de la sentencia try y except: variable no definida. En este caso se produce un error de variable no definida, por lo que se ejecuta el codigo que se encuentra en la sentencia except.

try:
    print(variable_no_definida) #Codigo que puede generar un error. En este caso se produce un error de variable no definida.
except NameError: #Tipo de error que se produce. En este caso es un error de variable no definida.
    print("Error: Variable no definida") #Codigo que se ejecuta si se produce un error. En este caso se imprime un mensaje de error.

#Ejemplo de la sentencia try y except con la sentencia finally: La sentencia finally se utiliza para ejecutar un bloque de codigo sin importar si se produce un error o no. La sentencia finally se ejecuta siempre, incluso si se produce un error en la sentencia try.

try:
    b = 10 / 0 #Codigo que puede generar un error. En este caso se produce un error de division por cero.
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero") #Codigo que se ejecuta si se produce un error. En este caso se imprime un mensaje de error.
finally:
    print("Ejecutando bloque finally sin importar si se produce un error o no") #Codigo que se ejecuta siempre, incluso si se produce un error en la sentencia try. 

#Tipos de errores en Python: Los errores en Python se pueden clasificar en tres tipos: errores de sintaxis, errores de excepcion y errores de logica. Los errores de sintaxis se producen cuando el codigo no cumple con las reglas del lenguaje Python. Los errores de excepcion se producen cuando el codigo cumple con las reglas del lenguaje Python, pero se produce un error en tiempo de ejecucion. Los errores de logica se producen cuando el codigo cumple con las reglas del lenguaje Python y no se produce un error en tiempo de ejecucion, pero el resultado del programa no es el esperado. Estos errores se pueden manejar mediante la sentencia try y except para evitar que el programa se detenga cuando se produce un error.

#Funcion: Una funcion es un bloque de codigo que se puede reutilizar, es decir, que se puede llamar varias veces en el programa. Permite organizar el codigo y evitar la repeticion de codigo. Una funcion puede recibir parametros y retornar valores.

#Estructura de una funcion:
#def nombre_de_la_funcion(parametros):
#    #Codigo de la funcion
#    return valor   

#Ejemplo de una funcion que recibe parametros y retorna un valor:
def mi_funcion(): #Argumentos de la funcion
    print("Hola, soy una funcion")

mi_funcion() #Llamada a la funcion. Parametros de la funcion. En este caso no tiene parametros.

#Ejemplo de una funcion que recibe parametros y retorna un valor para saludar a una persona:
def saludar(nombre, apellidos): #Argumentos de la funcion
    print(f"Hola {nombre, apellidos}, bienvenido a la programacion en Python")

saludar("Oneyver", "Rodriguez") #Llamada a la funcion con el parametro "Oneyver". Parametros de la funcion. En este caso tiene un parametro llamado "nombre"
saludar("Carlos", "Gonzalez") #Llamada a la funcion con el parametro "Carlos"

#Agregar un valor por defecto a un parametro de la funcion:
def saludar2(nombre, pais="Colombia"): #Argumentos de la funcion
    print("Hola ", nombre, "Eres de ", pais)

saludar2("Oneyver") #Llamada a la funcion con el parametro "Oneyver". Parametros de la funcion. En este caso tiene un parametro llamado "nombre" y un parametro por defecto llamado "pais"

#Devolucion de valores de una funcion medos de la palabra reservada return:
def suma(a, b): #Argumentos de la funcion
    return a + b #Devolucion de valores de la funcion

resultado = suma(5, 3) #Llamada a la funcion con los parametros 5 y 3. Parametros de la funcion. En este caso tiene dos parametros llamados "a" y "b"
print("El resultado de la suma es: ", resultado) #Impresion del resultado de la funcion suma

#Uso de pass en una funcion: La palabra reservada pass se utiliza para indicar que una funcion no tiene codigo, es decir, que no hace nada. Se utiliza para crear funciones vacias que se pueden completar posteriormente.
def funcion_vacia(): #Argumentos de la funcion
    pass #La funcion no hace nada

#Ejemplo de operaciones matematicas mediante el uso de funciones:
def suma3(a , b):
    return a + b

resultado_suma = suma3(100, 100)
print("El resultado de la suma es: ", resultado_suma)

def resta(a, b):
    return a - b
resultado_resta = resta(100, 50)
print("El resultado de la resta es: ", resultado_resta)

def multiplicacion(a , b):
    return a * b
resultado_multiplicacion = multiplicacion(5, 5)
print("El resultado de la multiplicacion es: ", resultado_multiplicacion)

def division(a, b):
    return a / b
resultado_division = division(100, 100)
print("El resultado de la division es: ", resultado_division)


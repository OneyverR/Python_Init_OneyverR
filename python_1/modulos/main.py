#Modulos en Python: Un modulo es un archivo que contiene codigo Python, es decir, que contiene funciones, clases y variables. Los modulos se pueden importar en otros archivos Python para reutilizar el codigo. Los modulos se pueden importar de dos formas: importando todo el modulo o importando solo las funciones, clases o variables que se necesitan.

#En este ejemplo se importan las funciones suma, resta, multiplicacion y division del modulo operaciones.py y se utilizan en el archivo main.py.
#Que informacion se debe tener en el modulo operaciones.py para que el archivo main.py funcione correctamente? Se deben tener las funciones suma, resta, multiplicacion y division definidas en el modulo operaciones.py. Como ejemplo, el modulo operaciones.py debe tener el siguiente codigo:
# def suma(a , b):
#     return a + b   
# def resta(a, b):
#     return a - b
# def multiplicacion(a , b):
#     return a * b
# def division(a, b):
#     return a / b


from operaciones import suma, resta, multiplicacion, division #Metodo de importacion de funciones de un modulo. Se importan las funciones suma, resta, multiplicacion y division del modulo operaciones.py

print(suma(2,2))
print(resta(5,2))
print(multiplicacion(10,2))
print(division(15,2))

#Otro metodo de importacion de funciones de un modulo es importando todo el modulo y luego llamando a las funciones con el nombre del modulo. Por ejemplo:
import operaciones #Metodo de importacion de todo el modulo operaciones.py

print(operaciones.suma(2,2))
print(operaciones.resta(5,2))
print(operaciones.multiplicacion(10,2))
print(operaciones.division(15,2))

#En general, se recomienda importar solo las funciones, clases o variables que se necesitan de un modulo para evitar conflictos de nombres y para mejorar la legibilidad del codigo.
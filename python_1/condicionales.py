
#Condicional If-Else
#El condicional if-else es una estructura de control que permite ejecutar un bloque de código si se cumple una condición, y otro bloque de código si no se cumple. La sintaxis básica es la siguiente:

x = 3
y = 5
z = 1

# if condición:
if  x > y:
    print("5 es mayor que 3")
elif x == y:
    print("5 es igual a 3")
else:
    print("5 es menor que 3")


# If con 2 condiciones
if x > y and x > z:
    print("5 es mayor que 3 y 1")
elif x == y or x > z:
    print("5 es igual a 3 o mayor que 1")
else:
    print("5 es menor que 3 y 1")


# Condicional IF con IF Anidados 
a = "Python"
b = "Javascript"
c = "Python"

if a == c: 
    if a == b:
        print("a es igual a c pero a es diferente de b")
    else: 
        print("Saliendo por el else del If interno")
else: 
    print("a no es igual a c")

#statement pass
# El statement pass es una instrucción que no hace nada. Se utiliza como un marcador de posición en el código, para indicar que no se debe ejecutar ninguna acción en ese lugar. Se utiliza comúnmente en estructuras de control como if, for y while, cuando se desea dejar un bloque de código vacío.

e = 10
f = 10
if e == f:
    pass  # No hace nada. Ignora el bloque de código y continúa con la ejecución del programa hasta determinar la siguiente instrucción. En este caso, el programa no hace nada y continúa con la ejecución del código después del bloque if.
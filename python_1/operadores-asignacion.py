
#Operadores de Asignacion
# Igual (=) 
x = 5
a = 3

# Suma y asignacion (+=)
x = x + 3
print(x)  # Imprime 6

x += 3  # Equivalente a x = x + 3
print(x)  # Imprime 8

#Resta y asignacion (-=)
x = x -3
x -= 3  # Equivalente a x = x - 3
print(x)  # Imprime 2

#Multiplicacion y asignacion (*=)
x *= 3  # Equivalente a x = x * 3
print(x)  # Imprime 6

#Division y asignacion (/=)
x /= 3
print(x)  # Imprime 5.0

#Modulo y asignacion (%=)
x %= 2
print(x)  # Imprime 1.0, ya que el residuo de la división de 5 entre 2 es 1

#Division entera y asignacion (//=)
y = 21
y //= 2
print("y =", str(y))  # Imprime 10, ya que la división entera de 21 entre 2 es 10

#Exponente y asignacion (**=)
y **= 3
print("y =", str(y))  # Imprime 1000, ya que 10 elevado a la potencia de 3 es 1000


#Walrus operator (:=)
# El operador walrus (:=) es un operador de asignación que permite asignar un valor a una variable como parte de una expresión. Este operador se introdujo en Python 3.8 y se utiliza para simplificar el código al permitir la asignación y la evaluación en una sola línea.
print(z := 23) # Asigna el valor 23 a la variable z y lo imprime en la consola
print("Z =", str(z)) # Imprime 23, ya que la variable z ahora tiene el valor 23
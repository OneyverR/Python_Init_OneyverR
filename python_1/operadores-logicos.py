
#operadores de comparación
# Los operadores de comparación se utilizan para comparar dos valores y devolver un valor booleano (True o False) en función de si la comparación es verdadera o falsa. Los operadores de comparación más comunes son:

#Igual a (==): Devuelve True si los valores son iguales, de lo contrario devuelve False.
x = 5
y = 3
z = 5
print(x == y)  # Imprime False, ya que 5 no es igual a 3

#Diferente de (!=): Devuelve True si los valores son diferentes, de lo contrario devuelve False.
print(x != y) #Imprimer True ya que 5 es diferente de 3   

#Mayor que (>): Devuelve True si el valor de la izquierda es mayor que el valor de la derecha, de lo contrario devuelve False.
print(x > y) #Imprime True ya que 5 es mayor que 3

#Menor que (<): Devuelve True si el valor de la izquierda es menor que el valor de la derecha, de lo contrario devuelve False.
print(x < y) #Imprime False ya que 5 no es menor que 3

#Mayor o igual que (>=): Devuelve True si el valor de la izquierda es mayor o igual que el valor de la derecha, de lo contrario devuelve False.
print(x >= y) #Imprime True ya que 5 es mayor o igual que 3

#Menor o igual que (<=): Devuelve True si el valor de la izquierda es menor o igual que el valor de la derecha, de lo contrario devuelve False.
print(x <= y) #Imprime False ya que 5 no es menor o igual que 3

#Operadores Logicos: Estos nos permiten combinar varias condiciones y devolver un valor booleano en función de si todas las condiciones son verdaderas o falsas. Los operadores lógicos más comunes son: 

# and (and): Devuelve True si ambas condiciones son verdaderas, de lo contrario devuelve False.
print(x > y and y > z)

#or (or): Devuelve True si al menos una de las condiciones es verdadera, de lo contrario devuelve False.
print(x > y or y > z)

#not (not): Devuelve True si la condición es falsa, de lo contrario devuelve False.
v = True
f = False
print(not(v)) #Imprime False ya que x es mayor que y
print(not(f)) #Imprime True ya que f es False

# Se conocemos como booleanos a los valores de verdad, es decir, aquellos que pueden ser verdaderos o falsos. En Python, los booleanos se representan con las palabras clave True y False.

v = True
f = False

print(v)  # Imprime True
print(f)  # Imprime False

print(type(v))

# Se utilizan ademas cuando se realizan comparaciones, por ejemplo, para saber si un valor es mayor que otro, si son iguales, etc. Estas comparaciones devuelven un valor booleano (True o False).

print(12 > 3) # Imprime True, ya que 12 es mayor que 3
print(12 < 3) # Imprime False, ya que 12 no es menor
print(12 == 3) # Imprime False, ya que 12 no es igual a 3
print(12 != 3) # Imprime True, ya que 12 no es igual a 3

#Casting de string a booleano
#El casting de string a booleano se realiza utilizando la función bool(). Esta función convierte un valor de tipo string en un valor booleano. En Python, cualquier cadena de texto que no esté vacía se considera True, mientras que una cadena vacía se considera False

print(bool(""))
print(bool("Hola Me llamo Oneyver"))

#Castig con diferentes tipos de datos
print(bool(123))
print(bool("abcd"))
print(bool([1,2,3,4,5,6]))

#Casos en los que el casting devuelve False
print(bool("")) 
print(bool(0))
print(bool([]))
print(bool(None))

#Otras formas de tener un valor booleano es usando isinstance() para verificar si un objeto es de un tipo específico. Por ejemplo, podemos verificar si una variable es una cadena de texto (str) o un número entero (int).

x = 1223
print(isinstance(x, int))  # Imprime True, ya que x es un número entero

y = "Hola Oneyver RODRIGUEZ"
print(isinstance(y,int))  # Imprime False, ya que y no es un número entero, sino una cadena de texto
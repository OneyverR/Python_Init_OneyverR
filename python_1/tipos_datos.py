
#String
# String es una secuencia de caracteres, se puede definir con comillas simples o dobles.

#Strin con comillas simples
string1 = 'Texto con Comillas Simples'  # String con comillas simples

#String con comillas dobles
string2 = "Texto con Comillas Dobles"  # String con comillas dobles

#String con comillas triples
string3 = '''Texto con comillas triples'''  # String con comillas triples

print(string1)  # Imprime Hola Mundo
print(string2)  # Imprime Hola Mundo
print(string3)  # Imprime Hola Mundo

#Numeros
"""
Numeros en Python pueden ser enteros o flotantes. Los enteros son numeros sin decimales, mientras que los flotantes son numeros con decimales.
"""

#Enteros
entero1 = 10  # Entero positivo
print(entero1)  # Imprime 10
entero2 = -5  # Entero negativo
print(entero2)  # Imprime -5

#Flotantes
flotante1 = 3.14  # Flotante positivo
flotante2 = -2.71  # Flotante negativo  

print(flotante1)  # Imprime 3.14
print(flotante2)  # Imprime -2.71

#Complejos
"""
Los numeros complejos son numeros que tienen una parte real y una parte imaginaria. En Python, los numeros complejos se representan con la letra j. Por ejemplo, 2 + 3j es un numero complejo con parte real 2 y parte imaginaria 3."""

complejo1 = 2 + 3j  # Numero complejo con parte real 2 y parte imaginaria 3
complejo2 = 4 - 5j  # Numero complejo con parte real 4 y parte imaginaria -5

print(complejo1)  # Imprime (2+3j)
print(complejo2)  # Imprime (4-5j)

#Listas
"""
Las listas son estructuras de datos que permiten almacenar una colección de elementos. En Python, las listas se definen con corchetes [] y los elementos se separan por comas. Las listas pueden contener elementos de diferentes tipos de datos, incluyendo otras listas. Estas son mutables, lo que significa que se pueden modificar después de su creación. Se pueden agregar, eliminar o cambiar elementos en una lista.
"""
lista1 = [1, 2, 3, 4, 5]  # Lista de enteros
lista2 = ["Manzana", "Pera", "Fresa"]  # Lista de strings
lista3 = [1, "Manzana", 3.14, True]  #Lista con elementos de diferentes tipos de datos

#Tuplas
"""
Las tuplas son estructuras de datos similares a las listas, pero a diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar una vez que se han creado. En Python, las tuplas se definen con paréntesis () y los elementos se separan por comas.
"""
tupla1 = (1, 2, 3, 4, 5)  # Tupla de enteros
tupla2 = ("Manzana", "Pera", "Fresa")  # Tupla de strings
tupla3 = (1, "Manzana", 3.14, True)  # Tupla con elementos de diferentes tipos de datos

#Diccionarios
"""
Los diccionarios son estructuras de datos que permiten almacenar una colección de elementos en pares clave-valor. En Python, los diccionarios se definen con llaves {} y los elementos se separan por comas. Cada elemento del diccionario tiene una clave única que se utiliza para acceder a su valor correspondiente. Los diccionarios son mutables, lo que significa que se pueden modificar después de su creación. Se pueden agregar, eliminar o cambiar elementos en un diccionario.
"""
diccionario1 = {
    "nombre": "Juan", 
    "edad": 30, 
    "ciudad": "Madrid"
}  # Diccionario con claves y valores de diferentes tipos de datos

#Conjuntos (sets)
"""
Los conjuntos son estructuras de datos que permiten almacenar una colección de elementos únicos y no ordenados. En Python, los conjuntos se definen con llaves {} o con la función set(). Los conjuntos son mutables, lo que significa que se pueden modificar después de su creación. Se pueden agregar o eliminar elementos en un conjunto. Los conjuntos no permiten elementos duplicados, por lo que si se intenta agregar un elemento que ya existe en el conjunto, no se producirá ningún cambio. No se peuden acceder a los elementos de un conjunto mediante un índice, ya que no tienen un orden definido.
"""
conjunto1 = {1,1,1, 2,2,2,2, 3,3,3, 4,4,4, 5}  # Conjunto de enteros
conjunto2 = {"Manzana", "Pera", "Fresa"}  # Conjunto de strings 
Conjunto3 = {1, "Manzana", 3.14, True}  # Conjunto con elementos de diferentes tipos de datos

print(conjunto1)  # Imprime {1, 2, 3, 4, 5}

#Booleanos

"""
Los booleanos son un tipo de dato que solo puede tener dos valores posibles: True (verdadero) o False (falso). En Python, los booleanos se representan con las palabras clave True y False. Los booleanos se utilizan comúnmente en expresiones condicionales y en estructuras de control de flujo, como if, while y for. Los booleanos también se pueden utilizar para realizar operaciones lógicas, como AND, OR y NOT.
"""
booleano1 = True  # Booleano verdadero
booleano2 = False  # Booleano falso

print(booleano1)  # Imprime True
print(booleano2)  # Imprime False  
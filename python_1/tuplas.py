#Una tupla es una colección de elementos ordenados e inmutables. A diferencia de las listas, no se pueden modificar después de su creación. Las tuplas se definen utilizando paréntesis () y los elementos se separan por comas.

#Indice s:     0         1         2       3
tecnologias = ("Python", "Java", "C++", "JavaScript")
print(tecnologias) # Imprime la tupla completa: ('Python', 'Java', 'C++', 'JavaScript').

#Imprimir un elemento específico de la tupla utilizando su índice
print(tecnologias[0]) # Imprime el primer elemento de la tupla, que es "Python".

#Las tuplas pueden tener elementos dupplicados
tecnologias_duplicadas = ("Python", "Java", "C++", "JavaScript", "Python")
print(tecnologias_duplicadas) # Imprime la tupla con elementos duplicados: ('Python', 'Java', 'C++', 'JavaScript', 'Python').

#Podemos connocer la cantidad de elementos en una tupla utilizando la función len()
print(len(tecnologias)) # Imprime la cantidad de elementos en la tupla tecnologias, que es 4.

#Podemos conocer el tipo de dato de una tupla utilizando la función type()
print(type(tecnologias)) # Imprime el tipo de la variable tecnologias, que es <class 'tuple'>.

#No se considera como tupla cuando se tiene un solo elemento, para que sea considerada como tupla se debe agregar una coma al final del elemento.
tupla_un_elemento = ("Python",)
print(type(tupla_un_elemento)) # Imprime el tipo de la variable tupla_un_elemento, que es <class 'tuple'>.

#Una tupla puede contener elementos de diferentes tipos de datos, incluyendo números, cadenas y booleanos.
tupla_mixta = (1, "dos", 3.0, True)
print(tupla_mixta) # Imprime la tupla mixta: (1, 'dos', 3.0, True).
print(type(tupla_mixta)) # Imprime el tipo de la variable tupla_mixta, que es <class 'tuple'>.

#Desempaquetado de tuplas: Podemos asignar los elementos de una tupla a variables individuales utilizando el desempaquetado de tuplas.
x, y, z, w = tecnologias
print(x) # Imprime el primer elemento de la tupla, que es "Python".
print(y) # Imprime el segundo elemento de la tupla, que es "Java".
print(z) # Imprime el tercer elemento de la tupla, que es "C++".
print(w) # Imprime el cuarto elemento de la tupla, que es "JavaScript".

#Union de tuplas: Podemos unir dos o más tuplas utilizando el operador +.
tupla1 = ("Python", "Java")
tupla2 = ("C++", "JavaScript")
tupla_unida = tupla1 + tupla2
print(tupla_unida) # Imprime la tupla unida: ('Python', 'Java', 'C++', 'JavaScript').

#Duplicación de tuplas: Podemos duplicar los elementos de una tupla utilizando el operador *.
tupla_duplicada = tupla1 * 2
print(tupla_duplicada) # Imprime la tupla duplicada: ('Python', 'Java', 'Python', 'Java').

#Recorrido de tuplas: Podemos recorrer los elementos de una tupla utilizando un bucle for.
for tecnologia in tecnologias:
    print(tecnologia) # Imprime cada elemento de la tupla tecnologias en una línea separada.

print("="*40)

#La unica forma de modificar una tupla es convirtiendola en lista, modificando la lista y luego convirtiendola nuevamente en tupla.

nueva_tupla = ("ingenieria", "matematica", "fisica")
print(nueva_tupla)
#Convertimos la tupla en lista
nueva_lista = list(nueva_tupla)
#Modificamos la lista
nueva_lista.append("quimica")
#Convertimos la lista nuevamente en tupla
nueva_tupla = tuple(nueva_lista)
print(nueva_tupla) # Imprime la tupla modificada: ('ingenieria', 'quimica', 'fisica', 'quimica').

# #Listas: Colección de elementos ordenados y modificables.

#Indices:     0         1         2       3        4 
frutas = ["naranja", "banana", "kiwi", "pera", "manzana"]
print(frutas) # Imprime la lista completa: ['naranja', 'banana', 'kiwi', 'pera', 'manzana'].
print(frutas[0]) # Imprime el primer elemento de la lista, que es "naranja".
print(type(frutas)) # Imprime el tipo de la variable frutas, que es <class 'list'>.


# #Los elementos de una lista son modificables, lo que significa que podemos cambiar el valor de un elemento en una posición específica.

frutas[1] = "fresa" # Cambia el valor del segundo elemento de la lista a "fresa".
print(frutas) # Imprime la lista actualizada: ['naranja', 'fresa
print(frutas[1]) # Imprime el segundo elemento de la lista, que ahora es "fresa".

# #Una lista puede contener elementos de diferentes tipos de datos, incluyendo números, cadenas y booleanos.

lista_mixta = [1, "dos", 3.0, True]
print(lista_mixta) # Imprime la lista mixta: [1, 'dos, 3.0, True].
print(type(lista_mixta)) # Imprime el tipo de la variable lista_mixta, que es <class 'list'>.

# #Podemos saber cuantos elementos hay en una lista utilizando la función len().
print(len(frutas)) # Imprime la cantidad de elementos en la lista frutas, que es 5.

# #Rango de indices en una lista: Podemos acceder a un rango de elementos en una lista utilizando la sintaxis de slicing.
print(frutas[1:4]) # Imprime los elementos desde el índice 1 hasta el índice 3 (excluyendo el índice 4): ['fresa', 'kiwi', 'pera'].

print(frutas[:3]) # Imprime los primeros tres elementos de la lista: ['naranja', 'fresa', 'kiwi'].

# #Podemos saber si un elemento está presente en una lista utilizando el operador in.
print("fresa" in frutas) # Imprime True si "fresa" está en la lista frutas, de lo contrario imprime False.
if "fresa" in frutas: # Verifica si "fresa" está en la lista frutas.
    print("la fresa está en la lista de frutas.")


#Ejemplo con una lista de Vehiculos
#Metodo para poder moficar un elemento de la lista
vehiculos = ["auto", "camioneta", "moto", "bicicleta", "camion"]
print(vehiculos) # Imprime la lista completa de vehículos: ['auto', 'camioneta', 'moto', 'bicicleta', 'camion'].

#Metodo append() para agregar un elemento al final de la lista
vehiculos.append("avion") # Agrega "avion" al final de la lista de vehículos.
print(vehiculos) # Imprime la lista actualizada de vehículos: ['auto', 'camioneta', 'moto', 'bicicleta', 'camion', 'avion'].

#Metodo insert() para agregar un elemento en una posición específica de la lista
vehiculos.insert(2, "barco") # Inserta "barco" en la posición 2 de la lista de vehículos.
print(vehiculos) # Imprime la lista actualizada de vehículos: ['auto', 'camioneta', 'barco', 'moto', 'bicicleta', 'camion', 'avion'].

#Metodo remove() para eliminar un elemento de la lista
vehiculos.remove("moto") # Elimina "moto" de la lista de vehículos.
print(vehiculos) # Imprime la lista actualizada de vehículos: ['auto', 'camioneta', 'barco', 'bicicleta', 'camion', 'avion'].

#Metodo pop() para eliminar un elemento de la lista por su índice
vehiculos.pop(3) # Elimina el elemento en la posición 3 de la lista de vehículos, que es "bicicleta".
print(vehiculos) # Imprime la lista actualizada de vehículos: ['auto', 'camioneta', 'barco', 'camion', 'avion'].

#Diferencia entre remove() y pop(): remove() elimina un elemento por su valor, mientras que pop() elimina un elemento por su índice.

#Metodo sort() para ordenar los elementos de la lista
vehiculos.sort() # Ordena los elementos de la lista de vehículos en orden alfabético   
print(vehiculos) # Imprime la lista ordenada de vehículos: ['auto', 'avion', 'barco', 'camion', 'camioneta'].

#Revertir el orden de los elementos de la lista
vehiculos.reverse() # Invierte el orden de los elementos de la lista de vehículos.
print(vehiculos) # Imprime la lista con los elementos en orden inverso: ['camioneta', 'camion', 'barco', 'avion', 'auto'].

#Unir dos listas utilizando el operador +
mas_vehiculos = ["helicoptero", "submarino"]
coleccion_vehiculos = vehiculos + mas_vehiculos # Une la lista de vehículos con la lista mas_vehiculos.
print(coleccion_vehiculos) # Imprime la lista combinada de vehículos: ['camioneta', 'camion', 'barco', 'avion', 'auto', 'helicoptero', 'submarino'].

#Metodo extend() para agregar los elementos de una lista a otra
vehiculos.extend(mas_vehiculos) # Agrega los elementos de la lista mas_vehiculos a la lista de vehículos.
print(vehiculos) # Imprime la lista actualizada de vehículos: ['camioneta', 'camion', 'barco', 'avion', 'auto', 'helicoptero', 'submarino'].

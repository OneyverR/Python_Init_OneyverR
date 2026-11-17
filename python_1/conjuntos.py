#Conjuntos (sets): Colección de elementos no ordenados y no indexados. Los conjuntos son útiles para almacenar elementos únicos y realizar operaciones matemáticas como la unión, intersección y diferencia.

marcas_deportivas = {"Nike", "Adidas", "Puma", "Reebok"}
print(marcas_deportivas) # Imprime el conjunto completo: {'Nike', 'Adidas', 'Puma', 'Reebok'}.
print(type(marcas_deportivas)) # Imprime el tipo de la variable marcas_deportivas, que es <class 'set'>.

print("="*80)
marcas_deportivas2 = {"Nike", "Adidas", "Puma", "Reebok", "Nike"}
print(marcas_deportivas2) # Imprime el conjunto completo sin elementos duplicados: {'Nike', 'Adidas', 'Puma', 'Reebok'}.
print(type(marcas_deportivas2)) # Imprime el tipo de la variable marcas_deportivas2, que es <class 'set'>.
print(len(marcas_deportivas2)) # Imprime la cantidad de elementos en el conjunto marcas_deportivas2, que es 4.

#Conjuntos con elementos de diferentes tipos de datos
conjunto_mixto = {1, "dos", 3.0, True}
print(conjunto_mixto) # Imprime el conjunto mixto: {1, 'dos', 3.0, True}.
print(type(conjunto_mixto)) # Imprime el tipo de la variable conjunto_mixto, que es <class 'set'>.

#Recorrrer un conjunto utilizando un bucle for
for marca in marcas_deportivas:
    print(marca) # Imprime cada elemento del conjunto marcas_deportivas en una línea separada. Se debe tener en cuenta que el orden de los elementos puede variar en cada ejecución, ya que los conjuntos no están ordenados.

#Buscar si un elemento está presente en un conjunto utilizando el operador in
print("Nike" in marcas_deportivas) # Imprime True si "Nike" está en el conjunto marcas_deportivas, de lo contrario imprime False.
print("Pera" not in marcas_deportivas) # Imprime True si "Pera" no está en el conjunto marcas_deportivas, de lo contrario imprime False.

#Agregar  elementos de un conjunto utilizando los métodos add()
marcas_deportivas.add("Under Armour") # Agrega "Under Armour" al conjunto marcas_deportivas.
print(marcas_deportivas) # Imprime el conjunto actualizado: {'Nike', 'Adidas', 'Puma', 'Reebok', 'Under Armour'}.

#Agregar varios elementos de un conjunto utilizando el método update()
marcas_deportivas.update(["New Balance", "Asics", "Fila"]) # Agrega varios elementos al conjunto marcas_deportivas.
print(marcas_deportivas) # Imprime el conjunto actualizado: {'Nike', 'Adidas', 'Puma', 'Reebok', 'Under Armour', 'New Balance', 'Asics', 'Fila'}.

marcas_deportivas_colombianas = {"Totto", "Bosi", "Patprimo", "Columbia"}
marcas_deportivas.update(marcas_deportivas_colombianas) # Agrega los elementos del conjunto marcas_deportivas_colombianas al conjunto marcas_deportivas.
print(marcas_deportivas) # Imprime el conjunto actualizado: {'Nike', 'Adidas', 'Puma', 'Reebok', 'Under Armour', 'New Balance', 'Asics', 'Fila', 'Totto', 'Bosi', 'Patprimo', 'Columbia'}.

#Nota: La funcion update() puede recibir cualquier iterable, como listas, tuplas o diccionarios, y agregará todos los elementos de ese iterable al conjunto.

#Eliminar elementos de un conjunto utilizando el método remove()
marcas_deportivas.remove("Fila") # Elimina "Fila" del conjunto marcas_deportivas.
print(marcas_deportivas) # Imprime el conjunto actualizado: {'Nike', 'Adidas', 'Puma', 'Reebok', 'Under Armour', 'New Balance', 'Asics', 'Totto', 'Bosi', 'Patprimo', 'Columbia'}.

#Eliminar elementos de un conjunto utilizando el método discard()
marcas_deportivas.discard("Bosi") # Elimina "Bosi" del conjunto marcas_deportivas.
print(marcas_deportivas) # Imprime el conjunto actualizado: {'Nike', 'Adidas', 'Puma', 'Reebok', 'Under Armour', 'New Balance', 'Asics', 'Totto', 'Patprimo', 'Columbia'}.

#Diferencia entre remove() y discard(): Si el elemento a eliminar no está presente en el conjunto, remove() generará un error, mientras que discard() no generará ningún error.

#Eliminar un elemento aleatorio de un conjunto utilizando el método pop(): Este método elimina y devuelve un elemento aleatorio del conjunto. Dado que los conjuntos no están ordenados, no se puede predecir qué elemento se eliminará.
elemento_eliminado = marcas_deportivas.pop() # Elimina un elemento aleatorio del conjunto marcas_deportivas y lo asigna a la variable elemento_eliminado.
print(elemento_eliminado) # Imprime el elemento eliminado aleatoriamente.

#Eliminar todos los elementos de un conjunto utilizando el método clear(): Esta función elimina todos los elementos del conjunto, dejándolo vacío.
marcas_deportivas.clear() # Elimina todos los elementos del conjunto marcas_deportivas.
print(marcas_deportivas) # Imprime el conjunto vacío: set().

print("="*80)
print("Operaciones con conjuntos")
print(" ")
#Operaciones con conjuntos: Podemos realizar operaciones matemáticas con conjuntos, como la unión, intersección y diferencia, utilizando los métodos union(), intersection() y difference().

conjunto_a = {"a", "b", "c", "d", "e"}
conjunto_b = {"a", "i", "f", "g", "h"}

union = conjunto_a.union(conjunto_b) # Realiza la unión de los conjuntos conjunto_a y conjunto_b.
print(union) # Imprime el conjunto resultante de la unión: {'a', 'b', 'c', 'd', 'e', 'i', 'f', 'g', 'h'}.

interseccion = conjunto_a.intersection(conjunto_b) # Realiza la intersección de los conjuntos conjunto_a y conjunto_b.
print(interseccion) # Imprime el conjunto resultante de la intersección: {'a'}.

diferencia = conjunto_a.difference(conjunto_b) # Realiza la diferencia de los conjuntos conjunto_a y conjunto_b.
print(diferencia) # Imprime el conjunto resultante de la diferencia: {'b', 'c', 'd', 'e'}.
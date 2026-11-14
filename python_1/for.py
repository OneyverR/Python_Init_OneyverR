
#Ciclo For: El ciclo for en Python se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena) o cualquier objeto iterable. La sintaxis básica es la siguiente:

palabra = "Python"
for letra in palabra:
    print(letra) #Esto imprimirá cada letra de la palabra "Python" en una línea separada.
    
#For para recorrer una lista: Este ejemplo muestra cómo usar un bucle for para recorrer una lista de frutas y imprimir cada fruta en una línea separada. La variable fruta se utiliza como un iterador que toma el valor de cada elemento de la lista frutas en cada iteración del bucle.

frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)

#Breake en For para romper el Bucle: Este ejemplo muestra cómo usar un bucle for junto con una declaración if para recorrer una lista de frutas y imprimir cada fruta en una línea separada, pero romper el bucle cuando se encuentra la fruta "banana". La variable fruta1 se utiliza como un iterador que toma el valor de cada elemento de la lista frutas2 en cada iteración del bucle. Cuando fruta1 es igual a "banana", la declaración if se evalúa como verdadera y se ejecuta la instrucción break, lo que rompe el bucle y termina la ejecución del mismo. Por lo tanto, la fruta "banana" no se imprimirá.

frutas2 = ["manzana", "banana", "cereza"]

for fruta1 in frutas2: 
    if fruta1 == "banana":
        break
    print(fruta1)

#Ciclo for con continue: este ejemplo muestra cómo usar un bucle for junto con una declaración if para recorrer una lista de frutas y imprimir cada fruta en una línea separada, pero omitiendo la fruta "banana". La variable fruta se utiliza como un iterador que toma el valor de cada elemento de la lista frutas en cada iteración del bucle. Cuando fruta es igual a "banana", la declaración if se evalúa como verdadera y se ejecuta la instrucción continue, lo que hace que el bucle salte a la siguiente iteración sin ejecutar la instrucción print(fruta). Por lo tanto, la fruta "banana" no se imprimirá.

frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    if fruta == "banana":
        continue
    print(fruta)

# Ciclo For con Else: este ejemplo muestra cómo usar un bucle for junto con una declaración else para recorrer una lista de frutas y imprimir cada fruta en una línea separada, pero omitiendo la fruta "banana". La variable fruta se utiliza como un iterador que toma el valor de cada elemento de la lista frutas en cada iteración del bucle. Cuando fruta es igual a "banana", la declaración if se evalúa como verdadera y se ejecuta la instrucción continue, lo que hace que el bucle salte a la siguiente iteración sin ejecutar la instrucción print(fruta). Por lo tanto, la fruta "banana" no se imprimirá. Cuando el bucle for ha terminado de ejecutarse y se ha salido del bucle, se ejecuta el bloque de código dentro del else, que imprime un mensaje indicando que se ha recorrido toda la lista.

frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    if fruta == "banana":
        continue
    print(fruta)
else:
    print("Se ha recorrido toda la lista")

# Ciclo For en un rango de nuemros: este ejemplo muestra cómo usar un bucle for para recorrer un rango de números del 0 al 9 y imprimir cada número en una línea separada. La función range() se utiliza para generar una secuencia de números enteros, y el bucle for itera sobre cada número en esa secuencia.

for i in range(8,10):
    print(i)


for i in range(0,10,2): # El tercer parámetro de la función range() indica el paso o incremento entre cada número en la secuencia. En este caso, el bucle for imprimirá los números pares del 0 al 8 (0, 2, 4, 6, 8) en una línea separada.
    print(i)

#Bucle anidado: este ejemplo muestra cómo usar un bucle for anidado para recorrer dos listas y imprimir cada combinación de elementos en una línea separada. La variable fruta se utiliza como un iterador que toma el valor de cada elemento de la lista frutas en cada iteración del bucle externo, y la variable adjetivo se utiliza como un iterador que toma el valor de cada elemento de la lista adjetivos en cada iteración del bucle interno.
#Lista:
frutas = ["manzana", "banana", "cereza"]
adjetivos = ["roja", "grande", "deliciosa"]

for fruta in frutas:
    for adjetivo in adjetivos:
        print(fruta, adjetivo)

for adjetivo in adjetivos: 
    for fruta in frutas:
        print(fruta, adjetivo)

#pass: este ejemplo muestra cómo usar la instrucción pass en un bucle for. La instrucción pass no hace nada, pero es útil cuando se necesita una declaración sintácticamente válida, pero no se necesita ninguna acción.

for i in range(10):
    pass
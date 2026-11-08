
#Indice de un texto
#Slice de un texto
"""
En Python, un slice (rebanada) es una forma de seleccionar un subconjunto de elementos de una secuencia, como una cadena de texto, una lista o una tupla.
"""
texto = "Hola, este es un ejemplo de texto para calcular el índice de legibilidad."
print(texto[0])  # Imprime el primer carácter del texto

# Seleccionar el rango de un texto
print(texto[0:4])  # Imprime los primeros cuatro caracteres del texto
print(texto[5:10])  # Imprime los caracteres del índice 5 al 9 del texto


print(texto[:5])  # Imprime los primeros cinco caracteres del texto. En ese caso, el índice de inicio es 0 por defecto
print(texto[5:])  # Imprime todos los caracteres del texto a partir del índice 5 hasta el final del texto

#Indice negativo
print(texto[-1])  # Imprime el último carácter del texto
print(texto[-5:-1])  # Imprime los últimos cuatro caracteres del texto

#Reemplazo de un texto
curso = "Este curso de HTML y el HTML es muy interesante. Cada que uso HTML, aprendo algo nuevo."
print(curso.replace("HTML", "Python!"))  # Reemplaza "HTML" por "Python!" en la cadena de texto

#Separacion de un texto en una lista de palabras
frase4 = "Hola, este es un ejemplo de texto para separar en palabras"
listaPalabras = frase4.split(" ") # Separa el texto en palabras y las almacena en una lista, en la funcion split() se indica que separe el texto en cada espacio en blanco
print(listaPalabras)  #Imprime ['Hola,', 'este', 'es', 'un', 'ejemplo', 'de', 'texto', 'para', 'separar', 'en', 'palabras'], que es la lista de palabras separadas del texto

#Normalizacion de un texto

texto2 = "HOLA onEyVER roDRIGUEZ novoa, Es un EsTudiante De PAython"
print("estudiante".lower() in texto2.lower())  # Imprime True, ya que la palabra "estudiante" esta incluida en el texto, sin importar si esta en mayusculas o minusculas
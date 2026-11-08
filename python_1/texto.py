
#Impresiones de texto con comillas incluidas

print("Hola Mundo")  # Imprime Hola Mundo
#print("Hola "Mundo"") #Forma incorrecta de imprimir Hola Mundo con comillas incluidas}

#Forma correcta de imprimir Hola Mundo con comillas incluidas
print ("Hola 'mundo'")  # Imprime Hola 'Mundo'
print('"Hola Mundo"')  # Imprime "Hola Mundo"

frase_ingles = "I'm Oneyver Rodriguez"  # Forma correcta de imprimir I'm Oneyver Rodriguez con comillas incluidas
print(frase_ingles)  # Imprime I'm Oneyver Rodriguez

#Impresion de texto en multilinea
frase_multilinea = """Hola Mundo
Esta es una frase en multilinea
"""
print(frase_multilinea)  # Imprime Hola Mundo Esta es una frase en multiline

# Conocer informacion acerca del tamaño de un string
palabra = "Esternocreidomastoideo"
print(len(palabra))  # Imprime 22, que es la cantidad de caracteres que tiene la palabra Esternocreidomastoideo

#Cononcer si una palabra esta incluida en un string
frase = "Si me preguntaran que me gusta de ella"
estaIncluida = "gusta" in frase
print(estaIncluida)  # Imprime True, ya que la palabra "gusta" esta incluida en la frase

#Conocer si una palabra no esta incluida en un string
noEstaIncluida = "carro" not in frase
print(noEstaIncluida)  # Imprime True, ya que la palabra "carro" no esta incluida en la frase

#Transformar un string a mayusculas
frase2 = "Mañana tengo que trabajar"
frase2Mayusculas = frase2.upper()
print(frase2Mayusculas)  # Imprime MAÑANA TENGO QUE TRABAJAR

#Transformar un string a minusculas
frase3 = "EN LA EMPRESA NO TENGO NINGUNA ASIGNACION PENDIENTE"
frase3Minusculas = frase3.lower()
print(frase3Minusculas)  # Imprime en la empresa no tengo ninguna asignacion pendiente

#Eliminar Espacios en blanco al inicio y al final de un string
contraseña= "        1005037208Yl     "
sinEspacios = contraseña.strip()
print(sinEspacios)  # Imprime 1005037208Yl, ya que se eliminaron los espacios en blanco al inicio y al final del string
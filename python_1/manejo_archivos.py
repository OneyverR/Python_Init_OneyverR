# Manejo de archivos en Python: Un archivo es un contenedor de datos que se puede almacenar en un disco duro, una memoria USB o en la nube. Los archivos se pueden crear, leer, escribir y eliminar. En Python, se pueden manejar archivos utilizando la función open() y los métodos read(), write() y close().

#Metodo open(): La función open() se utiliza para abrir un archivo y devolver un objeto de archivo. La sintaxis de la función open() es la siguiente:
# open(nombre_del_archivo, modo)

#Funciones de manejo de archivos en Python:
# open(): Abre un archivo y devuelve un objeto de archivo.
# read(): Lee el contenido de un archivo y devuelve una cadena de texto.
# write(): Escribe contenido en un archivo.
# close(): Cierra un archivo.
# x (modo de apertura): Crea un archivo nuevo y lo abre para escritura. Si el archivo ya existe, se produce un error.

#Ejemplo de manejo de archivos en Python:
# try: 
#     f = open("archivo.txt", "r") #Abre el archivo "archivo.txt" en modo escritura. Si el archivo no existe, se crea un archivo nuevo.
#     print(f.readline()) #Lee el contenido del archivo "archivo.txt" y lo imprime en pantalla. En este caso, el archivo esta vacio, por lo que no se imprime nada.
#     f.close() #Cierra el archivo "archivo.txt".
# except FileNotFoundError: 
#     print("Error: El archivo no existe") #Si el archivo no existe, se imprime un mensaje de error.

#Uso de with para manejar archivos en Python: La sentencia with se utiliza para manejar archivos en Python. La sentencia with se encarga de abrir y cerrar el archivo automaticamente, evitando errores de manejo de archivos. La sintaxis de la sentencia with es la siguiente:
# with open(nombre_del_archivo, modo) as variable:

try:
    with open("archivo.txt", "r", encoding="utf-8") as f: #Abre el archivo "archivo.txt" en modo lectura. Si el archivo no existe, se crea un archivo nuevo.
        print(f.readline()) #Lee el contenido del archivo "archivo.txt" y lo imprime en pantalla. En este caso, el archivo esta vacio, por lo que no se imprime nada.
        print(f.readline())
except FileNotFoundError:
    print("Error: El archivo no existe") #Si el archivo no existe, se imprime un mensaje de error.

#Nota: es importanrte usar el parametro encoding="utf-8" para evitar errores de codificacion al leer archivos que contienen caracteres especiales.

#Como escribir en un archivo en Python: Para escribir en un archivo en Python, se debe abrir el archivo en modo escritura ("w") o en modo append ("a"). El modo escritura ("w") borra el contenido del archivo si ya existe, mientras que el modo append ("a") agrega contenido al final del archivo sin borrar el contenido existente.

try:
    with open("archivo.txt", "w", encoding="utf-8") as f: #Abre el archivo "archivo.txt" en modo escritura. Si el archivo no existe, se crea un archivo nuevo.
        f.write("Hola, soy un archivo de texto\n") #Escribe el contenido en el archivo "archivo.txt".
        f.write("Este es un ejemplo de manejo de archivos en Python\n") #Escribe el contenido en el archivo "archivo.txt".
    with open("archivo.txt", "r", encoding="utf-8") as f: #Abre el archivo "archivo.txt" en modo lectura. Si el archivo no existe, se crea un archivo nuevo.
        print(f.readline()) #Lee el contenido del archivo "archivo.txt" y lo imprime en pantalla.
        print(f.readline()) #Lee el contenido del archivo "archivo.txt" y lo imprime en pantalla.
except FileNotFoundError:
    print("Error: El archivo no existe") #Si el archivo no existe, se imprime un mensaje de error.

#Como agregar contenido a un archivo en Python: Para agregar contenido a un archivo en Python, se debe abrir el archivo en modo append ("a"). El modo append ("a") agrega contenido al final del archivo sin borrar el contenido existente.
try:
    with open("archivo.txt", "a", encoding="utf-8") as f: #Abre el archivo "archivo.txt" en modo append. Si el archivo no existe, se crea un archivo nuevo.
        f.write("Este es un ejemplo de agregado de contenido a un archivo en Python\n") #Agrega contenido al final del archivo "archivo.txt".
    with open("archivo.txt", "r", encoding="utf-8") as f: #Abre el archivo "archivo.txt" en modo lectura. Si el archivo no existe, se crea un archivo nuevo.
        print(f.readline()) #Lee el contenido del archivo "archivo.txt" y lo imprime en pantalla.
        print(f.readline()) #Lee el contenido del archivo "archivo.txt" y lo imprime en pantalla.
        print(f.readline()) #Lee el contenido del archivo "archivo.txt" y lo imprime en pantalla.
except FileNotFoundError:
    print("Error: El archivo no existe") #Si el archivo no existe, se imprime un mensaje de error.

#Creacion de un archivo en Python: Para crear un archivo en Python, se debe abrir el archivo en modo escritura ("w") o en modo append ("a"). Si el archivo no existe, se crea un archivo nuevo. Si el archivo ya existe, se borra el contenido del archivo si se abre en modo escritura ("w") o se agrega contenido al final del archivo si se abre en modo append ("a").

try:
    with open("archivo_nuevo.txt", "r", encoding="utf-8") as f: #Abre el archivo "archivo_nuevo.txt" en modo lectura. Si el archivo no existe, se crea un archivo nuevo.
        print(f.readline()) #Lee el contenido del archivo "archivo_nuevo.txt" y lo imprime en pantalla.
        print(f.readline()) #Lee el contenido del archivo "archivo_nuevo.txt" y lo imprime en pantalla.
except FileNotFoundError:
    open("archivo_nuevo.txt", "x") #Si el archivo no existe, se crea un archivo nuevo.

try:
    with open("archivo_nuevo.txt", "a", encoding="utf-8") as f: #Abre el archivo "archivo_nuevo.txt" en modo append. Si el archivo no existe, se crea un archivo nuevo.
        f.write("Este es un ejemplo de creacion de un archivo en Python") #Agrega contenido al final del archivo "archivo_nuevo.txt".
        with open("archivo_nuevo.txt", "r", encoding="utf-8") as f: #Abre el archivo "archivo_nuevo.txt" en modo lectura. Si el archivo no existe, se crea un archivo nuevo.
            print(f.readline()) #Lee el contenido del archivo "archivo_nuevo.txt" y lo imprime en pantalla.
            print(f.readline()) #Lee el contenido del archivo "archivo_nuevo.txt" y lo imprime en pantalla.
except FileNotFoundError:
    print("Error: El archivo no existe") #Si el archivo no existe, se imprime un mensaje de error.
"""
Reto 22 — Manejo de archivos (con try/except)
=============================================

En manejo_archivos.py abriste archivos con 'with open(...)', leíste su contenido
y manejaste el caso de que el archivo no existiera (FileNotFoundError).

Tu tarea: completa 'contar_lineas' para que DEVUELVA cuántas líneas tiene el
archivo que está en 'ruta'.

Caso borde: si el archivo NO existe, devuelve 0 (captura el error, no dejes que
el programa se rompa).

Ejemplos:
    - un archivo con 3 líneas       -> 3
    - un archivo vacío              -> 0
    - una ruta que no existe        -> 0
"""


def contar_lineas(ruta):
    try:
        with open(ruta, "r", encoding= "utf-8") as f:
            lineas = f.readlines()
            return len(lineas)
    except FileNotFoundError:
        return 0

print(contar_lineas("archivo.txt"))
    

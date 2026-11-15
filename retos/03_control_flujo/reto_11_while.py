"""
Reto 11 — Bucle while
=====================

En while.py repetiste un bloque mientras una condición era verdadera,
avanzando una variable en cada vuelta (recuerda el operador +=).

Datos de partida (no los cambies):
    n = 100

Tu tarea: suma todos los números enteros desde 1 hasta n (incluido)
y guarda el total en 'suma'. Hazlo con un bucle while.

Para n = 100 el resultado esperado es:
    suma -> 5050

Cuidado: asegúrate de que la condición del while llegue a ser falsa,
o el bucle no terminará.
"""

# Datos de partida (no los modifiques)
n = 100

# TODO: con un while, acumula en 'suma' los enteros de 1 a n.
# Piensa: necesitas un valor inicial para 'suma' y una variable que
# avance en cada vuelta hasta pasar de n.

suma = 0
i = 1
while i <= n:
    suma += i
    i += 1
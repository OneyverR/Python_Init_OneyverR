"""
Reto 12 — Bucle for con range()
===============================

En for.py recorriste secuencias y usaste range(inicio, fin, paso).
Recuerda que range(1, 5) genera 1, 2, 3, 4 (el final NO se incluye).

Datos de partida (no los cambies):
    numero = 5

Tu tarea: calcula el factorial de numero (5! = 5 * 4 * 3 * 2 * 1)
usando un for con range(), y guárdalo en 'factorial'.

Para numero = 5 el resultado esperado es:
    factorial -> 120
"""

# Datos de partida (no los modifiques)
numero = 5

# TODO: con un for y range(), ve multiplicando y acumulando en 'factorial'.
# Piensa: ¿con qué valor conviene empezar 'factorial' si vas a MULTIPLICAR?
factorial = 1

for n_factorial in range(1, numero + 1, 1):
    factorial *= n_factorial
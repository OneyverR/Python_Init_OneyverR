"""
Reto 01 — Asignación múltiple
=============================

Python permite intercambiar dos valores SIN usar una variable temporal,
gracias a la asignación múltiple:  a, b = b, a

Partes de datos ya definidas (no las cambies):
    a = 5
    b = 9

Tu tarea: crea dos variables, `a_nuevo` y `b_nuevo`, que contengan los
valores de `a` y `b` INTERCAMBIADOS, usando asignación múltiple en una
sola línea.

Resultado esperado:
    a_nuevo  ->  9   (el valor que tenía b)
    b_nuevo  ->  5   (el valor que tenía a)
"""

# Datos de partida (no los modifiques)
a = 5
b = 9

a_nuevo = None
b_nuevo = None

a_nuevo, b_nuevo = b, a



"""
Reto 15 — Tuplas (desempaquetado e inmutabilidad)
=================================================

En tuplas.py viste que una tupla es INMUTABLE (no se puede cambiar), que puedes
desempaquetarla en variables (x, y = mi_tupla) y que, para "modificarla", el
truco es: convertirla a lista, cambiar la lista y volver a convertir a tupla.

Datos de partida (no los cambies):
    punto = (10, 20, 30)

Tu tarea:
    1. Desempaqueta 'punto' en tres variables: x, y, z.
    2. Crea 'punto_ampliado' que sea 'punto' pero con un 40 añadido al final.
       Recuerda: no puedes añadir a una tupla directamente; usa el truco.

Resultado esperado:
    x, y, z         -> 10, 20, 30
    punto_ampliado  -> (10, 20, 30, 40)   (y debe seguir siendo una tupla)
"""

# Datos de partida (no los modifiques)
punto = (10, 20, 30)

# TODO 1: desempaqueta punto en x, y, z
x = None
y = None
z = None

x,y,z = punto

# TODO 2: crea punto_ampliado = punto con un 40 al final (sigue siendo tupla)
punto_ampliado = None

punto_ampliado = list(punto)
punto_ampliado.append(40)
punto_ampliado = tuple(punto_ampliado)

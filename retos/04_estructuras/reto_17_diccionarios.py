"""
Reto 17 — Diccionarios (acceso, pertenencia y recorrido)
========================================================

En diccionarios.py accediste a valores por su clave, comprobaste si una clave
existe con el operador in, y recorriste los valores con un for sobre .values().

Datos de partida (no los cambies):
    jugador = {"goles": 2, "asistencias": 1, "minutos": 90}

Tu tarea:
    1. goles         -> el valor de la clave "goles".
    2. tiene_tarjetas-> ¿existe la clave "tarjetas" en el diccionario? (True/False)
    3. suma_total    -> la suma de TODOS los valores del diccionario.

Resultado esperado:
    goles          -> 2
    tiene_tarjetas -> False     (esa clave no existe)
    suma_total     -> 93        (2 + 1 + 90)
"""

# Datos de partida (no los modifiques)
jugador = {"goles": 2, "asistencias": 1, "minutos": 90}

# TODO 1: accede al valor de la clave "goles"
goles = None
goles = jugador["goles"]

# TODO 2: ¿existe la clave "tarjetas"? (debe quedar True o False)
tiene_tarjetas = None
tiene_tarjetas = "tarjetas" in jugador

# TODO 3: suma todos los valores del diccionario recorriéndolos con un for
#         (piensa con qué valor empezar la suma, como en los acumuladores)
suma_total = 0
for v in jugador.values():
    suma_total += v
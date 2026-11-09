"""
Reto 04 — Operadores aritméticos
================================

Repasa los operadores que viste en operadores.py:
    //  división entera (el cociente, sin decimales)
    %   módulo (el residuo de la división)
    **  exponente

Datos de partida (no los cambies):
    a = 17
    b = 5

Tu tarea: crea las tres variables pedidas.

Resultados esperados:
    cociente_entero  ->  3       (el cociente entero de a entre b)
    residuo          ->  2       (lo que sobra al dividir a entre b)
    es_divisible     ->  False   (¿a cabe exacto en b, sin que sobre nada?)
"""

# Datos de partida (no los modifiques)
a = 17
b = 5

# TODO 1: calcula el cociente entero de a entre b
cociente_entero = a // b
print(cociente_entero)

# TODO 2: calcula lo que sobra (el residuo) al dividir a entre b
residuo = a % b

# TODO 3: ¿a es divisible por b? (debe quedar True o False)
# Piensa: ¿qué valor tendría el residuo si a cupiera exacto en b?
es_divisible = a % b == 0

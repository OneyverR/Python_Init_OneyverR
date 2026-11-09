"""
Reto 05 — Comparaciones y booleanos
===================================

Las comparaciones (==, !=, >, <, >=, <=) devuelven un booleano (True/False).
Y con bool() puedes convertir otros valores: en booleanos.py viste que una
cadena vacía "" se considera False, y una con contenido, True.

Datos de partida (no los cambies):
    numero = 42
    edad = 17
    texto_vacio = ""

Tu tarea: crea las tres variables pedidas (todas deben quedar en True o False).

Resultados esperados:
    es_par           ->  True    (¿numero es par?)
    es_mayor_edad    ->  False   (¿la persona ya es mayor de edad?)
    vacio_es_truthy  ->  False   (¿una cadena vacía cuenta como verdadera?)
"""

# Datos de partida (no los modifiques)
numero = 42
edad = 17
texto_vacio = ""

# TODO 1: ¿numero es par? (debe quedar True o False)
# Piensa: un número es par cuando al dividirlo entre 2 no sobra nada.
es_par = numero % 2 == 0

# TODO 2: ¿la edad llega al mínimo de 18 para ser mayor de edad? (True/False)
es_mayor_edad = edad >= 18

# TODO 3: ¿una cadena vacía se considera verdadera? Conviértela a booleano.
vacio_es_truthy = bool(texto_vacio)

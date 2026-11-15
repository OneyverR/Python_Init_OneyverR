"""
Reto 09 — Operadores lógicos (and / or / not)
=============================================

En operadores-logicos.py combinaste condiciones con and, or y not.

Datos de partida (no los cambies):
    edad = 20
    tiene_licencia = True

Tu tarea (ambas deben quedar en True o False):
    puede_conducir         -> ¿es mayor o igual a 18 Y además tiene licencia?
    es_menor_sin_licencia  -> ¿es menor de 18 O no tiene licencia?

Resultados esperados (para los datos de arriba):
    puede_conducir         -> True
    es_menor_sin_licencia  -> False
"""

# Datos de partida (no los modifiques)
edad = 20
tiene_licencia = True

# TODO 1: combina las dos condiciones con el operador que exige que AMBAS se cumplan
puede_conducir = None
if  edad >= 18 and tiene_licencia:
    puede_conducir = True
else:
    puede_conducir = False
print(puede_conducir)

# TODO 2: combina con el operador que se cumple si AL MENOS UNA es cierta.
#         Una de las dos partes necesita negar 'tiene_licencia'.
es_menor_sin_licencia = None

if edad < 18 or not tiene_licencia:
    es_menor_sin_licencia = True
else: 
    es_menor_sin_licencia = False
print(es_menor_sin_licencia)
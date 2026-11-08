"""
Reto 03 — Manipulación de texto
===============================

Implementa `normalizar_usuario(texto)` que prepare un nombre de usuario:

    1. Elimina los espacios en blanco al inicio y al final.
    2. Pasa todo a minúsculas.

Importante: `strip()` solo quita los espacios de los EXTREMOS, no los
internos. "  Juan Perez  " debe quedar "juan perez" (el espacio del medio
se conserva).

Ejemplos:
    normalizar_usuario("  Oneyver  ")      -> "oneyver"
    normalizar_usuario("JUAN PEREZ")       -> "juan perez"
    normalizar_usuario("\tAna\n")          -> "ana"

Pista: encadena los métodos .strip() y .lower().
"""


def normalizar_usuario(texto):
    # TODO: quita espacios de los extremos y pasa a minúsculas
    pass

"""
Reto 02 — Tipos de datos (con una trampa clásica)
=================================================

Implementa `clasificar(valor)` que devuelva, como string, el tipo del valor:

    "booleano" | "entero" | "flotante" | "complejo" | "texto"

⚠️ Trampa profesional: en Python `bool` es una SUBCLASE de `int`, así que
`isinstance(True, int)` es `True`. Si compruebas el entero antes que el
booleano, clasificarás `True` como "entero". Comprueba el booleano PRIMERO.

Ejemplos:
    clasificar(True)     -> "booleano"
    clasificar(10)       -> "entero"
    clasificar(3.14)     -> "flotante"
    clasificar(2 + 3j)   -> "complejo"
    clasificar("hola")   -> "texto"

Pista: usa isinstance() y ordena bien las comprobaciones.
"""


def clasificar(valor):
    # TODO: devuelve el nombre del tipo. Recuerda: bool antes que int.
    pass

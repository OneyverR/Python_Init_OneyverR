"""
Reto 20 — Lambda (la fábrica de funciones)
==========================================

En lambda.py viste que una función puede DEVOLVER otra función (una lambda).
Por ejemplo, fabrica_funciones(n) devolvía  lambda x: x * n.

Tu tarea: completa 'crear_multiplicador' para que DEVUELVA una función (lambda)
que multiplique su argumento por 'n'.

Ejemplos esperados:
    triple = crear_multiplicador(3)
    triple(5)                 -> 15

    crear_multiplicador(2)(10) -> 20
    crear_multiplicador(0)(99) -> 0
"""


def crear_multiplicador(n):
    # TODO: devuelve una función lambda que reciba un número y lo multiplique por n.
    pass

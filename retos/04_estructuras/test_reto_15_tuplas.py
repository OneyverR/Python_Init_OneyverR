from reto_15_tuplas import x, y, z, punto_ampliado


def test_desempaquetado():
    assert x == 10
    assert y == 20
    assert z == 30


def test_punto_ampliado_contenido():
    assert punto_ampliado == (10, 20, 30, 40)


def test_sigue_siendo_tupla():
    # Caso borde: el resultado debe ser una tupla, no una lista
    assert isinstance(punto_ampliado, tuple)

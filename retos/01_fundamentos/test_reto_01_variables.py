from reto_01_variables import intercambiar


def test_intercambia_numeros():
    assert intercambiar(1, 2) == (2, 1)


def test_intercambia_strings():
    assert intercambiar("x", "y") == ("y", "x")


def test_intercambia_tipos_distintos():
    assert intercambiar(3.5, True) == (True, 3.5)


def test_devuelve_una_tupla():
    assert isinstance(intercambiar(1, 2), tuple)

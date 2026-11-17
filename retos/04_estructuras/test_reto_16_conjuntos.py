from reto_16_conjuntos import total_python, en_ambos, solo_python


def test_cuenta_unicos_sin_duplicado():
    # Caso borde: "Ana" está repetida, pero un set no cuenta duplicados -> 3, no 4
    assert total_python == 3


def test_interseccion():
    assert en_ambos == {"Luis", "Marta"}


def test_diferencia():
    assert solo_python == {"Ana"}

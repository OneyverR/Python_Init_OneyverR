from reto_06_slicing import primera, ultima, primeras_tres


def test_primer_caracter():
    assert primera == "P"


def test_ultimo_caracter():
    assert ultima == "n"


def test_primeras_tres_letras():
    assert primeras_tres == "Pyt"

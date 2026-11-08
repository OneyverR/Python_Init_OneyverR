from reto_03_texto import frase, usuario, longitud, tiene_python


def test_usuario_limpio_y_en_minusculas():
    assert usuario == "oneyver_dev"


def test_longitud_de_la_frase():
    assert longitud == 28
    assert longitud == len(frase)


def test_contiene_la_palabra_python():
    assert tiene_python is True

from reto_05_booleanos import es_par, es_mayor_edad, vacio_es_truthy


def test_numero_es_par():
    assert es_par is True


def test_no_es_mayor_de_edad():
    assert es_mayor_edad is False


def test_cadena_vacia_es_falsa():
    assert vacio_es_truthy is False

from reto_17_diccionarios import goles, tiene_tarjetas, suma_total


def test_acceso_por_clave():
    assert goles == 2


def test_clave_inexistente_es_falsa():
    # Caso borde: "tarjetas" no está en el diccionario
    assert tiene_tarjetas is False


def test_suma_de_valores():
    assert suma_total == 93

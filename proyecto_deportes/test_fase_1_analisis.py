from fase_1_analisis import goles_local, nombre_goleador, resultado


def test_goles_local_suma_la_plantilla():
    assert goles_local == 3


def test_maximo_goleador():
    assert nombre_goleador == "Dorlan Pabón"


def test_resultado_del_partido():
    assert resultado == "Victoria local"

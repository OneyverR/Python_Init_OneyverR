from reto_01_variables import a, b, a_nuevo, b_nuevo


def test_a_nuevo_toma_el_valor_de_b():
    assert a_nuevo == 9


def test_b_nuevo_toma_el_valor_de_a():
    assert b_nuevo == 5


def test_realmente_estan_intercambiados():
    # a_nuevo debe tener lo de b, y b_nuevo lo de a
    assert a_nuevo == b
    assert b_nuevo == a

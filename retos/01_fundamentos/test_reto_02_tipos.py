from reto_02_tipos import precio_entero, flotante_truncado, entero_flotante


def test_texto_a_entero():
    assert precio_entero == 1500
    assert isinstance(precio_entero, int)


def test_flotante_se_trunca_a_entero():
    # 9.99 -> 9 (NO 10: int() trunca, no redondea)
    assert flotante_truncado == 9
    assert isinstance(flotante_truncado, int)


def test_entero_a_flotante():
    assert entero_flotante == 7.0
    assert isinstance(entero_flotante, float)

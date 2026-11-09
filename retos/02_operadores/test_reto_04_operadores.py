from reto_04_operadores import cociente_entero, residuo, es_divisible


def test_cociente_entero():
    assert cociente_entero == 3


def test_residuo():
    assert residuo == 2


def test_es_divisible_da_falso():
    # 17 no es divisible por 5, así que el residuo (2) no es 0
    assert es_divisible is False

from reto_02_tipos import clasificar


def test_booleano_antes_que_entero():
    # La trampa: True NO debe clasificarse como "entero"
    assert clasificar(True) == "booleano"
    assert clasificar(False) == "booleano"


def test_entero():
    assert clasificar(10) == "entero"
    assert clasificar(-5) == "entero"


def test_flotante():
    assert clasificar(3.14) == "flotante"


def test_complejo():
    assert clasificar(2 + 3j) == "complejo"


def test_texto():
    assert clasificar("hola") == "texto"

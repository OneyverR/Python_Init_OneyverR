from reto_07_replace_split import corregida, palabras, num_palabras


def test_reemplazo_java_por_python():
    assert corregida == "Me gusta Python y programar en Python"


def test_separa_en_palabras():
    assert palabras == ["Me", "gusta", "Java", "y", "programar", "en", "Java"]


def test_cuenta_palabras():
    assert num_palabras == 7

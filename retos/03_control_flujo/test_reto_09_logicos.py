from reto_09_logicos import puede_conducir, es_menor_sin_licencia


def test_puede_conducir():
    assert puede_conducir is True


def test_no_es_menor_sin_licencia():
    assert es_menor_sin_licencia is False

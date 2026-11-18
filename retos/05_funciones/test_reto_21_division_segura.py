import pytest

from reto_21_division_segura import division_segura


@pytest.mark.parametrize("a, b, esperado", [
    (10, 2, 5.0),
    (9, 3, 3.0),
    (0, 5, 0.0),     # caso borde: 0 en el numerador NO es un error
    (7, 2, 3.5),
])
def test_division_normal(a, b, esperado):
    assert division_segura(a, b) == esperado


def test_division_entre_cero_devuelve_none():
    # Caso borde: dividir entre cero debe devolver None, no romper el programa
    assert division_segura(10, 0) is None

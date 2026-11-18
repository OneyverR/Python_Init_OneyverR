import pytest

from reto_20_lambda import crear_multiplicador


@pytest.mark.parametrize("n, x, esperado", [
    (3, 5, 15),
    (2, 10, 20),
    (0, 99, 0),     # caso borde: multiplicar por 0
    (5, 0, 0),      # caso borde: el argumento es 0
    (4, -2, -8),    # caso borde: negativos
])
def test_crear_multiplicador(n, x, esperado):
    multiplicador = crear_multiplicador(n)
    assert multiplicador(x) == esperado


def test_devuelve_una_funcion():
    # Debe devolver algo que se pueda llamar como función
    assert callable(crear_multiplicador(2))

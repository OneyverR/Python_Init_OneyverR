import pytest

from reto_19_promedio import promedio


@pytest.mark.parametrize("numeros, esperado", [
    ([10, 20, 30], 20.0),
    ([5], 5.0),
    ([2, 4], 3.0),
    ([0, 0, 0], 0.0),
])
def test_promedio(numeros, esperado):
    assert promedio(numeros) == esperado


def test_lista_vacia_devuelve_cero():
    # Caso borde: lista vacía, no debe fallar por dividir entre cero
    assert promedio([]) == 0

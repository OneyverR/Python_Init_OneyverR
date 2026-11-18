import pytest

from reto_18_funciones import aplicar_descuento


@pytest.mark.parametrize("precio, descuento, esperado", [
    (200, 50, 100.0),
    (100, 0, 100.0),    # caso borde: 0% de descuento no cambia el precio
    (0, 10, 0.0),       # caso borde: precio 0
    (50, 100, 0.0),     # caso borde: 100% de descuento deja 0
])
def test_aplicar_descuento(precio, descuento, esperado):
    assert aplicar_descuento(precio, descuento) == esperado


def test_descuento_por_defecto():
    # Si no se pasa 'descuento', debe usar 10%
    assert aplicar_descuento(100) == 90.0

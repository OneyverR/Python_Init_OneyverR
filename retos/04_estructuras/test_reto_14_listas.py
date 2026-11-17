from reto_14_listas import equipo, total


def test_orden_final_correcto():
    # El orden importa: "Entrenador" al inicio, "Mediocampista" al final
    assert equipo == ["Entrenador", "Portero", "Defensa", "Delantero", "Mediocampista"]


def test_entrenador_va_primero():
    # Caso borde: insertar al principio, no al final
    assert equipo[0] == "Entrenador"


def test_mediocampista_va_ultimo():
    assert equipo[-1] == "Mediocampista"


def test_total_de_miembros():
    assert total == 5

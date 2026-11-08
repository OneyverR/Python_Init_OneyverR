from reto_03_texto import normalizar_usuario


def test_quita_espacios_extremos():
    assert normalizar_usuario("  Oneyver  ") == "oneyver"


def test_pasa_a_minusculas():
    assert normalizar_usuario("JUAN PEREZ") == "juan perez"


def test_conserva_espacio_interno():
    # strip() NO toca los espacios del medio
    assert normalizar_usuario("  Luis Garcia  ") == "luis garcia"


def test_tabs_y_saltos_de_linea():
    assert normalizar_usuario("\tAna\n") == "ana"

from reto_22_archivos import contar_lineas


def test_cuenta_tres_lineas(tmp_path):
    archivo = tmp_path / "datos.txt"
    archivo.write_text("uno\ndos\ntres\n", encoding="utf-8")
    assert contar_lineas(str(archivo)) == 3


def test_archivo_vacio(tmp_path):
    archivo = tmp_path / "vacio.txt"
    archivo.write_text("", encoding="utf-8")
    assert contar_lineas(str(archivo)) == 0


def test_archivo_inexistente(tmp_path):
    # Caso borde: la ruta no existe -> debe devolver 0, no romper
    ruta = tmp_path / "no_existe.txt"
    assert contar_lineas(str(ruta)) == 0

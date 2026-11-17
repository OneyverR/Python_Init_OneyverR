# Retos — 04 Estructuras de datos

Refuerzan tus 4 temas nuevos: **listas, tuplas, conjuntos y diccionarios**.

| Reto | Archivo | Concepto |
|------|---------|----------|
| 14 | `reto_14_listas.py` | métodos de lista (`append`, `insert`, `len`) |
| 15 | `reto_15_tuplas.py` | desempaquetado e inmutabilidad |
| 16 | `reto_16_conjuntos.py` | unicidad, intersección y diferencia |
| 17 | `reto_17_diccionarios.py` | acceso, `in` y recorrer valores |

## Novedad: casos borde

A partir de este bloque, los tests incluyen **casos borde** a propósito (lo que pediste):
duplicados en conjuntos, una clave que no existe, el orden al insertar, el tipo del
resultado... Son justo las trampas donde un "pasa por suerte" fallaría. Si un test
con nombre como `test_clave_inexistente_es_falsa` o `test_cuenta_unicos_sin_duplicado`
se te pone rojo, ahí está tu aprendizaje.

## Cómo resolverlos

1. Abre el archivo `reto_XX_*.py` y lee el enunciado (docstring de arriba).
2. Completa los `# TODO`.
3. Corre los tests:

```bash
pytest retos/04_estructuras -v
```

> Empiezan en rojo porque las variables valen `None`. Ese es el punto de partida.

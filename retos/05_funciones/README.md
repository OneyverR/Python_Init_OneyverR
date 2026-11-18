# Retos — 05 Funciones y manejo de errores

Refuerzan tu gran salto: **funciones, lambda, try/except y manejo de archivos**.

| Reto | Archivo | Concepto |
|------|---------|----------|
| 18 | `reto_18_funciones.py` | `def`, `return`, parámetro por defecto |
| 19 | `reto_19_promedio.py` | función que procesa una lista (caso borde: vacía) |
| 20 | `reto_20_lambda.py` | lambda / función que devuelve una función |
| 21 | `reto_21_division_segura.py` | `try`/`except` |
| 22 | `reto_22_archivos.py` | `with open(...)` + manejo de error |

## Novedad: ahora resuelves FUNCIONES

Hasta ahora reemplazabas un `None` a nivel de módulo. Desde este bloque
**completas una función** (rellenas el cuerpo del `def`). Eso permite algo
importante: los tests te prueban con **muchos datos distintos** a la vez
(`@pytest.mark.parametrize`), que es el entrenamiento de casos borde de verdad.

Abre un test y verás varias filas de datos: cada una es un escenario, incluidos
los borde (lista vacía, división por cero, archivo inexistente, 0%, negativos).

> **Módulos:** cada test hace `from reto_XX import ...`. Eso ES importar un
> módulo — justo lo que practicaste en `python_1/modulos/`.

## Cómo resolverlos

1. Abre el archivo `reto_XX_*.py` y lee el enunciado (docstring).
2. Completa el cuerpo de la función (reemplaza el `pass`).
3. Corre los tests:

```bash
pytest retos/05_funciones -v
```

> Empiezan en rojo porque la función devuelve `None`. Ese es el punto de partida.

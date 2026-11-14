# Retos — 03 Control de flujo

Refuerzan tu salto al control de flujo: **condicionales, operadores lógicos,
`match`, `while` y `for`**. (Siguen sin funciones — eso llega en su módulo.)

| Reto | Archivo | Concepto |
|------|---------|----------|
| 08 | `reto_08_condicionales.py` | `if` / `elif` / `else` |
| 09 | `reto_09_logicos.py` | `and`, `or`, `not` |
| 10 | `reto_10_match.py` | `match` / `case` |
| 11 | `reto_11_while.py` | bucle `while` + acumulador |
| 12 | `reto_12_for_range.py` | `for` con `range()` |
| 13 | `reto_13_for_lista.py` | `for` sobre lista + `if` |

## Cómo resolverlos

1. Abre el archivo `reto_XX_*.py` y lee el enunciado (docstring de arriba).
2. Reemplaza el `None` por tu solución. En los bucles, escribirás varias líneas
   (inicializar la variable + el bucle que la va actualizando).
3. Corre los tests:

```bash
pytest retos/03_control_flujo -v
```

> **Importante:** aquí los tests comprueban el *resultado*, pero el valor del
> ejercicio está en que **tú escribas el `if` o el bucle**. Resolverlo a mano
> (poniendo el número final directo) pasa el test pero no te enseña nada. 😉
>
> Y ojo con los `while`: si la condición nunca se vuelve falsa, el programa se
> queda colgado. Asegúrate de que la variable avance en cada vuelta.

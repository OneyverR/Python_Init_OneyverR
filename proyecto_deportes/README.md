# 🏟️ Proyecto: Analizador Deportivo

Un **único proyecto que crece contigo**. Arranca modelando datos de fútbol con
estructuras básicas y, fase a fase, incorpora cada tema nuevo de la ruta hasta
llegar a análisis de datos y Machine Learning.

La idea pedagógica: el código "feo y manual" de la Fase 0 lo vas **refactorizando**
en las siguientes fases. Ese refactor *es* el aprendizaje.

## Fases

| Fase | Refuerza | Qué construyes | Estado |
|------|----------|----------------|--------|
| **0** | variables, tipos, listas, diccionarios, f-strings | Modelas jugadores y un partido; imprimes un resumen | 🟢 Hecha |
| **1** | control de flujo (`if`, `for`) | Calcula goles del equipo, máximo goleador y resultado | 🟡 En curso |
| 2 | funciones | Refactorizas la lógica en funciones reutilizables | ⚪ |
| 2 | funciones | Refactorizas la lógica en funciones reutilizables | ⚪ |
| 3 | ficheros + errores | Lees los datos desde un CSV real | ⚪ |
| 4 | NumPy / pandas | Estadísticas: medias, tablas, agrupaciones | ⚪ |
| 5 | matplotlib | Gráficos de rendimiento | ⚪ |
| 6 | scikit-learn | Modelo que predice el resultado de un partido | ⚪ |

## Ejecutar la fase actual

```bash
python proyecto_deportes/fase_1_analisis.py
```

Y para verificar tu solución de la Fase 1:

```bash
pytest proyecto_deportes -v
```

La Fase 1 es **guiada**: abre `fase_1_analisis.py` y completa los 4 `# TODO`
con `for` e `if`. Cuando los 3 tests estén en verde, la fase está superada.

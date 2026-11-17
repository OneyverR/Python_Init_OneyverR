# 🐍 Ruta Python — Oneyver Rodriguez

Repositorio de aprendizaje **progresivo y profesional** de Python, con la meta de
especializarme en **Ciencia de Datos**. Alineado con la *Ruta de aprendizaje de
Python en Platzi*.

Aquí conviven tres cosas que crecen juntas:

1. **Apuntes de práctica** — un archivo `.py` por concepto, autodocumentado (`python_1/`).
2. **Retos con tests** — ejercicios que se superan poniendo los tests en verde (`pytest`).
3. **Un proyecto profesional que evoluciona** — el *Analizador Deportivo*, que va
   incorporando cada tema nuevo.

> **Progreso actual:** 4 bloques de retos (17 retos) · Proyecto deportivo en Fase 1 ✅

---

## 🗺️ Roadmap

| # | Módulo | Estado |
|---|--------|--------|
| 1 | Fundamentos (variables, tipos, strings, números) | ✅ |
| 2 | Operadores y control de flujo (`if`, `match`, `for`, `while`) | ✅ |
| 4 | Estructuras de datos (listas, tuplas, sets, dicts) | ✅ |
| 3 | Funciones y manejo de errores | ⏭️ Siguiente |
| 5 | Ficheros, módulos y entornos virtuales | ⚪ Pendiente |
| 6 | Pruebas (pytest) y POO | ⚪ Pendiente |
| 7 | NumPy | ⚪ Pendiente |
| 8 | pandas | ⚪ Pendiente |
| 9 | Visualización (matplotlib / seaborn) | ⚪ Pendiente |
| 10 | Estadística y Machine Learning (scikit-learn) | ⚪ Pendiente |

---

## 🧩 Bloques de retos

| Bloque | Carpeta | Temas | Retos |
|--------|---------|-------|-------|
| 1 | `retos/01_fundamentos/` | variables, tipos, strings | 01–03 |
| 2 | `retos/02_operadores/` | operadores, booleanos, slicing | 04–07 |
| 3 | `retos/03_control_flujo/` | `if`/`elif`/`else`, `match`, `while`, `for` | 08–13 |
| 4 | `retos/04_estructuras/` | listas, tuplas, conjuntos, diccionarios | 14–17 |

> Desde el Bloque 4, los tests incluyen **casos borde** a propósito (duplicados,
> claves inexistentes, fronteras, tipos) para entrenar la detección de bugs que
> un solo dato no revela.

---

## 📁 Estructura

```
Python/
├── python_1/              # Apuntes por concepto (fundamentos → estructuras)
├── retos/                 # Retos con tests (pytest)
│   ├── 01_fundamentos/
│   ├── 02_operadores/
│   ├── 03_control_flujo/
│   └── 04_estructuras/
├── proyecto_deportes/     # El Analizador Deportivo (crece por fases)
├── docs/                  # Web de retos (GitHub Pages)
├── .vscode/               # Configuración del editor (pytest, UTF-8)
├── requirements.txt
└── README.md
```

---

## ⚙️ Puesta en marcha

```bash
# 1. Entorno virtual (una sola vez)
python -m venv .venv

# 2. Activarlo (Windows PowerShell)
.venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r requirements.txt
```

---

## ✅ Cómo resolver un reto

1. Abre la web (`docs/index.html`) o el `README` de la carpeta del bloque para leer el **enunciado**.
2. Completa el `# TODO` en `retos/<bloque>/reto_XX_*.py`.
3. Ejecuta los tests (todos, o solo un bloque):

```bash
pytest retos -v                     # todos los retos
pytest retos/04_estructuras -v      # solo un bloque
```

Todo en **verde** = reto superado. Empiezan en **rojo** a propósito: ese es tu punto de partida.

---

## 🏟️ El proyecto: Analizador Deportivo

Un único proyecto que arranca modelando datos con estructuras básicas y termina
prediciendo resultados con Machine Learning. Cada fase refuerza el tema recién
aprendido.

- **Fase 0** ✅ — modelado de datos (listas y diccionarios).
- **Fase 1** ✅ — análisis con control de flujo (goles, máximo goleador, resultado).
- **Fase 2** ⏭️ — refactor en funciones (se desbloquea al ver `def`).

Detalle y fases siguientes en [`proyecto_deportes/README.md`](proyecto_deportes/README.md).

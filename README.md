# 🐍 Ruta Python — Oneyver Rodriguez

Repositorio de aprendizaje **progresivo y profesional** de Python, con la meta de
especializarme en **Ciencia de Datos**. Alineado con la *Ruta de aprendizaje de
Python en Platzi*.

Aquí conviven tres cosas que crecen juntas:

1. **Apuntes de práctica** — un archivo `.py` por concepto, autodocumentado.
2. **Retos con tests** — ejercicios que se superan poniendo los tests en verde (`pytest`).
3. **Un proyecto profesional que evoluciona** — el *Analizador Deportivo*, que va
   incorporando cada tema nuevo.

---

## 🗺️ Roadmap

| # | Módulo | Estado |
|---|--------|--------|
| 1 | Fundamentos (variables, tipos, strings, números) | 🟢 En curso |
| 2 | Control de flujo (`if`, `for`, `while`) | ⚪ Pendiente |
| 3 | Funciones y manejo de errores | ⚪ Pendiente |
| 4 | Estructuras de datos a fondo + comprehensions | ⚪ Pendiente |
| 5 | Ficheros, módulos y entornos virtuales | ⚪ Pendiente |
| 6 | Pruebas (pytest) y POO | ⚪ Pendiente |
| 7 | NumPy | ⚪ Pendiente |
| 8 | pandas | ⚪ Pendiente |
| 9 | Visualización (matplotlib / seaborn) | ⚪ Pendiente |
| 10 | Estadística y Machine Learning (scikit-learn) | ⚪ Pendiente |

> Marca con 🟢/✅ cada módulo a medida que lo completes.

---

## 📁 Estructura

```
Python/
├── python_1/            # Apuntes de fundamentos
├── retos/               # Retos con tests (pytest)
│   └── 01_fundamentos/
├── proyecto_deportes/   # El proyecto que crece por fases
├── docs/                # Web de retos (GitHub Pages)
├── requirements.txt
└── README.md
```

---

## ⚙️ Puesta en marcha

Crea un entorno virtual (hábito profesional: aísla las dependencias del proyecto):

```bash
python -m venv .venv
```

Actívalo:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## ✅ Cómo resolver un reto

1. Abre la web (`docs/index.html`) o el `README` de la carpeta del reto para leer el **enunciado**.
2. Completa la función en `retos/01_fundamentos/reto_XX_*.py` (busca el `# TODO`).
3. Ejecuta los tests:

```bash
pytest retos/01_fundamentos -v
```

Todo en **verde** = reto superado. Empiezan en **rojo** a propósito: ese es tu punto de partida.

---

## 🏟️ El proyecto: Analizador Deportivo

Un único proyecto que arranca modelando datos con estructuras básicas y termina
prediciendo resultados con Machine Learning. Cada fase refuerza el tema recién
aprendido. Ver [`proyecto_deportes/README.md`](proyecto_deportes/README.md).

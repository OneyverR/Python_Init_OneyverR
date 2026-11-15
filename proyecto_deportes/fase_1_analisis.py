"""
Proyecto Analizador Deportivo — FASE 1: Análisis con control de flujo
=====================================================================

Partimos de los mismos datos de la Fase 0, pero ahora aplicamos lo del
Bloque 3 (for, if/elif/else) para que el programa CALCULE en vez de tener
los valores escritos a mano:

  1. Imprimir la plantilla con un bucle (sin repetir el print 3 veces).
  2. Calcular los goles del equipo local sumando los de cada jugador.
  3. Encontrar al máximo goleador.
  4. Decidir el resultado del partido.

Tu tarea: completa los 4 TODO. Cuando termines:
  - al ejecutar el script verás el resumen,
  - y al correr test_fase_1_analisis.py los 3 tests quedarán en verde.

Resultados esperados (con estos datos):
    goles_local      -> 3                 (2 + 1 + 0)
    nombre_goleador  -> "Dorlan Pabón"
    resultado        -> "Victoria local"  (3 goles contra 1)
"""

# --- Datos del partido (no los modifiques) ---
local = "Atlético Nacional"
visitante = "Millonarios"

jugador_1 = {"nombre": "Dorlan Pabón", "goles": 2, "asistencias": 1, "minutos": 90}
jugador_2 = {"nombre": "Jefferson Duque", "goles": 1, "asistencias": 0, "minutos": 78}
jugador_3 = {"nombre": "Daniel Ruiz", "goles": 0, "asistencias": 2, "minutos": 90}

plantilla = [jugador_1, jugador_2, jugador_3]

# Los goles del rival nos los dan (todavía no modelamos su plantilla)
goles_visitante = 1

print("=" * 44)
print(f"  {local}  vs  {visitante}")
print("=" * 44)

# --- 1. Imprime cada jugador recorriendo la plantilla con un for ---
# TODO: recorre 'plantilla'; por cada jugador imprime una línea con su nombre,
#       goles, asistencias y minutos. Igual que en la Fase 0, pero con UN solo
#       print dentro de un bucle en vez de tres copiados.

for jugador in plantilla:
    print(f"- {jugador['nombre']}: {jugador['goles']} goles, {jugador['asistencias']} asistencias ({jugador['minutos']} min)")

# --- 2. Calcula los goles del equipo local sumando los de cada jugador ---
# TODO: recorre 'plantilla' y ve acumulando los goles en 'goles_local'.
#       Piensa con qué valor conviene empezar 'goles_local' si vas a sumar.
goles_local = 0
for jugador in plantilla:
        goles_local += jugador['goles']

# --- 3. Encuentra al máximo goleador ---
# TODO: recorre 'plantilla' y guarda en 'nombre_goleador' el nombre del jugador
#       con más goles. Pista: ve guardando el "máximo hasta ahora" y compáralo
#       con el goleador de cada vuelta.

nombre_goleador = None
maximo_goles = 0

for jugador in plantilla:
    if jugador['goles'] > maximo_goles:
        maximo_goles = jugador['goles']
        nombre_goleador = jugador['nombre']


# --- 4. Decide el resultado del partido ---
# TODO: compara goles_local con goles_visitante y guarda en 'resultado' uno de:
#       "Victoria local", "Empate" o "Victoria visitante".
resultado = None

if goles_local >  goles_visitante:
    resultado = "Victoria local" 
elif goles_visitante > goles_local:
    resultado = "Victoria visitante"
else:
    resultado = "Empate"


# --- Resumen final (funciona cuando completes lo de arriba) ---
print()
print(f"Goles del local: {goles_local}  |  Goles del visitante: {goles_visitante}")
print(f"Máximo goleador: {nombre_goleador}")
print(f"Resultado: {resultado}")

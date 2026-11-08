"""
Proyecto Analizador Deportivo — FASE 0: Modelado de datos
=========================================================

Objetivo: representar jugadores y un partido usando SOLO lo visto hasta ahora
(variables, tipos, listas, diccionarios, strings y f-strings) e imprimir un
resumen legible.

Restricción intencional: todavía NO usamos bucles ni condicionales. Eso llega
en la Fase 1, donde refactorizaremos este mismo archivo. Por eso aquí accedemos
a los datos "a mano", por índice. Es a propósito: verás por qué hacen falta los
bucles cuando intentes escalar esto a 20 jugadores.
"""

# --- Datos de un partido: cada jugador es un diccionario ---
# Clave -> valor, igual que viste en tipos_datos.py

local = "Atlético Nacional"
visitante = "Millonarios"

jugador_1 = {"nombre": "Dorlan Pabón", "goles": 2, "asistencias": 1, "minutos": 90}
jugador_2 = {"nombre": "Jefferson Duque", "goles": 1, "asistencias": 0, "minutos": 78}
jugador_3 = {"nombre": "Daniel Ruiz", "goles": 0, "asistencias": 2, "minutos": 90}

# Una lista que agrupa a los jugadores (colección ordenada y mutable)
plantilla = [jugador_1, jugador_2, jugador_3]

# Marcador final (lo calcularemos automáticamente en la Fase 1)
goles_local = 3
goles_visitante = 1

# --- Resumen (a mano, sin bucles todavía) ---
print("=" * 40)
print(f"  {local}  {goles_local} - {goles_visitante}  {visitante}")
print("=" * 40)
print(f"Jugadores en el resumen: {len(plantilla)}")
print()

print(f"- {jugador_1['nombre']}: "
      f"{jugador_1['goles']} goles, {jugador_1['asistencias']} asistencias "
      f"({jugador_1['minutos']} min)")
print(f"- {jugador_2['nombre']}: "
      f"{jugador_2['goles']} goles, {jugador_2['asistencias']} asistencias "
      f"({jugador_2['minutos']} min)")
print(f"- {jugador_3['nombre']}: "
      f"{jugador_3['goles']} goles, {jugador_3['asistencias']} asistencias "
      f"({jugador_3['minutos']} min)")

print()
print(">> Proxima fase: con un bucle 'for' recorreremos la plantilla sin")
print("   repetir codigo, y con un 'if' hallaremos al maximo goleador.")

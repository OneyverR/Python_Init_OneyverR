"""
Reto 08 — Condicionales (if / elif / else)
==========================================

En condicionales.py usaste if/elif/else para ejecutar un bloque u otro
según una condición.

Datos de partida (no los cambies):
    nota = 85     # una calificación de 0 a 100

Tu tarea: según el valor de nota, guarda en 'letra' la calificación en letras:
    90 o más      -> "A"
    de 80 a 89    -> "B"
    de 70 a 79    -> "C"
    menos de 70   -> "F"

Para nota = 85 el resultado esperado es:
    letra -> "B"
"""

# Datos de partida (no los modifiques)
nota = 85

# TODO: usa if / elif / else para asignar a 'letra' la calificación correcta.
# Piensa: ¿en qué orden conviene comprobar los rangos para no equivocarte?
letra = None

if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
else:
    letra = "F"
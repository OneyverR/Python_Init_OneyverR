"""
Reto 10 — match / case
======================

En match.py comparaste un valor contra varios patrones con match/case,
incluyendo el comodín  case _  para "cualquier otro valor".

Datos de partida (no los cambies):
    dia = 3

Tu tarea: con match/case, guarda en 'nombre_dia' el día de la semana
    1 -> "Lunes", 2 -> "Martes", 3 -> "Miércoles", 4 -> "Jueves",
    5 -> "Viernes", 6 -> "Sábado", 7 -> "Domingo"
y para cualquier número fuera de 1..7 -> "Día inválido".

Para dia = 3 el resultado esperado es:
    nombre_dia -> "Miércoles"
"""

# Datos de partida (no los modifiques)
dia = 3

# TODO: usa match/case para asignar el nombre del día a 'nombre_dia'.
# No olvides el caso comodín para los números inválidos.
nombre_dia = None

match dia:
    case 1:
        nombre_dia = "Lunes"
    case 2:
        nombre_dia = "Martes"
    case 3:
        nombre_dia = "Miércoles"
    case 4:
        nombre_dia = "Jueves"
    case 5: 
        nombre_dia = "Viernes"
    case 6:
        nombre_dia = "Sábado"
    case 7:
        nombre_dia = "Domingo"
    case _:
        nombre_dia = "Dia inválido"

print(nombre_dia)
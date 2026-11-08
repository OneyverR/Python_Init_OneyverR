"""
Reto 03 — Métodos de strings
============================

Repasa lo que viste en texto.py: .strip() quita espacios de los extremos,
.lower() pasa a minúsculas, len() cuenta caracteres y el operador `in`
dice si un texto está dentro de otro.

Datos de partida (no los cambies):
    usuario_crudo = "   Oneyver_Dev   "
    frase = "Me gusta programar en Python"

Tu tarea: crea las tres variables pedidas.

Resultados esperados:
    usuario       ->  "oneyver_dev"   (sin espacios en los extremos y en minúsculas)
    longitud      ->  28              (número de caracteres de frase)
    tiene_python  ->  True            (¿está la palabra "Python" en frase?)
"""

# Datos de partida (no los modifiques)
usuario_crudo = "   Oneyver_Dev   "
frase = "Me gusta programar en Python"

# TODO 1: limpia usuario_crudo: sin espacios en los extremos y en minúsculas
# Pista: puedes encadenar .strip() y .lower()
usuario = usuario_crudo.strip()
usuario = usuario.lower()
print(usuario)

# TODO 2: cuántos caracteres tiene frase
longitud = len(frase)

# TODO 3: ¿la palabra "Python" está dentro de frase? (debe quedar True o False)
tiene_python = "Python" in frase

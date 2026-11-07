
# Definicion de Variables en Python

x = "Esta es una Variable"  # Nombre de variable: x, operador de asignacion: = , valor de la variable: "Esta es una Variable"
print(x)  # Imprime el valor de la variable x

# Formas correctas de definir variables en Python

x = "Aca estoy escribiendo otra cosa"  # Variable de tipo string
print(x)  # Imprime el valor de la variable x permite sobreescribir el valor de la variable

X = "Esto es otra variable" # Variable de tipo entero X es difetente a x, Python es case sensitive
print(X)  # Imprime el valor de la variable X

# Nombres validos para variables en Python

nombre = "Juan"  # Variable de tipo string
mi_variable = 10  # Variable con guion bajo
_variable = 20  # Variable que comienza con guion bajo
miVariaBle = 30  # Variable con mayusculas y minusculas
VARIABLE = 40  # Variable con mayusculas
miVariable123 = 50  # Variable con numeros al final

print(nombre, mi_variable, _variable, miVariaBle, VARIABLE, miVariable123)  # Imprime el valor de todas las variables

# Nombres invalidos para variables en Python
"""
2nombre = "Pedro"  # Variable que comienza con un numero
mi-variable = 10  # Variable con guion medio
mi variable = 10  # Variable con espacio
"""

#Convenciones de nomenclatura para variables en Python

#Camel Case: Es una convención de nomenclatura en la que se escriben las palabras juntas, y cada palabra comienza con una letra mayúscula, excepto la primera palabra. Ejemplo: miVariable, nombreCompleto, edadUsuario.
ejemploCamelCase = "Esta es una variable en Camel Case"

#Pascal Case: Es una convención de nomenclatura en la que se escriben las palabras juntas, y cada palabra comienza con una letra mayúscula. Ejemplo: MiVariable, NombreCompleto, EdadUsuario.

MiVariable = "Esta es una variable en Pascal Case"

#Snake Case: Es una convención de nomenclatura en la que se escriben las palabras separadas por guiones bajos, y todas las letras son minúsculas. Ejemplo: mi_variable, nombre_completo, edad_usuario.
mi_variable = "Esta es una variable en Snake Case"

"""
Motivo para elegir una convención de nomenclatura sobre otra: 
La elección de una convención de nomenclatura sobre otra depende del estilo de programación que se esté utilizando y de las preferencias personales del programador. Sin embargo, es importante ser consistente en el uso de la convención elegida para mantener un código limpio y legible. Para variables fijas, se recomienda utilizar Snake Case, para variables privadas se recomienda utilizar guion bajo al inicio del nombre de la variable, y para variables públicas se recomienda utilizar Camel Case o Pascal Case.
"""

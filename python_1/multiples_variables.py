# Asignacion multiple de variables

a, b, c = "Manzana", "Pera", "Fresa"  # Asignacion multiple de variables a, b, c con valores "Manzana", "Pera", "Fresa"

print(b, a, c)  # Imprime Manzana Pera Fresa

# Asiganacion multiple de variables con el mismo valor

d = e = f = "Fruta"  # Asignacion multiple de variables d, e, f con el mismo valor "Fruta"
print(d, e, f)  # Imprime Fruta Fruta Fruta

# Uso de Print con + en la asignacion multiple de variables
print("La variable a contiene: " + a)
print("La variable b contiene: " + b)
print("La variable c contiene: " + c)

# Diferentes formas de concatenar variables en un print
print("La variable a contiene: ", a)  # Concatenacion con coma
print("La variable b contiene: ", b)  # Concatenacion con coma
print("La variable c contiene: ", c)  # Concatenacion con coma
print("La variable d contiene: ", d)  # Concatenacion con coma
print("La variable e contiene: ", e)  # Concatenacion con coma
print("La variable f contiene: ", f)  # Concatenacion con coma
print(a + " " + b + " " + c)  # Concatenacion con +
print(a, b, c)  # Concatenacion con coma
print(a + b + c)  # Concatenacion con +. Tener cuidado con numeros y otros tipos de datos, ya que puede generar errores si no se convierten a string.
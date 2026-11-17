
#Diccionarios: Colección de elementos desordenados, modificables y indexados. Cada elemento de un diccionario tiene una clave única que se utiliza para acceder a su valor correspondiente.

zapatilla_asics = {
    "marca": "Asics",
    "modelo": "Gel-Kayano 27",
    "color": "Negro",
    "talla": 42,
    "precio": 150.00
}

print(zapatilla_asics)

# Para acceder a la informacion de una clave especifica dentro de un diccionario
print(zapatilla_asics["marca"])

#Otro metodo para acceder a la informacion de una clave especifica dentro de un diccionario es usando el metodo .get
print(zapatilla_asics.get("color"))

#Acceder unicamente a la informacion es las claves que conforman el diccionario
print(zapatilla_asics.keys())

#Acceder unicamente a la informacion de los valores de las llaves que componen el diccionario:
print(zapatilla_asics.values())

#Encontrar una llave dentro de un diccionario: usando el operador in
if "marca" in zapatilla_asics:
    print("La marca está en el diccionario")

#Nota: Se debe considerar que el operador in es sensible a mayúsculas y minúsculas

#Cambiar el valor de una clave en el diccionario
zapatilla_asics["precio"] = 120.00
print(zapatilla_asics)

#Agregar una nueva propiedad al diccionario: 
zapatilla_asics["stock"] = 10
print(zapatilla_asics)

#Agregar varias propiedades al diccionario: usando el metodo update()
zapatilla_asics.update({"descuento": 0.10, "envio_gratis": True})
print(zapatilla_asics)

# #Eliminar una propiedad del diccionario: usando el metodo pop(). Este metodo elimina la propiedad especificada y devuelve su valor.
zapatilla_asics.pop("precio")
print(zapatilla_asics)

# #Popitem(): Este metodo elimina y devuelve el ultimo elemento agregado al diccionario. Dado que los diccionarios no estan ordenados, no se puede predecir que elemento se eliminara.

zapatilla_asics.popitem()
print(zapatilla_asics)

# #clear(): Este metodo elimina todos los elementos del diccionario, dejandolo vacio.
zapatilla_asics.clear()
print(zapatilla_asics)


print("="*80)

#Metodo for para recorrer un diccionario: Podemos recorrer los elementos de un diccionario utilizando un bucle for. Al recorrer un diccionario, se obtienen las claves de los elementos.

for k in zapatilla_asics:
    print(k) # Imprime cada clave del diccionario zapatilla_asics en una línea separada.

print("="*80)

# Obtener unicamente los valores de un diccionario utilizando el metodo values()
for v in zapatilla_asics.values():
    print(v) # Imprime cada valor del diccionario zapatilla_asics en una línea separada.

print("="*80)

# Obtener tanto las claves como los valores de un diccionario utilizando el metodo items()
for k, v in zapatilla_asics.items():
    print(k, v) # Imprime cada clave y su valor correspondiente del diccionario zapatilla_asics en una línea separada.

#Diccionarios anidados: Un diccionario puede contener otro diccionario como valor de una de sus claves. Esto se conoce como un diccionario anidado.
zapatilla_asics_detalles = {
    "marca": "Asics",
    "modelo": "Gel-Kayano 27",
    "color": "Negro",
    "talla": {
        "eu": 42,
        "us": 9,
        "uk": 8
    },
    "precio": 150.00,
    "detalles": {
        "material": "Sintético",
        "suela": "Goma",
        "tecnologia": "Gel"
    }
}
print("="*80)

#Buscar una propiedad que este incluida dentro de un diccionario anidado
print(zapatilla_asics_detalles["detalles"]["material"]) #Imprime el material de la zapatilla

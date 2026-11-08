
# Principal tipos de números en Python
x = 1
y = 2.5
z = 3j

print(type(x))  # Imprime <class 'int'>
print(type(y))  # Imprime <class 'float'>
print(type(z))  # Imprime <class 'complex'>

# Parte Positiva y Negativa de los números
a = 10
b = -10
c = 5.5
d = -5.5
e = 3j
f = -3j

#Convertir diferentes tipos de números

#Entero a flotante
entero = 10
flotante = float(entero)
print(flotante)  # Imprime 10.0

#Flotante a entero
flotante = 10.5
entero = int(flotante)
print(entero)  # Imprime 10 Que pasa con el decimal? Se elimina, no se redondea. Se trunca la parte decimal y se queda solo con la parte entera.

#Entero y flotante a complejo
entero = 10
flotante = 5.5

enteroComplejo = complex(entero)
foltanteComplejo = complex(flotante)

print(enteroComplejo)  # Imprime (10+0j)
print(type(enteroComplejo))  # Imprime <class 'complex'>

print(foltanteComplejo)  # Imprime (5.5+0j)
print(type(foltanteComplejo))  # Imprime <class 'complex'>

# Generar un número aleatorio entre 1 y 10
import random
print(random.randrange(1,10)) # Imprime un número aleatorio entre 1 y 10, sin embargo, el 10 no está incluido. El rango es [1, 10)

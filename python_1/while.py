
#Bucle While: El bucle while ejecuta un bloque de código mientras una condición sea verdadera. La sintaxis básica es la siguiente:

i = 1

while i < 10:
    print (i) #Esto imprime los números del 0 al 9, ya que la condición i < 10 es verdadera mientras i sea menor que 10. Sin embargo esto puede generar un bucle infinito si no se incrementa el valor de i dentro del bucle. Por lo tanto, es importante asegurarse de que la condición eventualmente se vuelva falsa para evitar un bucle infinito.


#Ejemplo de uso de while:
while i < 10: 
    print(i) #Esto imprime los números del 1 al 10, ya que la condición i < 10 es verdadera mientras i sea menor que 10.
    i += 1 #Esto incrementa el valor de i en 1 en cada iteración del bucle, lo que eventualmente hará que la condición i < 10 sea falsa y el bucle termine.

#Ejemplo con condicional if: Este ejemplo muestra cómo usar un bucle while junto con una declaración if para imprimir los números del 1 al 10, pero omitiendo el número 5. La variable a se inicializa en 1 y se incrementa en 1 en cada iteración del bucle. Cuando a es igual a 5, la declaración if se evalúa como verdadera y se ejecuta la instrucción break, lo que rompe el bucle y termina la ejecución del mismo. Por lo tanto, el número 5 no se imprimirá.
a = 1

while a < 10:
    if a == 6:
        break #Esto rompe el bucle cuando a es igual a 6, por lo que el bucle se detendrá y no se ejecutará ninguna iteración más.
    print(a)
    a += 1


#Ejemplo 3: Este ejemplo muestra cómo usar un bucle while para imprimir los números del 1 al 10. La variable b se inicializa en 0 y se incrementa en 1 en cada iteración del bucle. El bucle continúa ejecutándose mientras b sea menor o igual a 10. Cuando b alcanza el valor de 11, la condición del bucle se vuelve falsa y el bucle termina.
b = 0
while b <= 10:
    b += 1 
    print(b) #Esto imprime los números del 1 al 10, ya que la condición b <= 10 es verdadera mientras b sea menor o igual a 10


#Ejemplo 4: #Este ejemplo muestra cómo usar un bucle while junto con una declaración if para imprimir los números del 1 al 10, pero omitiendo el número 5. La variable c se inicializa en 0 y se incrementa en 1 en cada iteración del bucle. Cuando c es igual a 5, la declaración if se evalúa como verdadera y se ejecuta la instrucción continue, lo que hace que el bucle salte a la siguiente iteración sin ejecutar la instrucción print(c). Por lo tanto, el número 5 no se imprimirá.

c = 0

while c < 10:
    c += 1
    if c ==5:
        continue
    print(c)

# Ejemplo de While con Else:  Este ejemplo muestra cómo usar un bucle while junto con una declaración else para imprimir los números del 1 al 10, pero omitiendo el número 5. La variable d se inicializa en 0 y se incrementa en 1 en cada iteración del bucle. Cuando d es igual a 5, la declaración if se evalúa como verdadera y se ejecuta la instrucción continue, lo que hace que el bucle salte a la siguiente iteración sin ejecutar la instrucción print(d). Por lo tanto, el número 5 no se imprimirá. Cuando d alcanza el valor de 10, la condición del bucle se vuelve falsa y se ejecuta el bloque de código dentro del else, que imprime un mensaje indicando que el número es mayor a 10.
d = 0

while d < 10:
    d += 1
    if d == 5:
        continue
    print(d)
else:
    print("El numero es mayor a 10") # En este caso, el bloque de código dentro del else se ejecutará después de que la condición del while sea falsa, es decir, cuando d sea mayor o igual a 10. Esto significa que el bucle while ha terminado de ejecutarse y se ha salido del bucle.



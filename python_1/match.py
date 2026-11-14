

#Match: Es una estructura de control que permite comparar un valor con varios patrones y ejecutar un bloque de código según el patrón que coincida. Es similar a un switch en otros lenguajes de programación, pero con más flexibilidad y poder.

#Ejemplo de uso de match:
dia = 7

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _: # El guion bajo (_) es un patrón comodín que coincide con cualquier valor que no haya sido capturado por los patrones anteriores. En este caso, si el valor de dia no coincide con ninguno de los casos anteriores, se ejecutará el bloque de código correspondiente al caso _.
        print("Día inválido")


#Ejemplo 2: Deportes que se juegan con un balón
deporte = "Tennis"

match deporte:
    case "Fútbol":
        print("Se juega con un balón de Cuadros")
    case "Baloncesto":
        print("Se juega con un balón Naranja")
    case "Voleibol": 
        print("Se Juega con un Balon de Colores")
    case "Futbol Americano":
        print("Se juega con un balón de forma ovalada")
    case _: # El guion bajo (_) es un patrón comodín que coincide con cualquier valor que no haya sido capturado por los patrones anteriores. En este caso, si el valor de deporte no coincide con ninguno de los casos anteriores, se ejecutará el bloque de código correspondiente al caso _.
        print("Este deporte no se juega con Balon")
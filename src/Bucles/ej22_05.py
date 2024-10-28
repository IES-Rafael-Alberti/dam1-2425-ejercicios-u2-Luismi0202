#Ejercicio 2.2.5¶
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

def introduce_dinero():
    """
Arg:
dinero = input() -> Cantidad de dinero introducida por el usuario
Intenta pasarlo a float:
Si lo hace:
Comprueba si es negativo
Si no lo hace:
Hace una excepción

Returns:
Devuelve o falso o la variable dinero, dependiendo de si es decimal positivo o no.
"""
    dinero = input()
    try:
        dinero = float(dinero)
        if dinero <0:
            return False 
        else:
            return dinero
    except ValueError:
        return False


def introduce_años():
    """
Arg:
años = input() -> Cantidad de años introducida por el usuario
Intenta pasarlo a int:
Si lo hace:
Comprueba si es negativo
Si no lo hace:
Hace una excepción

Returns:
Devuelve o falso o la variable años, dependiendo de si es entero positivo o no.
"""
    años = input()
    try:
        años = int(años)
        if años <0:
            return False
        else:
            return años
    except ValueError:
        return False


def capital_obtenido(cant_invertir,interes_anual,num_años):
    """
Args:
for i in range (1, num_años+1) -> Para i en el rango de años de 1 hasta el año introducido +1 (porque realmente empieza por 0)....
cant_invertir *= (1+interes_anual/100) -> La cantidad a convertir que se multiplicará por esa formula y se irá acumulando por cada vuelta del bucle (por eso el *=)
print (f"En {num_años} obtendrá un capital de: {cant_invertir:.2f}€") -> En vez de retornar, se imprime el número de capital de cada año

Returns: 
Nada, se imprime en función.
"""
    for i in range (1, num_años+1):
        cant_invertir= i*(1+interes_anual/100)
        print(f"En {i} años obtendrá un capital de: {cant_invertir:.2f}€")




def main():
    """
Función principal.
Llama a introduce dinero dos veces.
Luego llama a introduce año.
En ambos casos, comprobará primero si es falso:
si lo es en alguno de los 3, dará error y tendras que volver a introducir
si no lo es, seguirá con la siguiente instrucción
Acabará con una llamada a la función capital_obtenido y esta será la que imprima por pantalla los resultados.
"""
    print("Responde a las preguntas:")
    print("CANTIDAD A INVERTIR:")
    cant_invertir = introduce_dinero()
    while cant_invertir == False:
        print("**ERROR** la cantidad a invertir tiene que ser un número positivo.\n Vuelve a introducir:")
        cant_invertir= introduce_dinero()
    
    print("INTERÉS ANUAL:")
    interes_anual = introduce_dinero()
    while interes_anual == False:
        print("**ERROR** el interés anual tiene que ser un número positivo.\n Vuelve a introducir:")
    
    print("NÚMERO DE AÑOS:")
    num_años = introduce_años()
    while num_años == False:
        print("**ERROR** El número de años tiene que ser un número entero positivo.\n Vuelve a introducir:")

    capital_obtenido(cant_invertir,interes_anual,num_años)








if __name__ == "__main__":
    main()
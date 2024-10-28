#Ejercicio 2.2.2
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


def introduce_edad():
    """
    Args:
    edad = input()-> Número introducido por el usuario.

    Returns:
    Retorna el número introducido por el usuario.
    """
    edad = input()
    return edad



def comprobar_si_num(edad):
    """
Args:
Prueba si el valor es un entero:
Si lo es:
Comprueba si es positivo o negativo
Si no lo es:
Se produce una excepción

Returns:
Devuelve Falso o el valor, dependiendo de si es entero positivo o no.
"""
    try:
        edad = int(edad)
        if edad <0 :
            return False
        else: return edad
    except ValueError:
        return False



def años_cumplidos(edad):
    """
    Función que te dirá los años cumplidos

    Args:
    contador = "" --> Variable acumulable
    for i in range (1,edad + 1): --> Para i en rango 1 hasta la  edad introducida por usuario (se añade +1 porque python empieza a contar desde 0)
    if i == edad:
    contador += f"{i}"+"." --> Si i es igual a edad, se acumulará con un punto porque indica que es el final de la cadena.
    else:
    contador += f"{i}"+"," --> De lo contario, se acumulará con una coma.

    Returns: 
    Contador
    """
    contador = ""
    for i in range (1,edad + 1):
        if i == edad:
            contador += f"{i}"+"."
        else:
            contador += f"{i}"+","
    return contador



def main():
    """
    Función principal que pide tu edad en num entero positivo.
    Si no es un entero positivo dará un fallo.
    Si lo es, convertirá tu número en un entero.
    Este número servirá para la función años cumplidos, se le hará una llamada con una variable llamada contador.
    Esta variable será finalmente impresa por pantalla con una cadena de caracteres.
    """
    print("Dime tu edad")
    valor= introduce_edad()
    while comprobar_si_num(valor) == False:
        print("**ERROR** Introduce un número entero positivo.")
        valor = introduce_edad()
    edad = int(valor)
    contador= años_cumplidos(edad)
    print(f"Estos son los años que has cumplidos a lo largo de tu vida (apartir del 1): {contador}")








if __name__ == "__main__":
    main()
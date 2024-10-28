#Ejercicio 2.2.1
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.



def introduce_palabra():
    """
    Función donde usuario introduce palabra.
    Args:
    palabra= input()-> Usuario elige palabra

    Return:
    Se retorna la palabra escrita por el usuario.
    """
    palabra = input()
    return palabra


def repetir_palabra(palabra):
    """
    Función que recibe una palabra y la retorna.
    
    Args:

    Return:
    Devuelve la palabra introducida de antes.
    """
    return palabra



def main():
    """
    Función principal.
    Pide una palabra.
    Hace un bucle de la función de repetir palabra.
    """
    print("Dime algo y haré magia...")
    palabra = introduce_palabra()
    for i in range (1,10):
        print(repetir_palabra(palabra))
    



if __name__ == "__main__":
    main()
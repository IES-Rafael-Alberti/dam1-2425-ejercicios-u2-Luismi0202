#Ejercicio 2.2.12
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

números=["1","2","3","4","5","6","7","8","9"] #Creación de tupla para que no se puedan introducir números



def escribir_frase():
    """
Función que deja al usuario escribir frase.

Arg:
Input() para que el usuario ingrese una frase

Returns:
Frase ingresada por el usuario
"""
    frase = input()
    return frase.lower()



def escribir_letra():
    """
Función para escribir una única letra.

Arg:
Deja introducir una letra con un input()
Luego mira si esa letra es realmente una unica letra
Si es verdadero, la devuelve.
Si es falso, retorna falso

Returns:
La letra o falso en correspondencia a lo que el usuario haya ingresado dentro de la función.
"""
    letra = input()
    if len(letra) > 1:
        return False
    elif letra in números:
        return False
    else:
        return letra.lower()


def contar_letra(frase:str,letra:str):
    """
Función que contará las letras en la frase.

Arg:
Si le metemos la letra a, contará cuantas letras a hay en la frase y almacenará ese valor en una variable.

Returns:
Devuelve la variable que te dice el número de letras.
"""
    frase =frase.count(letra)
    return frase




def main():
    """
Función principal.
Pide al usuario una frase y una letra.
Si la letra no es una letra entonces tendra que volverla a escribir hasta que de una unica letra.
Si es una letra, mirará cuantas letras de la que se ha introducido hay en la frase introducida y te imprimirá el resultado por pantalla.
"""
    print("Escribe una frase")
    frase = escribir_frase()
    print("Escribe una letra para contar (RECUERDA QUE NO SE PUEDEN CONTAR NÚMEROS)")
    letra = escribir_letra()
    
    while letra == False:
        print(f"**ERROR** Tienes que escribir una única letra para poder contarla en su frase. \n Introduce de nuevo:")
        letra = escribir_letra()

    print(f"Has introducido la letra ({letra}) {contar_letra(frase,letra)} veces")







if __name__ == "__main__":
    main()
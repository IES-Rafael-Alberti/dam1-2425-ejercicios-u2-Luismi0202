#Ejercicio 2.2.20
#Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

"""
Creación de tupla para declarar números.
"""
numeros = ["1","2","3","4","5","6","7","8","9"]


def introduce_frase():
    """
Función donde usuario introduce una frase.

Arg:
Input para poner frase

Returns:
La frase que hayas puesto
"""
    frase = input()
    return frase


def introduce_letra():
    """
Función de introducir letra.

Arg:
Mientras no sea letra, se hará un bucle donde tendras que introducir la letra.
Si se ve que hay mas de una letra, te dara un error porque se pide una.
Si se ve que la letra es un número, te dara error porque no admite nuemreos.
Si no se cumple ninguna, se saldrá del bucle y te devolverá la letra.

Returns:
La letra en minúscula para poder contar el valor en la frase en minúsculas.
"""
    es_letra = False
    while not es_letra:
        letra = input()
        if len(letra) >1:
            print("**ERROR** Tienes que introducir una única letra. Introduce de nuevo")
            es_letra = False
        elif letra in numeros:
            print("**ERROR**, tu letra no puede ser un número. Introduce de nuevo")
            es_letra=False
        else:
            return letra.lower()


def encontrar_letra(frase:str,letra):
    """
    Función para encontrar la letra que quieras en una frase.
    Arg:
    Se crean dos variables acumulables que irán metiendo si una posición tiene coincidencia con la letra o no.
    Para cada caracter en la frase se hará un contador que irá sumando la posición. 
    Si el caracter del bucle coincide con el de la letra que queremos buscar, se dirá en que posición esta y que hay coincidencia.
    Sino, te dirá la posición y que no la encontró.

    Returns:
    Devuelve ambas cadenas de caracteres con saltos de línea
    """
    coincidencia = ""
    nocoincidencia = ""
    posicion = 0
    frase = frase.lower()
    for caracter in frase:
        posicion= posicion + 1
        if caracter == letra:
            coincidencia += f"Se encontró una coincidencia en el caracter {caracter} EN POSICIÓN {posicion} \n"
        else:
            nocoincidencia +=f"No se encontró una coincidencia en el caracter {caracter} EN POSICIÓN {posicion} \n"
    return coincidencia + nocoincidencia


def main():
    """
Función principal.
Pide una frase, se va a la función de introducir frase.
Luego pide una letra y se va a la función de pedir letra.
Imprime por pantalla la función encontrar letra.
"""
    print("Dame una frase")
    frase = introduce_frase()
    print("Dame una letra")
    letra = introduce_letra()
    print(encontrar_letra(frase,letra))







if __name__ == "__main__":
    main()
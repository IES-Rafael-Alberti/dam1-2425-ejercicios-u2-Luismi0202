#Ejercicio 2.2.25
#Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.


"""
Función donde el usuario introduce frase.

Args:
Input donde usuario introduce frase

Returs:
Frase introducida por el usuario
"""
def introduce_frase():
    frase= input()
    return frase


"""
Función que busca la palabra más larga de la lista de palabras de la frase.

Args:
Crea una variable que contiene la palabra mas larga de la lista de palabras

Returns:
Devuelve la variable con la palabra más larga
"""
def palabra_mayor(palabras:tuple):
    palabra_larga = max(palabras)
    return palabra_larga


"""
Función principal que te pedirá que le escribas una frase y te dirá cual es la palabra más larga de esta.
Las palabras de la frase seran identificadas por un split de espacios, creandose una tupla con las palabras.
La palabra larga se buscará en la función de palabra_mayor,encargada de retornar la palabra más larga de la frase.
El número de palabras se contara con un len de la lista de palabras.
Se imprimirá por pantalla cual es la palabra más larga y cuantas palabrasa hay en la frase.
"""
def main():
    print("Escribe una frase y te diré cual es la palabra más larga de la frase.")
    frase = introduce_frase()
    palabras = frase.split(" ")
    palabra_larga= palabra_mayor(palabras)
    numpalabras = len(palabras)
    print(f"La palabra más larga de la frase es {palabra_larga} y hay {numpalabras} palabras en la frase")




if __name__ == "__main__":
    main()
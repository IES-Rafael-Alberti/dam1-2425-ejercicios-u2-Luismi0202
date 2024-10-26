#Ejercicio 2.2.11
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""
Función de introducir palabra.

Args:
Input() para que usuario introduzca palabra

Returns:
Palabra introducida por el usuario.
"""
def introduce_palabra():
    palabra = input()
    return palabra


"""
Esta función, cogerá la palabra introducida por el usuario y le dará la vuelta a cada uno de sus caracteres.

Args:
La palabra introducida por el usuario.
Se crea una variable contador para almacenar los caracteres de la palabra separados.
Se hace bucle donde "cada letra en la palabra alrevés" será metida en una variable contador separadas por un salto de línea

Returns:
Devuelve la variable contador
"""
def magia_palabra(palabra:str):
    palabra=palabra.strip()
    contador =""
    for letra in reversed(palabra):
        contador += f"{letra}\n"
    return contador



"""
Función principal.
Pedirá al usuario que introduzca una palabra.
Esta palabra introducida irá a la función de magia_palabra, donde será puesta del revés y separada por caracteres
Imprimirá uno a uno todos los caracteres empezando por la ultima letra
"""
def main():
    print("Dime una palabra y hare magia...")
    palabra = introduce_palabra()
    caracteres= magia_palabra(palabra)
    print(caracteres)


if __name__ =="__main__":
    main()
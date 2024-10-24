#Ejercicio 2.2.1
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.


"""
Args:
palabra= input()-> Usuario elige palabra

Return:
Se retorna la palabra escrita por el usuario.
"""
def introduce_palabra():
    palabra = input()
    return palabra

"""
Args:

Return:
Devuelve la palabra introducida de antes.
"""
def repetir_palabra(palabra):
    return palabra


"""
Función principal.
Pide una palabra.
Hace un bucle de la función de repetir palabra.
"""
def main():
    print("Dime algo y haré magia...")
    palabra = introduce_palabra()
    for i in range (1,10):
        print(repetir_palabra(palabra))
    



if __name__ == "__main__":
    main()
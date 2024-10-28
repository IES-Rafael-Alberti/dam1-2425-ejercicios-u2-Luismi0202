#Ejercicio 2.2.13
#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.



def introduce_palabra():
    """
Función donde usuario escribe palabra y esta es retornada.
Arg:
input() para que el usuario ponga palabra

Returns: 
La palabra introducida por el usuario
"""
    palabra = input()
    return palabra



def main():
    """
Función principal.
Te da la bienvenida a la cueva y te dice que todo lo que digas sera convertido en eco. 
Se llamará dentro de un bucle a la función introduce_palabra() para introducir una palabra.
Si escribes salir (sea mayúsculas o en minúsculas), saldras de la cueva.
De lo contrario, se imprimirá la palabra introducida un par de veces dando el efecto del eco.
"""
    print("¡Bienvenido a mi cueva! Todo lo que digas será convertido en eco. \n SI QUIERES SALIR DEL PROGRAMA TENDRÁS QUE ESCRIBIR (salir)")
    no_salir= True
    while no_salir == True: #mientras que no haya "salir"...
        palabra = introduce_palabra()
        if palabra.lower() == "salir":
            print("¡Hasta pronto! Vuelve cuando quieras")
            no_salir= False
        else: 
            print(palabra.upper())
            print(palabra.upper())
            print(palabra.lower())
            print(palabra.lower())
            print(palabra.lower())










if __name__=="__main__":
    main()
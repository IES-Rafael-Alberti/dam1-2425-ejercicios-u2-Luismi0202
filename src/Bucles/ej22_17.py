#Ejercicio 2.2.17
#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.



"""
Función que pide al usuario un número entero positivo.

Args:
Mientras que no haya fin, se te irá pidiendo un número.
En caso de ser entero positivo, te retornara el número por lo que acabará el bucle.
En caso de ser un entero negativo, dará un error de que el número no puede ser negativo.
En caso de no ser un entero, dará un error de que el número no puede ser un entero.

Returns:
False o el número
"""
def introduce_num():
    fin= False
    while not fin:
        num = input()
        try:
            num= int(num)
            if num <0:
                raise ValueError("**ERROR**SU NÚMERO NO PUEDE SER NEGATIVO")
            else:
                return num
        except ValueError as e:
            print(f"**ERROR** {e}, vuelve a introducir:")  
            fin = False


"""
Función que suma los digitos de un número.

Args:
Creamos la variable sumadigitos donde mostraremos la cadena de la suma.
Creamos la variable resultado donde mostraremos el resultado de esta suma.
Bucle que hará que cada digito del número sea sumado de manera str a sumadigitos y de manera int a resultado
Le quitaremos el simbolo de suma al final con un slice.

Returns:
Devuelve una cadena de caracteres que te dira la sumatoria de los digitos con su resultado
"""
def suma_digitos(num):
    sumadigitos= ""
    resultado= 0
    for digito in str(num):
        sumadigitos+= f"{digito}+"
        resultado= int(digito)+resultado
    sumadigitos= sumadigitos[:-1] #quitamos + final
    return f"La suma de los digitos de {num} es de {sumadigitos}={resultado}"


"""
Función principal que pide un número.
Imprime por pantalla la función de sumar digitos.
"""
def main():
    print("Dame un número entero positivo y te hare la suma de sus digitos")
    num = introduce_num()
    print(suma_digitos(num))






if __name__=="__main__":
    main()
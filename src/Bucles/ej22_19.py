#Ejercicio 2.2.19¶
#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.


def introduce_num():
    """"
Función donde usuario introduce número:

Arg:
Input donde usuario introduce número.
Si el número es entero se mirará si está en el rango de 1 o 3. 
Si no está en el rango, dará un error por no estar en el menú.
Si está, se devolverá un número.
Si es una letra o no es un número entero, dará error.

Returs:
Devolverá el número entero introducido siempre y cuando esté en el rango.
"""
    num = input()
    try:
        num = int(num)
        if num <1 and num >3:
            raise ValueError("Introduce uno de los números marcados en el menú")
        else:
            return num
    except ValueError as e:
        print(f"**ERROR** {e}")


def imprimir_texto1():
    """
Función de imprimir el texto de la opción 1.

Returns:
Devolvera que seleccionaste la opción 1
"""
    return "Seleccionaste opción1"



def imprimir_texto2():
    """
Función de imprimir el texto de la opción 2.

Returns:
Devolvera que seleccionaste la opción 2
"""
    return "Seleccionaste opción2"



def main():
    """
Mientras fin sea falso, se te dará un menu para seleccionar.
Si la selección es 1, se imprimirá la opción 1.
Si la opción es 2, se imprimirá la opción 2.
Si la opción es 3, se saldrá del bucle porque declarará que el fin es True y acabará el programa.
"""
    fin = False 
    while not fin:
        print("SELECCIONA: \n1.- Comenzar programa \n 2.- Imprimir listado \n 3.- Finalizar programa")
        seleccion = introduce_num()
        if seleccion ==1:
            print(imprimir_texto1())
        if seleccion ==2:
            print(imprimir_texto2())
        elif seleccion ==3:
            fin =True

if __name__ =="__main__":
    main()
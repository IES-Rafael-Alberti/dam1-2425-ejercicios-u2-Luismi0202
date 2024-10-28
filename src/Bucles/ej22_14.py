#Ejercicio 2.2.14
#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.



def introduce_numero():
    """
Función donde usuario ingresa número y este es retornado.

Arg:
input donde usuario ingresa número

Returns: 
Devuelve el número/valor dado
"""
    num = input()
    return num



def comprobar_num(valor:str):
    """
Función que comprueba si el valor dado es un número entero.
Si el valor dado es un número entero, no pasara nada.
De lo contrario, retornara False.

Arg:
Try y except para ver si la variable valor se puede transformar en entero

Returns:
False en caso de que no se pueda (No seria un número entero)
"""
    try:
        valor=int(valor)
    except ValueError:
        return False

def main():
    """
Función principal que pedirá números enteros para sumar hasta que le metas un 0.
Estaran creadas dos variables, una que es la serie en caracteres y otra que es un contador encargado de sumar los números que se introduzcan.
Mientras el númereo no sea un 0, se te seguirá pidiendo que metas un número. 
Si metes un 0, se saldra del programa y te imprimirá por pantalla una cadena de caracteres de la sumatoria de todos los números introducidos con su resultado.
"""
    print("Introduce números enteros para sumar. \n SE TE SEGUIRÁ PIDIENDO NUMEROS PARA AÑADIR A LA SUMA HASTA QUE PONGAS UN 0")
    es_0= False
    serie = "SUMATORIA=>"
    contador = 0
    while not es_0:
        valor = introduce_numero()
        while comprobar_num(valor) == False:
            print("**ERROR** INTRODUCE UN NÚMERO VÁLIDO")
            valor = introduce_numero()
        num = int(valor)
        if num == 0:
                serie= serie[:-1] #Quitamos el "+"
                es_0=True
        else: 
            contador += num
            serie += f"{num}+"
    print(f"{serie}={contador}")
    




if __name__ == "__main__":
    main()
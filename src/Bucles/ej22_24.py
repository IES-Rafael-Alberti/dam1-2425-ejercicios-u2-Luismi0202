#Ejercicio 2.2.24
#Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.


def introduce_num():
    """
Función para quee usuario ingrese números enteros mayores a uno.

Arg:
Si el número introducido es un entero, se mirará si es igual a 0. En caso de serlo, lo devolvera.
Sin embargo, si es menor a 1 pero no es 0, se levantará un error y se volvera a pedir número.
Si el número es un entero positivo mayor a 1, también se devolvera número.
También dará error si no introducimos un número.

Returns:
Devuelve el número siempre y cuando sea 0 o mayor a 1
"""
    fin = False
    while not fin:
        num = input()
        try:
            num = int(num)
            if num == 0:
                return num
            elif num <=1:
                raise ValueError("Introduce un número mayor a 1")
            else:
                return num
        except ValueError as e:
            print(f"**ERROR**,{e}. Introduce de nuevo:")
            fin = False


def num_primos(num):
    """
Función que mira si el número es primo.

Arg:
Se hace un bucle que mirará si el número es divisible entre más numeros que el mismo y 1.
Si solo se puede dividir entre el mismo y 1, entonces es primo, si no, entonces no es primo.

Returns:
True en caso de serlo.
False si no lo es
"""
    contador = 0
    for i in range(1,num+1):
        if num%i==0:
            contador =contador+1
    if contador ==2:
        return True
    else:
        return False



def main():
    """
Función principal que pide que escribas números enteros mayores que uno.
Se crea una variable acumulable de los primos que vayamos introduciendo.
Mientras no haya fin, te pedirá introducir un número.
Si el número introducido es 0, entonces habra fin y saldras del bucle.
Si no lo es, entonces mirará si es primo y si lo es, acumulará un +1 en la variable primos.
Si no es primo, entonces se vuelve a hacer el bucle sin añadir.

Al final, se dirá cuantos números primos hemos introducido.
"""
    print("Escribeme números mayores que 1. \n EL PROGRAMA FINALIZA CUANDO ESCRIBAS 0")
    fin = False
    primos = 0
    while not fin:
        num = introduce_num()
        if num == 0:
            fin = True
        else:
            if num_primos(num) == True:
                primos +=1
                fin = False
            else:
                fin = False

    print(F"Has introducido {primos} números primos")



if __name__ == "__main__":
    main()
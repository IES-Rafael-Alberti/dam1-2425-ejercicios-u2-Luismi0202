#Ejercicio 2.2.22
#Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.


def introducir_num():
    """
Función donde usuario introduce número.

Arg:
Mientras no haya fin, se hace un bucle donde se le pide un número al usuario.
Se comprueba si el número es entero, en caso de que no, da fallo y pide otravez el número.
Si lo es pero es negativo, da fallo y vuelve a pedir número.
Si es entero pero no es negativo, entonces se devuelve el número.

Returns:
Devuelve el número entero positivo introducido por el usuario.
"""
    fin = False
    while not fin:
        num = input()
        try:
            num = int(num)
            if num <0:
                raise ValueError("No puedes introducir números negativos.")
            else:
                return num
        except ValueError as e:
            print(f"**ERROR** {e}. Introduce de nuevo.")
            fin = False


def digitos_par(num):
    """
Función que comprueba los digitos pares de un número.

Arg:
Se crea una variable acumulable de digitos pares.
Para los digitos de num (en str porque si no no lo detecta):
cada digito (en entero para poder hacer las operaciones) entre 2 si el resto es 0 entonces es par
Se acumula un +1 en la variable par porque por cada vuelta que de, mientras vea un par, sumará +1.

Returns:
Devuelve la variable par con el número de digitos que sean pares.
"""
    par = 0
    for digitos in str(num):
        if int(digitos)%2==0:
            par = par+1
    return par


def digitos_impar(num):
    """
Función que comprueba los digitos impares de un número.

Arg:
Se crea una variable acumulable de digitos impares.
Para los digitos de num (en str porque si no no lo detecta):
cada digito (en entero para poder hacer las operaciones) entre 2 si el resto es 1 entonces es impar
Se acumula un +1 en la variable impar porque por cada vuelta que de, mientras vea un impar, sumará +1.

Returns:
Devuelve la variable impar con el número de digitos que sean pares.
"""
    impar= 0
    for digitos in str(num):
        if int(digitos)%2==1:
            impar=impar+1
    return impar


def main():
    """
Función principal.
Pedirá al usuario que ingrese números enteros positivos. Cuando meta 0, se saldrá.
Mientra fin sea falso, se hace bucle de introducir numero.
Si el número introducido es 0, fin es verdaderoo.
Si no, se comprueban los digitos pares e impares del número y se acumula esa cantidad a otras variables acumulables pares e impares.
Estas variables tendrá el total de digitos pares e impares de los números introducidos y la cantidad sera imprimida por pantalla una vez salgamos del bucle..
"""
    print("Introduzca números enteros positivos. \n ESCRIBE 0 PARA SALIR")
    fin = False
    par = 0
    impar = 0
    while fin == False:
        num = introducir_num()
        if num == 0:
            fin = True
        else:
            print(f"{num} tiene {digitos_par(num)} digitos pares y {digitos_impar(num)} digitos impares")
            par +=digitos_par(num)
            impar += digitos_impar(num)
    print(f"Se han leido en total {par} digitos pares y {impar} digitos impares")





if __name__ == "__main__":
    main()
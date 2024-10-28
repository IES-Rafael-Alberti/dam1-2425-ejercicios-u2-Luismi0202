#Ejercicio 2.2.16
#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

"""
Función para que el usuario introduzca un número entero positivo.

Args:
Mientras que no encuentre fin, se pedira un valor.
Si este valor es un entero, se mirará si es negativo.
Si no lo es, se devuelve el número.
De lo contrario, se le asignará un mensaje de error de negativo.
Si el número no es une entero, el programa le asignara el error correspondiente de ValueError

Returns:
Devuelve el número entero positivo.
"""
def introduce_num():
    fin = False 
    while fin== False:
        num = input()
        try:
            num = int(num)
            if num <0:
                raise ValueError("El número entero debe ser positivo")
            else:
                return num
        except ValueError as e:
            print(f"**ERROR** {e}, DAME NÚMERO VÁLIDO")
            fin = False


"""
Función principal.
Pide que le ingreses varios números hasta que le digas 0 (en ese caso dejará de pedir numeros)
Si el número es otro distinto a 0, mirará si es mayor a la variable contador y en ese caso, se sumará a la variable contador para poder usarse como comprobante.
Si no es mayor, no pasará nada con ese número, pero si es mayor que el número introducido anteriormente, se reseteará la variable contador y se almacenará el número.
Se imprimirá por pantalla la variable contador, donde esta introducido el número más alto.
"""
def main():
    print("Ingresame varios números ENTEROS POSITIVOS y te dire cual es el mayor. \n SI INTRODUCES 0, DEJARAS DE INTRODUCIR NÚMEROS")
    si_es0= False
    contador=0
    while si_es0== False:
        num = introduce_num()
        if num == 0:
            si_es0= True
        elif num > contador:
            contador = 0
            contador= contador + num
    print(f"El número mas alto de los ingresados es el:{contador}")
            

        


if __name__=="__main__":
    main()
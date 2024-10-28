#Ejercicio 2.2.10¶
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.


"""
Args:
num = inpuut()-> Pide al usuario que ingrese un número

Returns:
Retorna el número ingresado por el usuario.
"""
def introduce_num():
    num = input()
    return num


"""
Args:
Intenta pasar valor a entero:
Si lo consigue, devuelve el valor.
Si no lo consigue, Devuelve falso.

Returns:
Devuelve falso o el valor dependiendo de si es un número correcto o no.
"""
def comprobar_num(valor):
    try:
        valor =valor(int)
        return valor
    except ValueError:
        return False


"""
Args:
UN NÚMERO PRIMO ES AQUEL QUE ES SOLAMENTE DIVISIBLE ENTRE EL MISMO Y 1
Sabiendo esto, creamos una variable contador y un bucle for desde 1 hasta el número.
Cada vez que el número sea divisible por un número, se almacenará un +1 en el contador.
Si el contador es igual a dos, quiere decir que ese número solamente es divisible por dos valores (el mismo y 1)
De lo contrario, no será primo.

Returns:
Devuelve si el número es primo o no en función de la variable contador.
"""
def es_primo(num):
    contador = 0
    for i in range(1,num+1):
        if num%i==0:
            contador =contador+1
    if contador ==2:
        return "Su número es primo"
    else:
        return "Su número NO es primo"


"""
Función principal que pide un número.
Comprueba si este número introducido es válido, si no lo es da error.
Si el número introducido es válido, se pasara el valor a entero y se mirará si es primo.
Se imprime por pantalla el valor que retorna la función "es_primo"
"""
def main():
    print("Dame un número entero")
    valor = introduce_num()
    while valor == False:
        print("**ERROR** Valor inválido. Introduce un número entero:")
        valor= introduce_num()
    num = int(valor)
    print(es_primo(num))








if __name__ == "__main__":
    main()
#Ejercicio 2.2.3
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


def introduce_num():
    """
Args:
num = input()-> Número introducido por el usuario.

Returns:
Retorna el número introducido por el usuario.
"""
    num = input()
    return num


def comprobar_num(valor):
    """
Args:
Prueba si el valor es un entero:
Si lo es:
Comprueba si es positivo o negativo
Si no lo es:
Se produce una excepción

Returns:
Devuelve Falso o el valor, dependiendo de si es entero positivo o no.
"""
    try:
        valor = int(valor)
        if valor <0:
            return False
        else: 
            return True
    except ValueError:
        return False


def num_impares(num):
    """
Args:
for i in range(1,num + 1):--> Para i en el rango de 1 hasta num (se le pone +1 porque python empieza a contar desde 0)
if i == num: 
contador += f"{i}"+"."--> Si i es igual al número introducido, se acumulará al contador seguido de un punto en lugar de una coma, para indicar que es el último.
elif i %2 == 1:
contador += f"{i}"+"," --> Si el número es impar, se acumulará seguido de una coma.
elif i %2 == 0:
i = None --> Si es para, la variable i no valdra nada.
"""
    contador = ""
    for i in range(1,num + 1):
        if i == num:
            contador += f"{i}"+"."
        elif i %2 == 1:
            contador += f"{i}"+","
        elif i %2 == 0:
            i = None
    return contador


def main():
    """
Función principal. Pedirá num entero positivo.
Si no se le da, dara un error. 
En caso de darle un num entero positivo, seguira con las instrucciones y se pasará ese num a entero.
Se llamará a la variable num_impares creando una variable contador para que el resultaado sea el contador de esa función.
Se imprimirá esta variable contador con una cadena de caracteres.
"""
    print("Dame un número entero positivo")
    valor = introduce_num()
    while comprobar_num(valor) == False:
        print("**ERROR** Introduce un número entero positivo. \n Introduzca de nuevo:")
        valor = introduce_num()
    num = int(valor)
    contador = num_impares(num)
    print(f"Todos los impares hasta ese número (desde 1) son: {contador}")






if __name__ == "__main__":
    main()

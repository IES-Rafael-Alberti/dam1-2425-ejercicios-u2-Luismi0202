#Ejercicio 2.3.3¶
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.



def introduce_num():
    """
Función donde usuario introduce número.

Arg:
Mientras no se encuentre fin, se hace bucle donde se pide número.
Si el número es un entero, se mira si el número es negativo, si lo es dará error.
Si no, devuelve el número.
En caso de no ser un entero o no ser un número, dara un error genérico.

Returns:
Devuelve el número entero positivo introducido.
"""
    fin = False
    while not fin:
        num = input()
        try:
            num = int(num)
            if num <0:
                raise ValueError("El número no puede ser negativo.")
            else: 
                return num
        except ValueError as e:
            print(f"**ERROR** {e}. Vuelve a introducir.")
            fin = False


def cuenta_atras(num):
    """
Función que hará la cuenta atrás desde un número hasta el 0.

Arg:
Se crea variable acumulable para acumular los valores de la cuenta atrás.
Se hace bucle donde la variable i recibirá el valor desde el numero hasta el 0 en cada recorrido del bucle.
Si la i es igual a 0, se imprimirá de forma distinta al resto.
De lo contrario, se imprimira la i en str seguido de 3 puntos.

Returns:
Se devuelve la variable de la cuenta atras.
"""
    cuenta= "CUENTA ATRÁS=>"
    for i in range(num,0-1,-1):
        if i == 0:
            cuenta += f"{i}...¡DESPEGUE!"
        else:
            cuenta += f"{i}..."
    return cuenta



def main():
    """
Función principal.
Se pide un número entero positivo al usuario.
El numero será el que reetorne la función de introduce_num
Se imprime por pantalla la función de cuenta atras con su return.
"""
    print("Dame un número entero positivo")
    num = introduce_num()
    print(cuenta_atras(num))





if __name__ =="__main__":
    main()
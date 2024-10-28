#Ejercicio 2.2.4¶
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

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


def cuenta_atras(num):
    """
Args:
Contador= ""--> Variable que se irá acumulando a cada vuelta del bucle
for i in range(num,0-1,-1): --> Para i en el rango de número hasta 0-1 con un paso de -1 (porque va alrevés)
if i == 0:
contador += f"{i}"+"."---> Si i es igual a 0, acaba con punto
else:
contador += f"{i}"+","--> Si no, el contador seguirá acumulandose con los números seguidos por comas.

Returns:
Variable contador con toda la cadena str acumulada.
"""
    contador= ""
    for i in range(num,0-1,-1):
        if i == 0:
            contador += f"{i}"+"."
        else:
            contador += f"{i}"+","
    return contador


def main():
    """
Función principal que pedirá num entero positivo.
Si el usuario no le da un num entero positivo dará fallo.
Si se lo da, el valor será convertido en número entero.
Se hará una variable contador con la función de cuenta atrás.
Esa variable, sera finalmente impresa por pantalla con un print seguida de una cadena de caracteres para que quede bien.
"""
    print("Dame un número entero positivo")
    valor = introduce_num()
    while comprobar_num(valor) == False:
        print("**ERROR**, Introduce un número entero positivo. \n Pruebe de nuevo:")
        valor = introduce_num()
    num = int(valor)
    contador = cuenta_atras(num)
    print (f"Su cuenta atrás desde 0 hasta {num} es: {contador}")









if __name__ == "__main__":
    main()
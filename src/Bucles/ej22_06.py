#Ejercicio 2.2.6
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.


def introduce_num():
    """
Arg:
num = input()-> Introducción de número por usuario
Intenta pasar el número a entero: 
>si lo hace vera si es menor que 0.
>Si no lo hace, dará una excepción

Returns:
Devuelve el número o False dependiendo de si es num entero o no.
"""
    num = input()
    try:
        num = int(num)
        if num <0:
            return False
        else:
            return num
    except ValueError:
        return False


def magia_triangulo(num):
    """
Arg:
contador= "" -> Variable donde se acumularan valores
for i in range (1,num+ 1) -> Rango desde 1 hasta num introducido
contador += (i*"*")-> Variable contador se actualiza añadiendo (i * astericos). En cada vuelta i vale un valor hasta num
contador += "\n" -> Despues de hacer todo esto, hace un salto de linea para separarse del resto

Returns:
Retorna la variable contador con todas las vueltas que ha ido acumulando.
"""
    contador = ""
    for i in range (1,num + 1):
         contador += (i*"*")
         contador += "\n"
    return contador


def main():
    """
Función principal. 
Llama a introducir número.
Si el número introducido no es válido te dará error.
En caso de ser correcto, lo volvera un entero y se irá a la variable del triángulo para imprimirte por pantalla el resultado de contador.
"""
    print("Dame un número entero y lo transformaré en un triángulo con magia...")
    num =introduce_num()
    while num == False:
        print("**ERROR** Tienes que introducir un número entero positivo...")
        num = introduce_num()
    num = int(num)
    print(magia_triangulo(num))


if __name__ =="__main__":
    main()

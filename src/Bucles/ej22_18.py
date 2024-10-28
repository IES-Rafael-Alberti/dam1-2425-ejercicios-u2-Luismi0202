#Ejercicio 2.2.18
#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

"""
Función que pide al usuario introducir un número entero positivo.
Si es -1, si que devolvera "Salida" pero si no, simplemente levantara un error.

Args:
Mientras no encuentre fin, pedirá un número al usuario.
Si el número es entero, mirará si es -1, si lo es, devolvera "Salida".
Si no lo es pero es negativo, sera considerado un error.
Si solo es un número entero positivo, este número sera devuelto.
Si no es un número, será un error.

Returns:
"Salida" si es -1, num si es número entero positivo, errores si son letras o negativos distintos a -1
"""
def introduce_num():
    fin = False 
    while not fin:
        num = input()
        try:
            num = int(num)
            if num == -1:
                return "Salida"
            elif num <-1:
                raise ValueError("INTRODUCE NÚMEROS POSITIVOS A NO SER QUE QUIERAS SALIR DEL PROGRAMA CON -1")
            else:
                return num
        except ValueError as e:
            print(f"**ERROR** {e}, introduce número válido.")
            fin = False

"""
Función que suma los digitos de un número y almacena su sumatoria y los resultados para devolverlos juntos.

Args:
Variable sumatoria y resultado para retornarlos luego con los digitos sumandose y su resultado.
Bucle que hará que cada digito de num (en str porque asi detecta cada caracter) se meta en sumatoria con un + y se sume todo el rato en resultado.
Se le quita a sumatoria el "+" del final.

Returns:
Devuelve la sumatoria = resultado
"""
def suma_digitos(num):
    sumatoria=""
    resultado=0
    for digito in str(num):
        sumatoria+=f"{digito}+"
        resultado= int(digito)+resultado
    sumatoria = sumatoria[:-1]
    return f"{sumatoria} = {resultado}"


"""
Función que comprueba que el número es par.

Args:
Si el número es par...

Returns:
Booleano si es par o no.
"""
def es_num_par(num):
    if num%2==0:
        return True
    else:
        return False

"""
Función que pide al usuario ingresar númereos positivos para sumar sus digitos.
Se crea una variable llamada pares, en caso de introducir -1 al inicio, esta se entregará tal y como está al inicio.
Si el número no es igual a salida (es decir, -1), entonces imprimirá la suma de los digitos del número
luego, mirará si es par, si lo es la almacenará en la variable de pares.
Volvera a pedir un número a introducir y se repetirá el bucle hasta que se introduzca -1
Por último, cuando se salga del bucle, se imprimirá por pantalla los números introducidos que son pares.
"""
def main():
    print("Ingresa números enteros positivos y te dire la suma de sus digitos \n ESCRIBE -1 PARA SALIR")
    num = introduce_num()
    pares="NÚMEROS PARES INTRODUCIDOS=> "
    while num != "Salida":
        print(suma_digitos(num))
        if es_num_par(num) == True:
            pares+= f"{num},"
        num = introduce_num()
    pares= pares[:-1]
    print(pares)




if __name__ =="__main__":
    main()
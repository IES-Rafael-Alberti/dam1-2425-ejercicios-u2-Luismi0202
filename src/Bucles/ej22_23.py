#Ejercicio 2.2.23
#Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.

"""
Tupla para declarar digitos numéricos.
"""
numeros = ["0","1","2","3","4","5","6","7","8","9"]


"""
Función para introducir el nombre de un libro:

Args:
input donde usuario introduce libro. Cada vez que introduzca el libro, saldra delante la palabra "Libro"

Returns:
Devuelve el nombre del libro introducido
"""
def introduce_libro():
    libro = input("Libro:")
    return libro

"""
Función que sirve para contar los digitos numericos del libro introducido.

Args:
Se declara una variable acumulable.
Para cada caracter de la cadena de caracteres libros se hace un bucle hasta que termine de ir caracter a caracter.
Si el caracter esta en la tupla numeros, se suma 1 a la variable digitos.

Returs:
Al final, se devolverá la variable digitos que tendrá de resultado todos los digitos numéricos de la cadena de caracteres
"""
def contar_digitos(libro):
    digitos = 0
    for caracter in str(libro):
        if caracter in numeros:
            digitos+=1
    return digitos
        
"""
Función principal.
Mientras fin sea falso, te pedirá introducir un titulo de libro.
Si lo que introduces es una barra (/), la linea se completará y te contará el numero de digitos de esta, luego volvera a pasarse a 0 para volver a sumarse en la siguiente linea.
Si lo que introduces es una estrella (*), entonces finalizará el bucle y te dirá cuantas lineas completas se han leido.
Si introduces el titulo de un libro, mirará cuantos digitos numericos tiene el libro con la función contar digitos. Este numero se almacenara en la variable digitos.
"""
def main():
    fin = False 
    digitos = 0
    lineas = 0
    while not fin:
        libro =introduce_libro()
        if libro.strip()=="/":
            lineas +=1
            print(f"Linea completa. Aparecen {digitos} digitos numéricos")
            digitos= 0
        elif libro.strip()=="*":
            fin = True
        else:
            digitos += contar_digitos(libro)
    print(f"Se leyeron {lineas} lineas completas.")

















if __name__ == "__main__":
    main()
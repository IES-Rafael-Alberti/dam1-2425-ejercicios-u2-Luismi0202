#Ejercicio 2.3.2
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.



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



def mostrar_impares(num):
    """
Función que muestra los impares desde 1 hasta el número introducido.

Arg: 
Variable contador de impares.
Se hace bucle donde se le asigna a i un valor desde 1 hasta num en cada recorrido.
Si ve que i es impar, la mete en la variable impares.
Luego, a esta variable, se le quitará la coma del final y se le añadirá un punto.

Returns:
Devuelve la variable impares.
"""
    impares="IMPARES=>"
    for i in range(1,num+1):
        if i%2==1:
            impares +=f"{i},"
    impares= impares[:-1]
    impares+="."    
    return impares




def main():
    """
Variable que pide un número entero positivo.
El usuario introduce este número a través de la llamada a la función.
Se imprime por pantalla una cadena de caracteres junto a una llamada a la función de mostrar a impares para que muestre los números impares.
"""
    print("Dame un número entero positivo.")
    num = introduce_num()
    print(f"Los números impares desde 1 hasta {num} son: \n {mostrar_impares(num)}")









if __name__ == "__main__":
    main()
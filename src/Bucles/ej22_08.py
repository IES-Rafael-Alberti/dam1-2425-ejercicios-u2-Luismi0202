#Ejercicio 2.2.8
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.


def introduce_num():
    """
Arg:
num = input()-> Input para que el usuario meta un número
Prueba si ese número es entero

Returns: 
Devuelve el número o que es falso dependiendo de si es número o no.
"""
    num = input()
    try:
        num = int(num)
        return num
    except ValueError:
        return False


def triangulo_impar(num:int):
    """
Arg:
for i in range(1,num+1): --> Bucle que hará las vueltas hasta el valor que le hayamos introducido
if i%2==1: -->Mientras que el valor de la vueltaeste en número impar, se hará posible el print
triangulo = "" --> Reseteo de triangulo para que vaya haciendo prints por columnas
for x in range (i,0,-2): --> Se ponen los númeroos del reves
triangulo+= f" {x} "
print(triangulo) --> Imprime por pantalla el resultado del triángulo

Returns:
"""
    
    for i in range(1,num+1):
        if i%2==1:
            triangulo = ""
            for x in range (i,0,-2):
                triangulo+= f" {x} "
            print(triangulo)

def main():
    """
Función principal que pide un número entero. Si el número no es entero dará fallo.
De lo contrario, el valor introducido se pasará a número entero y luego, pedirá a la función triangulo_impar que le haga un triangulo hasta 
el valor impar del número introducido.
"""
    print("Dame un número entero")
    num = introduce_num()
    while num == False:
        print("**ERROR** DEBES INTRODUCIR UN NÚMERO VÁLIDO")
    num= int(num)
    triangulo_impar(num)

if __name__ =="__main__":
    main()
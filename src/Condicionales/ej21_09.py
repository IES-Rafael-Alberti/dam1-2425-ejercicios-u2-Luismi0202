#Ejercicio 2.1.9
#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.



def introduce_edad():
    """
Arg:
edad = input() -> Usuario escribe edad aquí

Returns:
retorna la edad que haya puesto
"""
    edad = input()
    return edad


def comprobar_edad(valor:str):
    """
Arg:
valor = valor.strip()-> Elimina los huecos
valor.startswith("-")-> Marcará si el valor empieza con guión. Como no queremos negativos retornaremos False luego.
valor.count(".")-> Se contara si hay porque no queremos ni decimales ni caracteres
valor.isdigit()-> comprobará si valor es un número

Returns:
Devolvera siempre booleanos (True o False)
"""
    valor= valor.strip()
    if valor.startswith("-"):
        return False
    elif valor.count(".") >= 1:
        return False
    if valor.isdigit() == False:
        return False
    else: #si no es número se mira si es negativo (para poder descartarlos)
        valor = int(valor)
        if valor <0:
            return False
        else:
            return True

def precio_entrada(valor):
    """
Arg:
If valor <4, ==4 and <=18, >18 -> Rango de valores que puede tomar cada if

Returns:
En cada uno retornará una cadena de caracteres diciendo cuanto tiene que pagar
"""
    if valor <4:
        return "¡Ehnorabuena chaval! Entras totalmente GRATIS"
    if valor ==4 and valor <=18:
        return "Pues ya sabes... para entrar tendrás que darme 5€"
    if valor >18:
        return "Ya puedes ir dándome 10€ si deseas entrar..."


def main():
    """
Función que pide edad, llama a la función introducir edad.
Luego, se comprueba que esa edad sea correcta, si no da error.
la edad se transforma en entera y pasa a mirarse cual es el precio
de su entrada con una llamada a la función correspondiente.
"""
    print("Si quieres pasar, primero tendrás que darme tu edad...")
    valor = introduce_edad()
    while comprobar_edad(valor) == False:
        print("*ERROR* Eso no es una edad... Dimela de nuevo:")
        valor = introduce_edad()
    edad = int(valor)
    print (precio_entrada(edad))









if __name__== "__main__":
    main()
#Ejercicio 2.2.9¶
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


def introduzca_contraseña():
    """
Arg:
contraseña = input()-> Usuario escribe contraseña

Returns:
Contraseña introducida por usuario
"""
    contraseña = input()
    return contraseña


def comprobar_contraseña(c_introducida,contraseña):
    """
Arg:
if c_introducida != contraseña--> Si la contraseña introducida no es igual a la contraseña

Returns:
Devuelve booleano (True o False)
"""
    if c_introducida != contraseña:
        return False
    else:
        return True



def main():
    """
Función principal.
Se declara la contraseña y un contador.
Se le pide al usuario contraseña, si la contraseña no es la introducida, tiene 3 intentos para introducirla o si no se acabará el programa.
De lo contrario, si la contraseña es la verdadera, te dará la bienvenida.
"""
    contador = 0
    contraseña = "contraseña"
    print("Para acceder... INTRODUZCA CONTRASEÑA")
    c_introducida= introduzca_contraseña()
    while comprobar_contraseña(c_introducida,contraseña) == False and contador <3:
        contador = contador + 1
        print(f"**ERROR** Inténtalo de nuevo, tienes {3-contador} intentos")
        c_introducida = introduzca_contraseña()
        if contador ==3 and contraseña != c_introducida:
            print("Se acabaron tus intentos... Hasta pronto")
    if comprobar_contraseña(c_introducida,contraseña) == True:
        print("Bienvenido de nuevo,usuario")



if __name__ == "__main__":
    main()
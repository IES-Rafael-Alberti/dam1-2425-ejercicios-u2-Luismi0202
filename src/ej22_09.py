#Ejercicio 2.2.9¶
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

"""
Args:
contraseña = input()-> Usuario escribe contraseña

Returns:
Contraseña introducida por usuario
"""
def introduzca_contraseña():
    contraseña = input()
    return contraseña



"""
Args:
if c_introducida != contraseña--> Si la contraseña introducida no es igual a la contraseña

Returns:
Devuelve booleano (True o False)
"""
def comprobar_contraseña(c_introducida,contraseña):
    if c_introducida != contraseña:
        return False
    else:
        return True


"""
Función principal.
Se declara la contraseña y un contador.
Se le pide al usuario contraseña, si la contraseña no es la introducida, tiene 3 intentos para introducirla o si no se acabará el programa.
De lo contrario, si la contraseña es la verdadera, te dará la bienvenida.
"""
def main():
    contador = 0
    contraseña = "contraseña"
    print("Para acceder... INTRODUZCA CONTRASEÑA")
    c_introducida= introduzca_contraseña()
    while comprobar_contraseña(c_introducida,contraseña) == False and contador <3:
        contador = contador + 1
        print(f"**ERROR** Inténtalo de nuevo, tienes {3-contador} intentos")
        c_introducida = introduzca_contraseña()
        if contador ==3:
            print("Se acabaron tus intentos... Hasta pronto")
    if comprobar_contraseña == True:
        print("Bienvenido de nuevo,usuario")



if __name__ == "__main__":
    main()
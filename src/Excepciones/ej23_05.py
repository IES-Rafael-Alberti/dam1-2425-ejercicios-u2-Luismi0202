#Ejercicio 2.3.5¶
#Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"



"""
Función donde usuario introduce contraseña.

Args:
La contraseña introducida será un input donde el usuario pondrá la contraseña.

Returns:
Devuelve esa contraseña introducida
"""
def introduce_contraseña():
    contraseña_introducida= input()
    return contraseña_introducida
    
"""
Función donde te loggeas.
La contraseña es aguacate.
El usuario tendra que introducir aguacate de contraseña o si no se levantará un NameError.
"""
def main():
    contraseña = "aguacate"
    print("Introduzca contraseña")
    contraseña_introducida = introduce_contraseña()
    if contraseña != contraseña_introducida:
        raise NameError("Incorrect Password!!")
    else:
        print("¡Bienvenido de vuelta!")

if __name__ == "__main__":
    main()
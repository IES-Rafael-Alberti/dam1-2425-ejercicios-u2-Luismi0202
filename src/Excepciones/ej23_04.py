#Ejercicio 2.3.4¶
#Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.


def introduce_num():
        """
Función donde usuario introduce nnúmero.

Arg:
Usuario introduce número.
Si el número es entero no pasara nada.
Si no lo es, dará una excepción con mensaje de erroor.

Returns:
Devuelve que el número es entero.
"""
        num = input()
        try:
            num = int(num)
            return True
        except ValueError:
            print("La entrada no es correcta")

def main():
     """
Función principal.
Pide un número entero.
Si se lo das no pasa nada.
Si le das una letra, una frase, un decimal o etc... Te dará error.
"""
     print("Introduce un número entero.")
     num = introduce_num()


if __name__ =="__main__":
     main()

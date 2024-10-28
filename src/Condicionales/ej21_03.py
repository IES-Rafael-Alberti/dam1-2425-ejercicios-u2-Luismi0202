#Ejercicio 2.1.3
#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.



def introducir_números():
    """
Función para introducir un número y devolverlo.
"""
    num = input()
    return num


def comprobar_num(valor:str):
    """
Función que comprueba si el número es realmente un número.
"""
    valor= valor.strip()
    if valor.startswith("-"):
        return valor.lstrip("-").isdigit()
    elif valor.count(".") > 1:
        return False
    else: 
        return valor.replace(".","").isdigit()


def división(num1,num2:float):
    """
Función encargada de dividir dos números 
y devolver esta división.
"""
    return num1/num2


def divisor_valido(num2):
    """
Función que mira si el divisor de la división es válido 
(en este caso, queremos que no se pueda dividir entre 0 porque no es posible)
"""
    if num2 == 0:
        return False
    else:
        return True
    

def main():
    """
Función principal. Si uno de los dos números introducidos
resulta no ser un número, te pedirá que lo vuelvas a introducir. 
Podrás ver cual de los dos es el que ha fallado y en el paréntesis, 
podrás ver el dividendo o el divisor para no perderte en la división.
"""
    print("¡Dame dos números!")
    num1= introducir_números()
    num2= introducir_números()

    no_es_num = True
    while no_es_num:
        valor1=comprobar_num(num1)
        valor2= comprobar_num(num2)

        if valor1 and valor2== True:
            no_es_num=False
        else:
            if not valor1:
                print(f"ERROR, EL NÚMERO 1 ({num1} NO ES VÁLIDO, INTRODUCE UN NÚMERO VÁLIDO PARA UN DIVIDENDO (X /{num2})")
                num1= introducir_números()    
            if not valor2:
                print(f"ERROR, EL NÚMERO 2 ({num2}) NO ES VÁLIDO, INTRODUCE UN DIVISOR VÁLIDO ({num1} / X)")
                num2= introducir_números()

    num1 = float(num1)
    num2 = float(num2)
    if divisor_valido(num2)== False:
        print("ERROR, UN NÚMERO NO ES DIVISIBLE ENTRE CERO")
    else:
        print(f"LA DIVISIÓN DE {num1} ENTRE {num2} ES IGUAL A... {división(num1,num2)}")




if __name__ == "__main__":
    main()
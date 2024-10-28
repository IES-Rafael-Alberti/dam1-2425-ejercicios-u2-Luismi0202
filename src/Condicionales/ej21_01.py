#Ejercicio 2.1.1
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.


def introducir_edad(valor):
    """
Función para ingresar un valor y que este sea retornado a variable
"num" que está asignada en el main y que llama a esta misma función.
"""
    valor = input()
    return valor


def si_negativo(num:float):
    """
Función que mira si el número es negativo
"""
    valor= 0
    while num <1:
        print("Chaval tu edad no puede ser negativa... Dimela de verdad")
        num = introducir_edad(valor)
        si_igual_num= comprobar_si_num(num)
        while not si_igual_num:
            print("No me mientas chaval, dime cuantos años tienes")
            num =introducir_edad(valor)
            si_igual_num=comprobar_si_num(num)
        num = float(num) 
    return num


def si_decimal(num:float):
    """
Función que mira si el número es decimal. TE PERMITO DEJAR DECIMALES PORQUE LUEGO REDONDEO...
"""
    if num %1 == 0:
        return False 
    else: 
        return True 


def comprobar_si_num(valor:str):
    """
Función que comprueba si el valor introducido
es realmente un número.
"""
    try:
        float(valor)
        return True
    except ValueError:
        return False


def mayor_de_edad(num):
    """
Función que comprueba si el usuario
es mayor de edad. Dependiendo de lo que sea devolverá
un valor u otro.
"""
    num = int(num)
    if num <18:
        return "lo siento eres menor adiós *se va*"
    else:
        return "¡¡PERFECTO, ERES MAYOR DE EDAD!!¡¡VAMONOS A POR CERVEZA!!"


def main():
    """
Función principal. Se le asignará variable num a la función
introducir edad y luego se hará otra variable que comprobará
si ese num es un num. A esta variable le haremos una condicional de
que si es un número, devolverá lo de la función mayor_edad, si no,
simplemente le dirá que eso no es un número. 
"""
    valor = 0
    num = 0
    print("¡Te invito a una cer-! Espera, ¿CUÁNTOS AÑOS TIENES?")
    num = introducir_edad(valor)
    si_igual_num = comprobar_si_num(num)
    while not si_igual_num:
        print("No me mientas chaval, dime cuantos años tienes")
        num =introducir_edad(valor)
        si_igual_num=comprobar_si_num(num)
    num = float(num)
    num =si_negativo(num)
    if si_decimal(num)== True:
        if num >=17.5:
            num = 17
        else:
            num = round(float(num))
        print(mayor_de_edad(num))
    else:
        print(mayor_de_edad(num))

if __name__ == "__main__":
    main()
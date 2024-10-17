#Ejercicio 2.1.1
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

"""
Función para ingresar un valor y que este sea retornado a variable
"num" que está asignada en el main y que llama a esta misma función.
"""
def introducir_edad(valor):
    valor = input()
    return valor

"""
Variable que comprueba si el valor introducido
es realmente un número.
"""
def comprobar_si_num(valor:str):
    valor.strip
    if valor.count(".")>=1:
        return False 
    elif valor.count("-")>1:
        return False
    elif valor.find("-"):
        valor = valor[0:]
        valor = valor.replace("-","")
        return valor.isdigit()

"""
Variable que comprueba si el usuario
es mayor de edad. Dependiendo de lo que sea devolverá
un valor u otro.
"""
def mayor_de_edad(num):
    num = int(num)
    if num <18:
        return"lo siento eres menor adiós *se va*"
    else:
        return "¡¡PERFECTO, ERES MAYOR DE EDAD!!¡¡VAMONOS A POR CERVEZA!!"

"""
Función principal. Se le asignará variable num a la función
introducir edad y luego se hará otra variable que comprobará
si ese num es un num. A esta variable le haremos una condicional de
que si es un número, devolverá lo de la función mayor_edad, si no,
simplemente le dirá que eso no es un número. 
"""
def main():
    valor = 0
    num = 0
    print("¡Te invito a una cer-! Espera, ¿CUÁNTOS AÑOS TIENES?")
    num = introducir_edad(valor)
    si_igual_num = comprobar_si_num(num)
    if si_igual_num == True:
        print(mayor_de_edad(num))
    else:
        while si_igual_num== False:
            print("No me mientas chaval, dame un número...")
            num = introducir_edad(valor)
            si_igual_num= comprobar_si_num(num)
            if si_igual_num == True:
                print(mayor_de_edad(num))


if __name__ == "__main__":
    main()
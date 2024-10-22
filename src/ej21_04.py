#Ejercicio 2.1.4¶
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
#  ANOTACIÓN:%=1 impar %0 = par

"""
Función para introducir un número
y que te lo retorne
"""
def introduce_num():
    num = input()
    return num

"""
Función para comprobar si ese valor es un número.
Si empieza con guión, lo quitara y mirara si el resto son
digitos, de lo contrario, comprobará la cadena entera.
"""
def comprobar_num(valor:str):
    valor = valor.strip()
    if valor.startswith("-"):
        return valor.lstrip("-").isdigit()
    else:
        return valor.isdigit()

"""
Función para retornar si el número es par o impar.
"""
def par_impar(num):
    if num %2 ==1:
        return "Su número es impar"
    elif num %2 ==0:
        return "Su número es par"

"""
Función principal. Si el número no es número, 
se te pedirá otro y se volverá a comprobar que este
sea un número.
"""
def main():
    print("Dame un número entero")
    num = introduce_num()
    es_num= comprobar_num(num)
    while es_num == False:
        print("DAME UN NÚMERO ENTERO *ERROR*")
        num = introduce_num()
        es_num = comprobar_num(num)
    num = int(num)
    print(par_impar(num))



if __name__ == "__main__":
    main()
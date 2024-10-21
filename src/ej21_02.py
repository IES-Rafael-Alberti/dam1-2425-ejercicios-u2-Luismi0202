#Ejercicio 2.3.2
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
# %=1 impar %0 = par

def introducir_número():
    num = input()
    return num

def es_num(valor:str):
    valor = valor.strip
    if valor.count("-")>1:
        return False
    elif valor.count(".")>1:
        return False
    elif valor.startswith("-"):
        return valor.isdigit()

def es_negativo_o_decimal(num):
    while num <0 or num%2==1:
        print("ERROR, INTRODUCE UN NÚMERO QUE SEA POSITIVO")
        valor= introducir_número
        num = es_num(valor)
        while num == False:
            print("DAME UN NÚMERO VÁLIDO")
            valor = introducir_número
            num= es_num(valor)
        num = float(valor)
    return num

def cadena(num):
    serie = ""
    for i in range (1,num+1):
        if i == num:
            serie=serie + str(i) + "."
        elif i %2 == 1:
            serie=serie + str(i) + ","
        elif i %2== 0:
            i = "par"
    return serie

def main():
    print("Dame un número entero positivo")
    valor=introducir_número()
    num = es_num(valor)
    while num == False:
        print("DAME UN NÚMERO VÁLIDO")
        valor = introducir_número
        num = es_num(valor)
    num = float(valor)
    es_negativo_o_decimal(num)
    num = int(num)
    print(f"AQUÍ TIENES LOS NÚMEROS IMPARES HASTA ESE NÚMERO: \n {cadena(num)}")







if __name__ == "__main__":
    main()
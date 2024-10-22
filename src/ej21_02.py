#Ejercicio 2.3.2
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
#  ANOTACIÓN:%=1 impar %0 = par
"""
Función de introducir número
"""
def introducir_número():
    num = input()
    return num

"""
Función para mirar si el valor es un número.
"""
def es_num(valor:str):
    valor= valor.strip()
    if valor.startswith("-"):
        return valor.lstrip("-").isdigit()
    elif valor.count(".") > 1:
        return False
    else: 
        return valor.replace(".","").isdigit()

"""
Función que mira si el número es negativo o decimal, en caso de serlo, te pedirá que introduzcas otro número hasta
que le des el correcto y lo devuelva.
"""
def es_negativo_o_decimal(num):
    while num < 1 or '.' in str(num):
        print("ERROR, INTRODUCE UN NÚMERO QUE SEA ENTERO POSITIVO")
        valor = introducir_número()
        while not es_num(valor):
            print("DAME UN NÚMERO VÁLIDO")
            valor = introducir_número()
        num = int(valor)
    return num

"""
Bucle for que hará que se vayan acumulando las variables "i" que vayan
pasando y todas serán impares dado a que le hemos creado unas condicionales.
"""
def cadena(num):
    serie = ""
    for i in range (1,num+1):
        if i == num:
            serie=serie + str(i) + "."
        elif i %2 == 1:
            serie=serie + str(i)+","
        elif i %2== 0:
            i = "par"
    return serie

"""
Función principal.
"""
def main():
    print("Dame un número entero positivo")
    valor=introducir_número()
    num = es_num(valor)
    while num == False:
        print("DAME UN NÚMERO VÁLIDO")
        valor = introducir_número()
        num = es_num(valor)
    num = float(valor)
    num = es_negativo_o_decimal(num)
    print(f"AQUÍ TIENES LOS NÚMEROS IMPARES HASTA ESE NÚMERO: \n {cadena(num)}")







if __name__ == "__main__":
    main()
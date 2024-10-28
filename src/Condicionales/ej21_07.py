#Ejercicio 2.1.7
#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
"""
Renta	            Tipo impositivo
Menos de 10000€	         5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	        45%
"""
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.



def introduce_num():
    """
Función que sirve para introducir num
Retorna ese num
"""
    num = input()
    return num



def comprobar_si_num(valor:str):
    """
Función que sirve para comprobar si es num.
Retorna booleano
"""
    valor= valor.strip()
    if valor.startswith("-"):
        return valor.lstrip("-").isdigit()
    elif valor.count(".") > 1:
        return False
    else: 
        return valor.replace(".","").isdigit()



def comprobar_negativo(num):
    """
Función que sirve para comprobar si es negativo.
Retorna booleano.
"""
    if num < 0:
        return True
    else: 
        return False

def renta(num):
    """
Función que sirve para comparar números.
Retorna el tipo de impositivo en función del número de la renta.
"""
    if num <10000:
        return "Su tipo de impositivo es del 5%"
    elif num >=10000 and num <20000:
        return "Su tipo de impositivo es del 15%"
    elif num >=20000 and num <35000:
        return "Su tipo de impositivo es del 20%"
    elif num >=35000 and num <=60000:
        return "Su tipo impositivo es del 30%"
    elif num >60000:
        return "Su tipo impositivo es del 45%"


def main():
    """
Función principal.
Comprueba si el num es un num, si no lo es da error,
de lo contrario, mirará si el numero es negativo,
si lo es dará error. Finalmente, imprimirá por pantalla
el tipo de renta que tengamos en función del return
de venta.
"""
    print("Dime tu renta anual")
    num = introduce_num()
    si_es_num = False
    si_negativo= True
    while not si_es_num:
        if comprobar_si_num(num)== False:
            print("**ERROR, EL NÚMERO INTRODUCIDO NO ES VÁLIDO. INTRODUCE DE NUEVO")
            num = introduce_num()
        else:
            si_es_num = True 
    while si_negativo:
        num= float(num)
        if comprobar_negativo(num)== True:
            print("**ERROR** EL NÚMERO DEBE SER POSITIVO. INTRODUCE DE NUEVO")
            num = introduce_num()
            while comprobar_si_num(num) == False:
                print("**ERROR, EL NÚMERO INTRODUCIDO NO ES VÁLIDO. INTRODUCE DE NUEVO")
                num = introduce_num()
            si_negativo = True
        else:
            si_negativo = False
    print (renta(num))



if __name__ == "__main__":
    main()
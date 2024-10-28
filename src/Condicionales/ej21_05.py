#Ejercicio 2.1.5
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def edad():
    """
Función para escribir edad y la retorna.
"""
    años = input()
    return años


def ingresos():
    """
Función para escribir y retornar el dinero
"""
    dinero = input()
    return dinero



def comprobar_si_num(valor:str):
    """
Función que comprueba si
el valor introducido es un número
"""
    valor= valor.strip()
    if valor.startswith("-"):
        return valor.lstrip("-").isdigit()
    elif valor.count(".") > 1:
        return False
    else: 
        return valor.replace(".","").isdigit()
    

def tributa(años,dinero):
    """
Función que dice si tributas o no dependiendo 
del dinero y la edad que tengas.
"""
    if años <16 and dinero <1000:
        return "LO SENTIMOS, USTED NO TRIBUTAS"
    else: 
        return "¡¡EHNORABUENA!! USTED TRIBUTA"
    


def main():
    """
Función principal que comprueba si los números de la edad
o de los ingresos son correctos y en caso de que uno de los dos falle
te los volvera a pedir. También recogera la edad y los ingresos de las 
otras funciones.
"""
    print("Dime tu edad")
    años = edad()
    print("Ahora dime tus ingresos mensuales")
    dinero = ingresos()
    
    es_num= False
    while not es_num:
        if comprobar_si_num(años) and comprobar_si_num(dinero):
            es_num= True
        elif comprobar_si_num(años) == False:
            print("¡¡ERROR!! Introduce tu edad correctamente (NÚMERO NO VÁLIDO)")
            años = edad()
            es_num = False
        elif comprobar_si_num(dinero) == False:
            print("¡¡ERROR!! Introduce tus ingresos correctamente (NÚMERO NO VÁLIDO)")
            dinero = ingresos()
            es_num = False

    años = float(años)
    dinero = float(dinero)
    print(tributa(round(años,2),dinero))


if __name__ == "__main__":
    main()
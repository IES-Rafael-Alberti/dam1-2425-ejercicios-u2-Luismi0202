#Ejercicio 2.1.5
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""
Función para escribir edad y la retorna.
"""
def edad():
    años = input()
    return años

"""
Función para escribir y retornar el dinero
"""
def ingresos():
    dinero = input()
    return dinero


"""
Función que comprueba si
el valor introducido es un número
"""
def comprobar_si_num(valor:str):
    valor= valor.strip()
    if valor.startswith("-"):
        return valor.lstrip("-").isdigit()
    elif valor.count(".") > 1:
        return False
    else: 
        return valor.replace(".","").isdigit()
    
"""
Función que dice si tributas o no dependiendo 
del dinero y la edad que tengas.
"""
def tributa(años,dinero):
    if años <=16 or dinero <1000:
        return "LO SENTIMOS, USTED NO TRIBUTAS"
    else: 
        return "¡¡EHNORABUENA!! USTED TRIBUTA"
    

"""
Función principal que comprueba si los números de la edad
o de los ingresos son correctos y en caso de que uno de los dos falle
te los volvera a pedir. También recogera la edad y los ingresos de las 
otras funciones.
"""
def main():
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
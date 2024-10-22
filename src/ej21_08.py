#Ejercicio 2.1.8
#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
"""
Nivel	        Puntuación
Inaceptable	    0.0
Aceptable	    0.4
Meritorio   	0.6 o más
"""
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.


def introduce_puntuación():
    puntuacion= input()
    return puntuacion

def comprobar_si_num(valor:str):
    valor= valor.strip()
    if valor.startswith("-"):
        return valor.lstrip("-").isdigit()
    elif valor.count(".") > 1:
        return False
    else: 
        return valor.replace(".","").isdigit()

def nivel(num):
    if num == 0.0 or num <0.4:
          return 0.0
    elif num ==0.4 or num <0.6:
        return 0.4
    elif num ==0.6 or num >0.6:
        return num

def dinero(num):
    cantidad_dinero = 2400 * num
    return f"USTED CONSIGUE {cantidad_dinero}€ CADA MES"

def comprobar_si_decimal_o_negativo(num:str):
    if num <0.0:
        return True
    else:
        num = str(num)
        return num.isdecimal()

def main():
    print("Dame tu puntuación")
    valor = introduce_puntuación()
    si_es_num= False 
    si_es_decimal = False
    
    while si_es_num == False:
        if comprobar_si_num(valor) == True:
            si_es_num = True
        elif comprobar_si_num(valor) == False:
            print("**ERROR** TIENES QUE INTRODUCIR UN NÚMERO")
            valor = introduce_puntuación()
            si_es_num= False
    num = float(valor)
   
    while si_es_decimal == False:
        if comprobar_si_decimal_o_negativo(num) == True:
            print("**ERROR**, EL NÚMERO DEBE SER UN DECIMAL A PARTIR DE 0")
            valor = introduce_puntuación()
            while comprobar_si_num(valor)== False:
                print("**ERROR**, TIENES QUE INTRODUCIR UN NÚMERO")
                valor = introduce_puntuación()
            num = float(valor)
            si_es_decimal= False
        else:
            si_es_decimal= True

    valor = float(valor)
    punt_nivel= nivel(num)
    print(dinero(punt_nivel))

    


if __name__ =="__main__":
    main()
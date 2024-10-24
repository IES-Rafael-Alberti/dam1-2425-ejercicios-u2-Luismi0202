#Ejercicio 2.1.8
#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
"""
Nivel	        Puntuación
Inaceptable	    0.0
Aceptable	    0.4
Meritorio   	0.6 o más
"""
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

"""
Args:
puntuación: input() donde el usuario escribirá la puntuación

Returns:
Retorna la puntuación escrita por el usuario
"""
def introduce_puntuación():
    puntuacion= input()
    return puntuacion

"""
Args:
valor= valor.strip() -> Quitará los espacios vación de izquierda a derecha para poder contar correctamente.
if valor.startswith("-") -> Si el valor empieza con guión.

Returns:
valor.lstrip("-").isdigit() -> Quitará el guión y dirá si el resto son números (booleano).
False -> Retorna booleano (si tiene mas de un punto es falso)
valor.replace(".","").isdigit() -> Reemplaza el punto si hay solo 1 por un vacío y mira si el resto son números (booleano).
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
Args:
if num == 0.0 or num <0.4 -> Si el valor es igual a cero o  menor a 0.4...
if num ==0.4 or num <0.6 -> Si el valor es igual a 0.4 o menor a 0.6...
if num==0.6 or num >0.6 -> Si el valor es igual o mayor a 0.6...
if num <0.0 -> Si el valor es menor que 0.0....

Returns:
Puede devolver 0.0, 0.4 o el número en caso de que sea mayor o igual a seis.
En caso de ser negativo, devuelve "Error".
"""
def nivel(num):
    if num == 0.0 or num <0.4:
          return 0.0
    elif num ==0.4 or num <0.6:
        return 0.4
    elif num >=0.6:
        return num
    elif num <0.0:
        return "Error" #Devuelve caracteres para usarlo luego en while

"""
Args:
cantidad_dinero = 2400 * num -> variable que hará la multiplicación de 2400 por el número para dar el reusltado

Returns: 
Cadena de caracteres junto a variable cantidad_dinero para luego imprimir esta función
"""
def dinero(num):
    cantidad_dinero = 2400 * num
    return f"USTED CONSIGUE {cantidad_dinero}€ CADA MES"

"""
Función principal.
Te pide puntuación, llama a introduce puntuación,
verifica si los números son negativos o si son decimales,
en caso de que se produzca algún error, se pide de nuevo el número.
Al final, el valor se vuelve un float y este se manda a la función nivel
para ver en que nivel está y se imprimirá esta función.
"""
def main():
    print("Dame tu puntuación")
    valor = introduce_puntuación()
    si_es_num= False #Bandera 1.
    si_es_nivel = False #Bandera 2.
    
    while si_es_num == False: 
        if comprobar_si_num(valor) == True:
            si_es_num = True #Como es número se sale del bucle
        elif comprobar_si_num(valor) == False:
            print("**ERROR** TIENES QUE INTRODUCIR UN NÚMERO")
            valor = introduce_puntuación()
            si_es_num= False
    num = float(valor)
    
    while not si_es_nivel:
        if nivel(num) == "Error":
            print("El número introducido es menor que 0, vuelve a introducir")
            valor = introduce_puntuación()
            while comprobar_si_num(valor) == False:
                print("**ERROR** TIENES QUE INTRODUCIR UN NÚMERO")
                valor = introduce_puntuación()
            num = float(valor)
            si_es_nivel = False
        else:
            si_es_nivel= True #Como es un nivel, se sale del bucle

    punt_nivel = nivel(num)
    print(dinero(punt_nivel))

    


if __name__ =="__main__":
    main()
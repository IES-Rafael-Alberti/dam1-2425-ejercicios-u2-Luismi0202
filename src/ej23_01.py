#Ejercicio 2.3.1¶
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
#EXTRA: CALCULAR EXCEPCIONES SI LA EDAD NO ES POSITIVA, ES IGUAL A 0 O ES MAYOR QUE 125.


"""
Función que pide edad.
"""
def pedir_edad():
    fin = False
    while fin == False:
        try:
            edad = int(input())
            if edad < 0:
                raise ValueError("La edad debe ser un número positivo.")
            elif edad == 0:
                raise ValueError("La edad debe ser un número que no sea 0.")
            elif edad >125:
                raise ValueError("La edad debe ser un número igual o inferior a 125")
            else:
                return edad
        except ValueError as e:
            print(f"ERROR, {e} DAME UN NÚMERO VÁLIDO")            
            fin = False

"""
Función que mostrará los años cumplidos.
"""
def mostrar_años_cumplidos(edad:int):
    serie = ""
    for i in range (1,edad+1):
        if i == edad:
            serie += str(i) + "."
        else:
            serie += str(i) + ","
    return serie


"""
Función principal
"""
def main():
    print("Dame tu edad")
    edad = pedir_edad()
    contador= mostrar_años_cumplidos(edad)
    print(f"Aquí tienes todos los años que has cumplido: {contador}")




if __name__== "__main__":
    main()
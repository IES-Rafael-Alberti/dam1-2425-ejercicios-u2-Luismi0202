#Ejercicio 2.1.1
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def introducir_edad(valor):
    valor = input()
    return valor

def comprobar_si_num(valor:str):
    valor.strip
    if valor.count(".")>=1:
        return False 
    elif valor.count("-")>=1:
        return False
    elif valor.find("-"):
        valor = valor[0:]
        return valor.isdigit()

def mayor_de_edad(num):
    if num <18:
        return"lo siento eres menor adiós *se va*"
    elif num >=18:
        return "¡¡PERFECTO, ERES MAYOR DE EDAD!!¡¡VAMONOS A POR CERVEZA!!"

def main():
    valor = 0
    num = 0
    print("¡Te invito a una cer-! Espera, ¿CUÁNTOS AÑOS TIENES?")
    num = introducir_edad(valor)
    num = comprobar_si_num(num)
    if num == True:
        print(mayor_de_edad(num))
        
if __name__ == "__main__":
    main()
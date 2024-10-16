#Ejercicio 2.1.1
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
mensaje_de_error= "ERROR, INTRODUCE TU EDAD DE VERDAD"

def introducir_edad(valor):
    valor= input()
    return valor
def valor_es_num(valor:str):
    valor= valor.strip
    contarpuntos= valor.count(".")
    contarguion = valor.count("-")
    if contarpuntos >= 1:
        return False 
    elif contarguion >1:
        return False
    elif valor.startswith("-"):
        valor = valor.replace("-","")
    return valor.isdigit

def mayor_edad(num):
    if num >=18:
        return "¡¡EHNORABUENA, ERES MAYOR DE EDAD!! ESTÁS INVITADO A UNA CERVECITA!!"
    elif num <18:
        return "Lo siento, no estás listo para la vida de adulto... eres menor...."
    
def msj_error(mensaje_de_error):
    return mensaje_de_error
def main():
    valor= str
    print("Introduce tu edad:")
    num= introducir_edad(valor)
    valor_es_num(valor)
    while valor_es_num(valor)!=True:
        msj_error()
        valor=input()
    print(mayor_edad(num))

if __name__ == "__main__":
    main()
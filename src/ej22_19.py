#Ejercicio 2.2.19¶
#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.


def introduce_num():
    num = input()
    try:
        num = int(num)
        if num <1 and num >3:
            raise ValueError("Introduce uno de los números marcados en el menú")
        else:
            return num
    except ValueError as e:
        print(f"**ERROR** {e}")


def imprimir_texto():
    return "Holaaaaa"

def main():
    fin = False 
    while not fin:
        print("SELECCIONA: \n1.- Comenzar programa \n 2.- Imprimir listado \n 3.- Finalizar programa")
        seleccion = introduce_num()
        if seleccion ==1 or seleccion == 2:
            print(imprimir_texto())
        elif seleccion ==3:
            fin =True

if __name__ =="__main__":
    main()
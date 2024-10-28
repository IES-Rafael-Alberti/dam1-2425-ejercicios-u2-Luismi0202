#P2.4 - Ejercicio.
#El algoritmo burbuja

def burbuja(a:list)-> list:
    """
    Función que hará el orden burbuja.

    Arg:
    Contamos el número de números que hay en total en la lista.
    Hacemos dos bucles for, un rango de 0 hasta n-1 y otro de i+1 a n.
    Esto se hará para comparar un número de la listas con el siguiente.
    Si el primer número es mayor que el siguiente, se intercambiará con el siguiente porque es menor.
    
    Returns:
    Retorna la lista actualizada
    """
    n=len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a[i]>a[j]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
                
                  
    return a


def main():
    """
    Función principal.
    Le hacemos una lista y llamamos a la función burbuja con ella.
    """
    a = [8,3,1,19,14]
    print(burbuja(a))

if __name__ == "__main__":
    main()
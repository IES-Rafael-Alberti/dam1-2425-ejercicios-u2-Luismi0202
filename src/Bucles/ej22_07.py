#Ejercicio 2.2.7¶
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.



def tabla(num:int):
    """
Arg:
tabla=f"Tabla del {num}\n"-> Variable acumulable. Si es la tabla del 1 dirá que es la tabla del 1 seguido de la tabla.
for i in range(1,10+1): ->  Para i en el rango del 1 al 10 (se añade mas 1 porque empieza a contar a partir de 0)
tabla += f"{num}*{i}={num*i}\n" -> Se acumula en la variable la tabla

Returns:
Retorna la tabla del número que sea
"""
    tabla=f"Tabla del {num}\n"
    for i in range(1,10+1):
        tabla += f"{num}*{i}={num*i}\n"
    return tabla

def main():
    """
Función principal.
Declarará un número apartir de un bucle for del 1 al 10.
Así, en cada salto que haga, se irá a la función de tabla, se hará la tabla de ese número,
y luego la función main le dará otro dentro del rango 1-10
"""
    for i in range(1,10+1):
        print(tabla(i)+"\n")


if __name__ =="__main__":
    main()
#Ejercicio 2.2.21¶
#Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.


"""
Función donde el usuario ingresa los montos.

Args:
Mientras el número no sea válido, se hará un bucle pidiendo el número.
Si el numero es decimal pero es negativo, dará error.
Si no es negativo, no dara error.

Returns:
devuelve el número en caso de no ser negativo y de que sea un número
"""
def introduce_montos():
    valido = False
    while not valido:
        montos =input()
        try: 
            montos= float(montos)
            if montos <0:
                raise ValueError("El número no puede ser negativo.")
            else:
                return montos
        except ValueError as e:
            print(f"**ERROR** {e}. Introduce de nuevo")

"""
Función para calcular el total de ventas totales.

Args:
Si el número es mayor a 1000, se le aplicará un descuento del 10% a las ventas.
Si no, se devolvera el número tal y como estaba.

Returns:
Devuelve el número con descuentos o no en función de si el número es mayor a 1000
"""
def total_ventas(ventas):
    if ventas >1000:
        ventas_descuento = ventas*0.10
        ventas = ventas - ventas_descuento
        return f"INFORME TOTAL (DESCUENTO APLICADO): VENTAS DE {ventas}€"
    else:
        return f"INFORME TOTAL: VENTAS DE {ventas}€"

"""
Función principal.
Mientras que no haya fin, se hará un bucle donde se te pidan montos de las ventas.
Si el montos es 0, entonces hay fin. 
De lo contrario, el monto se irá acumulando en la variable de datos_montos.
Con esta variable, miraremos el total de ventas con la función de total ventas.
"""
def main():
    fin = False
    datos_montos = 0
    print("INTRODUCE MONTOS DE LAS COMPRAS:\n (pon 0 para salir)")
    while not fin:
        montos =introduce_montos()
        if montos == 0:
            fin = True
        else:
            datos_montos+= montos
            fin = False
    print(total_ventas(datos_montos))
if __name__ == "__main__":
    main()
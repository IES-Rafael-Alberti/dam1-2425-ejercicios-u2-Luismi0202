#Ejercicio 2.1.10
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
"""Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón."""
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


def introduce_valor():
    """
Arg:
tipo = input() -> Poner el tipo de pizza o ingrediente

Returns: 
tipo = el tipo de pizza o ingrediente introducido
"""
    tipo = input()
    return tipo 



def ingredientes(tipo:str):
    """
Arg:
if tipo.lower() == vegetariana -> Si es vegetariana...
if tipo.lower() == no vegetariana -> Si no es vegetariana...

Returns:
pimiento y tofu si es vegetariana, 
peperoni,jamon y salmon si es no vegetariana
Error -> Si no es ninguna de las dos devolvera un valor llamado error
"""
    if tipo.lower() == "vegetariana":
        return "Pimiento, tofu"
    elif tipo.lower() == "no vegetariana":
        return "Peperoni, Jamón y Salmón"
    else:
        tipo = "Error"
        return tipo


def selección_ingredientes(tipo:str,ingrediente:str):
    """
Arg:
if tipo.lower()== vegetariana -> Si es vegetariana...
    if ingrediente.lower() == "pimiento" or "tofu" -> si es uno de estos ingredientes...
if tipo.lower()== no vegetariana -> Si es no vegetariana...
    if ingrediente.lower() == "peperoni" or "jamón" or "salmón"-> si es uno de estos ingredientes...

Returns:
Puede retornar o ingrediente o falso dependiendo de si el valor es uno de los que se te piden o no
"""
    if tipo.lower() == "vegetariana":
        if ingrediente.lower()== "pimiento" or ingrediente.lower()=="tofu":
            return ingrediente
        else:
            return "Error"
    elif tipo.lower() == "no vegetariana":
        if ingrediente.lower() == "peperoni" or ingrediente.lower() == "jamón" or ingrediente.lower()== "salmón":
            return ingrediente
        else:
            return "Error"



def main():
    """
Función principal. Pide que pizza quieres, la introduces a través de una función.
Si le has introducido una de las dos que te dicen seguirá comprobando otras cosas, sino,
te dara un error. Luego te pedirá ingrediente y pasará lo mismo, si le das uno de los que te da,
no pasará nada, de lo contrario, dará error.
La función acabara con un print a el tipo de pizza, al ingrediente elegido y una cadena de caracteres.
"""
    print("ESCRIBA: ¿Que pizza quieres? \n A)Vegetariana (Escriba vegetariana) \n B)No vegetariana (Escriba no vegetariana)")
    tipo = introduce_valor()
    while ingredientes(tipo) == "Error":
        print("**ERROR** ¡¡¡¡Tienes que introducir (Vegana) o (No vegana) en función del menú que quieras!!!!")
        tipo = introduce_valor()
    print(f"Elija un ingrediente entre estos: {ingredientes(tipo)}")
    ingrediente= introduce_valor()
    while selección_ingredientes(tipo,ingrediente)== "Error":
        print(f"**ERROR** Introduce un tipo de ingrediente válido para tu pizza {tipo}")
        ingrediente = introduce_valor()
    print(f"Entonces quieres una pizza {tipo} con los siguientes ingredientes: Mozarella, tomate,{selección_ingredientes(tipo,ingrediente)}... ¡Oido cocina!")




if __name__ == "__main__":
    main()
#Ejercicio 2.1.10
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
"""Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón."""
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.



def introduce_pizza():
    tipo = input()
    return tipo 

def ingredientes(tipo:str):
    if tipo.lower() == "vegetariana":
        return "Pimiento, tofu"
    elif tipo.lower() == "no vegetariana":
        return "Peperoni, Jamón y Salmón"
    else:
        tipo = "Error"

def menu():
    





def main():
    print("ESCRIBA: ¿Que pizza quieres? \n A)Vegetariana (Escriba vegetariana) \n B)No vegetariana (Escriba no vegetariana)")
    tipo = introduce_pizza()
    while ingredientes(tipo) == "Error":
        print("**ERROR** ¡¡¡¡Tienes que introducir (Vegana) o (No vegana) en función del menú que quieras!!!!")
        tipo = introduce_pizza()
    print(f"Elija ingredientes {ingredientes(tipo)}")







if __name__ == "__main__":
    main()
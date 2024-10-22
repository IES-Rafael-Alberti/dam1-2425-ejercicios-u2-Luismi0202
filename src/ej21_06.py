#Ejercicio 2.1.6¶
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""
Tupla para indicar los dos sexos que se pueden poner.
"""
SEXOS = ["hombre","mujer"]


"""
Función de introducir nombre.
Retorna nombre.
"""
def introduce_nombre():
    nom = input()
    return nom

"""
Función de introducir sexo.
Retorna sexo.
"""
def introduce_sexo():
    sexo= input()
    return sexo
"""
Función que comprueba si el valor introducido
es un número.
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
Función que mirará la inicial de tu nombre y la comparará
más tarde en mayúsculas con la letra correspondiente que pida el
enunciado. Según si empieza con esa inicial o no,
o si es hombre o mujer, pertenecerá a un grupo u otro.
"""
def grupo(sexo:str,nombre:str):
    nombre_inicial = nombre[0:]
    if sexo.lower()== "hombre":
        if nombre_inicial.upper() < "N":
            return "Usted está en el grupo A"
        else:
            return "Usted está en el grupo B"
    elif sexo.lower() == "mujer":
        if nombre_inicial.upper() > "M":
            return "Usted está en el grupo A"
        else:
            return "Usted está en el grupo B"

"""
Función principal. Si uno de los dos es un número,
te dará un error. Si el sexo no es hombre o mujer, 
te dará un error. De cumplirse todo correctamente,
te dirá el grupo al que perteneces.
""" 
def main():
    print("Dame tu nombre")
    nombre = introduce_nombre()
    print("Dime tu sexo")
    sexo = introduce_sexo()
    es_num= True 
    es_sexo = False
    while es_num:
        if not comprobar_si_num(nombre) and not comprobar_si_num(sexo):
            es_num = False
        elif comprobar_si_num(nombre) == True:
            print("**ERROR** Los números no son válidos \n INTRODUCE DE NUEVO SU NOMBRE:")
            nombre = introduce_nombre()
        elif comprobar_si_num(sexo) == True: 
            print("**ERROR** Los números no son válidos. \n INTRODUCE DE NUEVO SU SEXO:")
            sexo = introduce_sexo()
    while not es_sexo:
        if sexo.lower() not in SEXOS:
            print("**ERROR** INTRODUCE SU SEXO (HOMBRE O MUJER)")
            sexo = introduce_sexo()
            es_sexo = False
        else:
            es_sexo = True
    print(grupo(sexo,nombre))






if __name__ == "__main__":
    main()
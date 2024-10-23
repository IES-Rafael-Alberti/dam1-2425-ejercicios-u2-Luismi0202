

def introduce_num():
    num = input()
    try:
        num = int(num)
        return num
    except ValueError:
        return False

def triangulo_impar(num:int):
    triangulo = ""
    for i in range(1,num+1):
        if i%2==1:
            triangulo+= f" {i} "
            print(triangulo)

def main():
    print("Dame un número entero")
    num = introduce_num()
    while num == False:
        print("**ERROR** DEBES INTRODUCIR UN NÚMERO VÁLIDO")
    num= int(num)
    triangulo_impar(num)

if __name__ =="__main__":
    main()
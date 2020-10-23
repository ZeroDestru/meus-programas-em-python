'''
binário, octal, decimal e hexadecimal.
Para transformar da base decimal para qualquer outra, será chamada apenas uma função.
Para transformar de qualquer base para base decimal, será chamada apenas uma função.
Para transformar de qualquer base para qualquer outra sem ser decimal, será necessário, primeiro
transformar da base informada para decimal e o resultado transformar para a base desejada, ou seja,
chamará as duas funções.
'''
def binário(num):
    posn = 0

    while(num > 1):
        num2 = int(num%2)
        num = num/2
        posn*=10
        posn += num2

    return posn

def octal(num):
    posn = 0
    
    while(num > 1):
        num2 = int(num%8)
        num = num/8
        posn *= 10
        posn += num2
    
    return posn

def hexadecimal(num):
    posn = 0
    
    while(num > 1):
        num2 = int(num%16)
        num = num/16
        posn *= 10
        posn += num2
    
    return posn

def bitodec(num):
    posn = 0
    num2 = []
    
    while(num > 1):
        num2.append(num%10)
        num = int(num/10)
    
    for i in range(len(num2)):
        posn += num2[i]**(i+1)

    return posn

def octtodec(num):
    posn = 0
    num2 = []
    
    while(num > 1):
        num2.append(num%10)
        num = int(num/10)
    
    for i in range(len(num2)):
        posn += num2[i]**(i+1)

    return posn

def hextodec(num):
    posn = 0
    num2 = []
    
    while(num > 1):
        num2.append(num%10)
        num = int(num/10)
    
    for i in range(len(num2)):
        posn += num2[i]**(i+1)

    return posn

while(True):
    print("\nbem vindo vindo a o conversor de bases")
    print("se deseja converter decimal em binário digite 1")
    print("se deseja converter decimal em octal digite 2")
    print("se deseja converter decimal para hexadecimal digite 3")
    print("se deseja converter binário em decimal digite 4")
    print("se deseja converter octal em decimal digite 5")
    print("se deseja converter hexadecimal para decimal digite 6")
    print("se deseja converter binário em octal digite 7")
    print("se deseja converter binário em hexadecimal digite 8")
    print("se deseja converter octal em binario digite 9")
    print("se deseja converter octal em hexadecimal digite 10")
    print("se deseja converter hexadecimal para binario digite 11")
    print("se deseja converter hexadecimal para octal digite 12")
    print("se deseja sair digite 13")

    respm = int(input("digite a opção que deseja: "))

    if(respm == 1):
        num3 = int(input("digite o numero: "))

        print("conversão dá ", binário(num3))

    elif(respm == 2):
        num3 = int(input("digite o numero: "))

        print("conversão dá ", octal(num3))

    elif(respm == 3):
        num3 = int(input("digite o numero: "))

        print("conversão dá ", hexadecimal(num3))

    if(respm == 4):
        num3 = int(input("digite o numero: "))

        print("conversão dá ", bitodec(num3))

    elif(respm == 5):
        num3 = int(input("digite o numero: "))

        print("conversão dá ", octtodec(num3))

    elif(respm == 6):
        num3 = int(input("digite o numero: "))

        print("conversão dá ", hextodec(num3))

    if(respm == 7):
        num3 = int(input("digite o numero: "))
        num4 = bitodec(num3)

        print("conversão dá ", octal(num4))

    elif(respm == 8):
        num3 = int(input("digite o numero: "))

        print("conversão dá ", octal(num3))

    elif(respm == 9):
        num3 = int(input("digite o numero: "))
        num4 = bitodec(num3)
        
        print("conversão dá ", hexadecimal(num3))

    if(respm == 10):
        num3 = int(input("digite o numero: "))

        print("conversão dá ", bitodec(num3))

    elif(respm == 11):
        num3 = int(input("digite o numero: "))

        print("conversão dá ", octtodec(num3))

    elif(respm == 12):
        num3 = int(input("digite o numero: "))

        print("conversão dá ", hextodec(num3))
    


    elif(respm == 13):
        break

    else:
        print("não há essa opção, tente novamente")
        input()

from msvcrt import getch
segun = 0
ho = 0
min = 0
se = 0
respm = 0

def segtkrun():
    
    global segun
    se = int(segun%100)
    segun/=100
    min = int(segun%100)
    segun/=100
    ho = int(segun)

    hora = [ho,':',min,':',se]
    return hora
    

def compltkrun():

    global ho, min, se
    hora = ho
    hora = (hora*100)+min
    hora = (hora*100)+se

    return hora


def kruntnos():

    global ho, min, se, segun
    sen=0 
    minn=0 
    hon=0

    hora = ho
    hora = (hora*100)+min
    hora = (hora*100)+se
    
    sen = int(hora%60)
    hora/=60
    minn = int(hora%60)
    hora/=60
    hon = int(hora)

    nos = [hon,':',minn,':',sen]

    return nos

while(True):
    print("\nbem vindo vindo a o conversor de tempo")
    print("se deseja converter segundos em tempo Krunensberg digite 1")
    print("se deseja converter tempo de Krunensberg em segundos digite 2")
    print("se deseja converter Krunensberg para o nosso tempo digite 3")
    print("se deseja sair digite 4")

    respm = int(input("digite a opção que deseja: "))

    if(respm == 1):
        segun = int(input("digite os segundos: "))

        re = segtkrun()
        for i in range(len(re)):
            print(re[i],end='')
        getch() 

    elif(respm == 2):
        ho = int(input("digite as horas: "))
        min = int(input("digite os minutos: "))
        se = int(input("digite os segundos: "))

        re = compltkrun()
        print(re, "segundos")
        getch() 

    elif(respm == 3):
        ho = int(input("digite as horas: "))
        min = int(input("digite os minutos: "))
        se = int(input("digite os segundos: "))

        re = kruntnos()
        for i in range(len(re)):
            print(re[i],end='')
        getch() 

    elif(respm == 4):
        break

    else:
        print("não há essa opção, tente novamente")
        getch() 
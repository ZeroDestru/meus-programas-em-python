from random import randint
bat = "a"
vida = 1200
enem = 2000
iten = 3
pot = 500
tes = 's'
print("testanto batalha de RPG")

while(tes == 's'):

    print("wild beast apareceu, deseja batalhar contra ?")

    res = input()

    if(res == 's' ):
        print("lembrando que a ação é só a letra inicial: a attack, i itens, r correr")

        print(f"your life: {vida}")
        print(f"enemy life: {enem}")

        act = input("digite a ação: ")

        while(enem >= 0):

            if(act == 'a'):

                atk = randint(200, 400)
                at = randint(100, 200)

                vida -= at
                enem -= atk

            elif(act == 'i'):

                print("usar potion,p,") 
                us = input()

                if(us == 'p'):
                
                    vida += pot

                    atk = randint(200, 400)

                    vida -= atk

            print(f"your life: {vida}")
            print(f"enemy life: {enem}")

            act = input("digite a ação: ")

            if(vida <= 0):
                print("você morreu")

            elif(enem <= 0):
                print("inimigo derrotado")

    else:
        print("Então continuou a jornada")

    print("deseja testar novamente ?")
    tes = input("s/n")
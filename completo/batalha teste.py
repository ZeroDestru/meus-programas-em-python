from random import randint
bat = "a"
vida = 1200
enem = 2000
print("testanto batalha de RPG")

print("wild beast apareceu, deseja batalhar contra ?")

res = input()

if(res == "s" ):
    print("lembrando que a ação é só a letra inicial: a attack, c curar, r correr")

    act = input("digite a ação: ")

    if(act == "a"):
            print(f"your life: {vida}")

            print(f"enemy life: {enem}")

            input()

            while(enem >= 0):
                

                atk = randint(200, 400)
                at = randint(100, 200)

                print(f"seu atack {atk}")

                print(f"enemy atack {at}")

                input()

                vida -= at
                enem -= atk

                print(f"your life: {vida}")

                print(f"enemy life: {enem}")
                bat = input()



            if(vida <= 0):
                print("você morreu")

            elif(enem <= 0):
                print("inimigo derrotado")

else:
    print("Então continuou a jornada")
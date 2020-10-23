from random import randint

lnus = []
a = 0
b =0
tr = True
for i in range (50):

    lnus.append(randint(1,99))

while (tr):

    a = int(input("escolha a menor posição que deseja ver: "))

    b = int(input("agora a maior posição(máximo 50): "))

    if(a <= 0) or (a > b):
        print(f"número inválido, tente novamento um número maior que {a}")
    
    elif(b >= 51):
        print(f"número inválido, tente novamento um número menor que {b}")

    else:
        tr = False

for c in range(a-1,b):

    print(lnus[c], end=" ")
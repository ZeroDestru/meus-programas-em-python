from random import randint
a = 0
ap = 0
b = 0
bp = 0
c = 0
cp = 0

while(ap < 3) and (bp < 3) and (cp < 3):

    
    c = randint(1,2)
    b =randint(1,2)
    a = int(input("digite um valor entre 1 e 2 "))

    if(a == 1) or (a == 2):

        if(b == c) and (a != b):
            ap += 1

        elif (a == c) and (b != a):
            bp += 1

        elif(b == a) and (c != b):
            cp += 1

        else:
            ap += 0

        print(f"pontos, seu {ap}, do jogador b {bp}, do jogador c {cp}")
    else:
        print("valor inválido")
    
if(ap > bp) and (ap > cp):
    print("parabéns, você ganhou")

elif(bp > cp) and (bp > ap):
    print("ganhou o jogador b")

else:
    print("jogador c ganhou")

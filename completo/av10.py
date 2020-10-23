from random import randint

SURPRESINHA = []
MEGASENA = []
acertos = 0
a = 0
i = 0
while(i <= 6):

    nu = randint(1,60)
    if (nu not in SURPRESINHA):
        SURPRESINHA.append(nu)
        i += 1

for i in range(6):

    for j in range(6):

        if(SURPRESINHA[i] <= SURPRESINHA[j]):
            a = SURPRESINHA[j]
            SURPRESINHA[j] = SURPRESINHA[i]
            SURPRESINHA[i] = a


print(SURPRESINHA)
i = 1

while(i <= 6):

    nu = int(input(f" {i}/6 digite um numero: "))

    if(nu not in MEGASENA):

        MEGASENA.append(nu)
        i += 1


for i in range (6):
    if (MEGASENA[i] in SURPRESINHA):
            acertos += 1

print(f"você acertou {acertos} numeros")

if(acertos == 4):
    print("você fez uma Quadra")

elif(acertos == 5):
    print("você fez uma Quina")

elif(acertos == 6):
    print("você fez uma Sena")

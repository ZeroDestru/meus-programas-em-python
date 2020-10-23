from random import randint

somalin = []
somacolun = []
a = 0
b = 0
matriz = [0]*5

for i in range(5):
    matriz[i] = [0]*5

for i in range(5):
    for j in range(5):
        matriz[i][j] = randint(1,50)

print("a matriz abaixo tem")

for i in range(5):
    for j in range(5):

        print(matriz[i][j],end=' ')

    print()

for i in range(5):
    for j in range(5):
        
        b += matriz[j][i]
        a += matriz[i][j]

    somalin.append(a)
    somacolun.append(b)

for i in range(5):
    print(f"soma da linha {i} = {somalin[i]}")

for i in range(5):
    print(f"soma da coluna {i} = {somacolun[i]}")


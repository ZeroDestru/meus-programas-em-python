from random import randint

tr = True
matriz = []
num = 0
soma = []
a = 0
conferir = 0
matriz2 = []

while(tr):

    tam = int(input("qual o tamanho da matriz desejada ? "))

    if(tam >= 2):
        tr = False


confe = (tam+tam**3)/2

for i in range(tam):
    matriz.append([])

    for j in range(tam):
        
        tr = True

        while(tr):
            num = int(input(f"digite valor diferante para a posição {i}{j} "))
            #num = randint(1,tam**2)

            if(num <= tam**2):

                if(num in matriz2):
                    print("numero já está presente")

                else:
                    matriz[i].append(num)
                    matriz2.append(num)
                    tr = False

            else:
                print("numero inválido")

print()
print("matriz:")
print(matriz)
for i in range(tam):
    for j in range(tam):

        print(matriz[i][j],end=' ')

    print()

for i in range(tam):
    for j in range(tam):

        if(i == j):
            a += matriz[j][i]

if(a == confe):
    conferir += 1

soma.append("soma da diagonal principal")
soma.append(a)
a = 0

for i in range(tam):

    a += matriz[i][(tam-1)-i]

if(a == confe):
    conferir += 1

soma.append("soma da diagonal secundária")
soma.append(a)
a = 0

for i in range(tam):
    for j in range(tam):
        a += matriz[i][j]

    if(a == confe):
        conferir += 1

    soma.append(f"soma da linha {i}")
    soma.append(a)
    a = 0

for i in range(tam):
    for j in range(tam):
        a += matriz[j][i]

    if(a == confe):
        conferir += 1

    soma.append(f"soma da coluna {j}")
    soma.append(a)
    a = 0

if(conferir == (len(soma)/2)):
    soma.append("É um Quadrado Mágico")

else:
    soma.append("Não é um Quadrado Mágico")

for i in range(len(soma)):

    if(i%2 == 0):
        print()
        print(f"{soma[i]}",end=" = ")

    elif(i%2 == 1):
        print(f"{soma[i]}")
        print()
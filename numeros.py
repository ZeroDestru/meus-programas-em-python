from random import randint

matriz = []

for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(randint(1,50))


for i in range(5):
    for j in range(5):
        if(j > i):
            print(matriz[i][j],end=' ')
        else:
            print(' ',end=' ')

    print()
    
print("a diagonal secundária é:", end=' ')

for i in range(5):

    print(matriz[i][4-i],end=' ')
from random import randint

matriz = []
maior = []
maiorco = 0

for i in range(5):
    matriz.append([])

    for j in range(5):
        matriz[i].append(randint(0,99))

        print(matriz[i][j],end=' ')

        if(matriz[i][j] > maiorco):
            maior.append(matriz[i][j])
            maiorco = matriz[i][j]/2

    print()
    
maior.sort()

print(f"o segundo maior valor da matriz é = {maior[len(maior)-2]}")
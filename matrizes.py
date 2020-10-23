from random import randint
ma_i = int(input("quantas linhas na matriz ? "))
ma_j = int(input("quantas colunas na matriz ? "))
k = ma_i

matriz = [0]*ma_i
for i in range(ma_i):
    matriz[i] = [0]*ma_j
'''
for i in range(ma_i):
    for j in range(ma_j):
        matriz[i][j]=int(input(f"digite o valor localizado em i={i}, j={j})) 
'''

transposta = [0]*ma_i
for i in range(ma_i):
    transposta[i] = [0]*ma_j

for i in range(ma_i):
    for j in range(ma_j):
        matriz[i][j]=int(randint(1,50)) 

for i in range(ma_i):
    for j in range(ma_j):

        print(matriz[i][j],end=' ')

    print()

print("a diagonal principal é:",end=' ')

for i in range(ma_i):
    for j in range(ma_j):

        if(i == j):
            print(matriz[i][j],end=' ')
print()

print("a diagonal secundária é:", end=' ')

ge(ma_i):for i in ran

    print(matriz[i][(ma_i-1)-i],end=' ')

print()
print()
print("triângulo superior é:")

for i in range(ma_i):
    for j in range(ma_j):
        if(j > i):
            print(matriz[i][j],end=' ')
        else:
            print(' ',end=' ')

    print()

print("triângulo inferior é:")

for i in range(ma_i):
    for j in range(ma_j):
        if(j < i):
            print(matriz[i][j],end=' ')

    print()
print()
print("triângulo superior esquerdo é:")

for i in range(ma_i):
    for j in range(ma_j):
        if(j < k):
            print(matriz[i][j],end=' ')
    print()
    k-=1

k = ma_i
print()
print("triângulo inferior direito é:")

for i in range(ma_i):
    for j in range(ma_j):
        if(j > k):
            print(matriz[i][j],end=' ')
        else:
            print(' ',end=' ')
    print()
    k-=1

print()
print("transposta da matriz:")

for i in range(ma_i):
    matriz[i]

    for j in range(ma_j):

        transposta[i][j] = matriz[j][i]

for i in range(ma_j):
    for j in range(ma_i):

        print(transposta[i][j],end=' ')
    print()

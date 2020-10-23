matriz = [0]*5
matriz[0] = [1,2,3,4,5]
matriz[1] = [6,7,8,9,10]
matriz[2] = [11,12,13,14,15]
matriz[3] = [16,17,18,19,20]
matriz[4] = [21,22,23,24,25]
k = 4

transposta = [0]*5
for i in range(5):
    transposta[i] = [0]*5


print("a matriz:")

for i in range(5):
    for j in range(5):

        print(matriz[i][j],end=' ')

    print()

print("a diagonal principal é:",end=' ')

for i in range(5):
    for j in range(5):

        if(i == j):
            print(matriz[i][j],end=' ')
print()
print("a diagonal secundária é:", end=' ')

for i in range(5):

    print(matriz[i][4-i],end=' ')

print()
print()
print("triângulo superior é:")

for i in range(5):
    for j in range(5):
        if(j > i):
            print(matriz[i][j],end=' ')
        else:
            print(' ',end=' ')

    print()

print("triângulo inferior é:")

for i in range(5):
    for j in range(5):
        if(j < i):
            print(matriz[i][j],end=' ')

    print()
print()
print("triângulo superior esquerdo é:")

for i in range(5):
    for j in range(5):
        if(j < k):
            print(matriz[i][j],end=' ')
    print()
    k-=1

k = 4
print()
print("triângulo inferior direito é:")

for i in range(5):
    for j in range(5):
        if(j > k):
            print(matriz[i][j],end=' ')
        else:
            print(' ',end=' ')
    print()
    k-=1

print()
print("transposta da matriz:")

for i in range(5):
    matriz[i]

    for j in range(5):

        transposta[i][j] = matriz[j][i]

for i in range(5):
    for j in range(5):

        print(transposta[i][j],end=' ')
    print()


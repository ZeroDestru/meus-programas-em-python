pala = input("digite a palavra codificada: ")
deco = []

for i in range(1,len(pala)-1):
    if(pala[i-1] == 'p') and (pala[i+1] == 'p') or pala[i+1] == ' ':
        deco.append(pala[i])

    if(pala[i] == ' '):
        deco.append(' ')

deco.append(pala[len(pala)-1])
for i in range(len(deco)):
    print(deco[i], end='')

input()
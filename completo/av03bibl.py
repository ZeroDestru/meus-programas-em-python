
def transform(text, mat, codig):
    co = []

    for i in range(len(text)):
        if(text[i] == ' '):
            co.append(30)
        else:
            co.append(codig.index(text[i])+1)

    return multi(co, mat, True)


def decodificar(decof, mat, codig):
    text2 = []

    codif = multi(decof, mat, False)

    for i in range(len(codif)):
        if(codif[i] == 30):
            text2.append(' ')
        else:
            text2.append(codig[codif[i]-1])

    text2 = ' '.join(text2)

    return text2

def multi(co, mat, fn):
    matriz = [[],[]]
    codif = []

    for i in range(len(co)//2):
        matriz[0].append(co[i])
        matriz[1].append(co[(len(co)//2)+i])

    if(len(co)%2 == 1):
        matriz[0].append(co[len(co)-1])
        matriz[1].append(1)

    for i in range(2):
        for j in range(len(matriz[i])-1):
            codif.append((matriz[0][j]*mat[i][0]) + (matriz[1][j]*mat[i][1]))
            
    if(fn):
        codif.append((matriz[0][len(matriz[0])-1]*mat[0][1]) + (1*mat[1][0]))
    else:
        codif.append((matriz[0][len(matriz[0])-1]*mat[0][1]) + (1*mat[1][1]))
    

    return codif

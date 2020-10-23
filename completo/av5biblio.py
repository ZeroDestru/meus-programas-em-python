def insercao(a,b,cores):
    cores

    cores.append((a,b))

def consulta(cor,cores):

    for codig in cores:
        if(codig[1] == cor):
            return codig[0]

    return "cor não cadastrada"

def listagem(cores):

    for i in range(len(cores)):

        print(f'cor {cores[i][1]}: codigo {cores[i][0]}')

def menu(cores):
    res= int(input('informe o que deseja \n1.Inserção no código rgb \n2.Consulta o código \n3.Litar o código\n'))

    if res == 1:
        a,b = input("digite o codigo e a cor que representa separando cada um por espaço: ").split(' ')
        b.lower()
        insercao(a,b,cores)

    if res == 2:
        cor = input("digite a cor que deseja: ").lower()
        print(f"código da cor:{cor} é {consulta(cor, cores)}")

    if res == 3:
        listagem(cores)

    ter= input('\ndeseja continuar? (s/n)').lower()

    if ter == "s":

        return menu(cores)

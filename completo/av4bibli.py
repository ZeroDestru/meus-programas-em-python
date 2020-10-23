def maiorposi(num):
    num2 = num//10

    if(num2 != 0):
        num//=10
        return maiorposi(num)
    return num

def menu():
    a,b = input("digite os numeros que deseja(lembrando que o espaço é para separa qual é o 1 e o 2): ").split(' ')

    Ama = maiorposi(int(a))
    Bma = maiorposi(int(b))

    print(f"a soma dos digitos mais significativos é {Ama+Bma}")

    res = input("deseja fazer o cálculo mais uma vez ? s/n ").lower()

    if(res == 's'):
        return menu()

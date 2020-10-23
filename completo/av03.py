import av03bibl

matco = [[3,1],[2,1]]
matde = [[1,-1],[-2,3]]
codig = 'abcdefghijklmnopqrstuvwxyz.!#'
text = ''
decof = []

print("Bem vindo a o decodificador de mensagens: ")

while(True):
    
    print("Qual a opção que deseja fazer ?")
    print("1 - Criptografar mensagem")
    print("2 - Decriptografar mensagem")
    print("3 - Sair")
    mens = int(input())

    if(mens == 1):
        text = str(input("digite a mensagem: "))

        print(f"sua mensagem criptografada é: {av03bibl.transform(text,matco,codig)}")

    elif(mens == 2):

        print("digite a mensagem criptografada, digitando um numero e de cada vez")
        while(True):
            decof.append(int(input("numero: ")))

            print("deseja continuar ? s/n")
            men = input().lower()

            if(men == 'n'):
                break
        
        print(f"sua mensagem é: {av03bibl.decodificar(decof, matde, codig)}")

    elif(mens == 3):
        break
    else:
        print("não existe essa opção, tente novamente")

    input()
    text = ''
    decof = []



num = 15
div = 2

while(div <= 20):

    if(num%div == 0):
        div += 1
        

    else:
        num += 1
        div = 2

print(f"{num} é divisível por todos os númerosde 1 até 15")
num1 = int(input())
num2 = int(input())
n = 1
n1 = 1
m1 = 0
m2 = 0
while(n < num1):

    if(num1%n == 0):
       

        m1 += n
        n += 1


    else:
        n += 1

    while(n1 < num2):

        if(num2%n1 == 0):
            

            m2 += n1
            n1 += 1


        else:
            n1 += 1

if(m1 == num2) and (m2 == num1):
    print(f"{num1} e {num2} são amigos")
    print(f"porque a soma dos divisores de cada um, respectivamente {m1}, e {m2}")

else:
    print(f"{num1} e {num2} não são amigos")
    print(f"porque a soma dos divisores de cada um, respectivamente {m1}, e {m2}")
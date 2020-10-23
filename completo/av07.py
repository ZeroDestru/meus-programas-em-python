from random import randint

num = 0
num2 = 0
num3 = 0
num4 = 1
num5 = 0
a = 0
b = 0
c = 0
d = 0
tent = 0
tr = True

while(tr):
    num = randint(100,999)

    for i in range (3):

        num2 = num%10

        if(i == 0):
            a = num2
        elif(i == 1):
            b = num2
        else:
            c = num2
        
        num //= 10

    if(a != b) and (a != c) and (b != c):
        tr = False
num = (a*100)+ (b*10) + c

while(num != 495):
    
    num5 = num
    for i in range (3):
        num2 = num%10
        if(i == 1):
            a = num2
        elif(i == 2):
            b = num2
        else:
            c = num2
        num //= 10
    
    if(b > a):
        d = b
        b = a
        a = d
        

    if(c > a):
        d = c
        c = a
        a = d  
    
    if(c > b):
        d = c
        c = b
        b = d
         

    num3 = (a*100) + (b*10) + c
    num4 = (c*100) + (b*10) + a

    num = num3-num4 
    
    print(f"o menor número, e maior número formado por {num5}, são respectivamente {num3}, e {num4}")
    print(f"isso dá {num3} - {num4} = {num}")
    tent += 1
    
print(f"teve que ter {tent} tentativas para chegar a 495")
    

x = True
num = 100
while(x):

    cen = num//100
    dez = num//10 - cen*10
    uni = num%10
    
    if(cen < dez) and (dez < uni):
        print(num)
        num += 1
        x = num < 1000

    else:
        num +=1
        x = num < 1000
        
num = int(input())

n = 1
while(n <= num):

    if(num%n == 0):
        print(f"{n} é um divisor")
        n += 1

    else:
        n += 1


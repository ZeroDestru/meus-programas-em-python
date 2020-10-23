from random import randint

A = []
num = 0
a = 0
for i in range (10):
    A.append(randint(1,50))
    #A.append(int(input()))
    
for i in range(10):

    for j in range(10):

        if(A[i] <= A[j]):
            a = A[j]
            A[j] = A[i]
            A[i] = a

#prin(A)

num = int(input("digite um valor qual: "))

for i in range(10):
    if(num < A[i]):
        A.insert(i,num)
        break

print(A)
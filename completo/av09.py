from random import randint

list1 = []
list2 = []
list3 = []
pos = 9

for i in range (10):
    list1.append(randint(1,50))
    list2.append(randint(1,50))

for j in range (10):
    list3.append(list1[j] + list2[9-j])

print(f"O vetor 1 é {list1}")
print(f"O vetor 1 é {list2}")
print("a soma cada elemento com a posição inversa de cada lista dá")
print(f"o Vetor etor formado é {list3}")
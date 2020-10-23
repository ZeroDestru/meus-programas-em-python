from random import randint

str = "eu quero saber "

print(str)

strb = list(str)

print(strb)

strc = ' '.join(strb)

print(strc)

'''
pode ser na mesma variavel
transformando str
'''
'''
str.starswith("letra/nome descrito")
str.endswith("letra/nome descrito")
'''
'''
caps faz diferença
'''

str.upper()
str.lower()

'''
transforma mas não converte
para real alteração tem que atribuir ("variavel = str.upper/lower()")
'''
'''
print(str.count('o que desejar'))
print(str.find(o que desejar"))
print(str.rfind(o que desejar"))
'''
'''
apenas conta quantos tem, mas o "in" confere se tem o que é para contar
o find, só acha o primeiro, para a próxima voce deve(str.find("palavra", inico,fim))
'''
'''
sepa = str.split('caracter que desejar)
'''
'''
ele vai separar no caracter que quer
'''

'''
troca = str.replace("o que desejar", "qual quer", numero de vezes que desejar)
'''





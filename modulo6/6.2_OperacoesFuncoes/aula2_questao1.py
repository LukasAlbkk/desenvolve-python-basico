import random 

lista = []
for i in range (0,20):
    n = random.randint(-100,100)
    lista.append(n)
print(sorted(lista))
print(lista)
print(lista.index(max(lista)))
print(lista.index(min(lista)))

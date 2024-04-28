import random

lista1 = []
lista2 = []
lista3 = []

for i in range(0,20):
    lista1.append(random.randint(0,50))
    lista2.append(random.randint(0,50))

for i in lista1:
    if i in lista2 and i not in lista3:
        lista3.append(i)

print("Lista 1: ",lista1)
print("Lista 2: ",lista2)
print("Intersecão: ",lista3)

for i in range(len(lista3)):
    elemento = lista3[i]
    contagem1 = lista1.count(elemento)
    contagem2 = lista2.count(elemento)
    print(elemento,": (lista1 =",contagem1,",lista2 =",contagem2,")")
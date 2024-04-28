lista1 = []
lista2 = []
lista3 = []

n1 = int(input("Digite a quantidade de elementos da lista: "))
print(f"Digite os {n1} elementos da lista1: ")

for i in range(n1):
    elem = int(input())
    lista1.append(elem)

n2 = int(input("Digite a quantidade de elementos da lista: "))
print(f"Digite os {n2} elementos da lista2: ")

for i in range(n2):
    elem = int(input())
    lista2.append(elem)

i, j = 0, 0
while i < n1 or j < n2:
    if i < n1:
        lista3.append(lista1[i])
        i += 1
    if j < n2:
        lista3.append(lista2[j])
        j += 1

print("Lista Intercalada: ",lista3)
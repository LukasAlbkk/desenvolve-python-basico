lista = []

while True:
    n = int(input("Digite o número para a lista, pelo menos 4, se zero finaliza: "))
    lista.append(n)
    if n == 0 and len(lista) >= 4:
        break
        
print(lista)
print(lista[0:3])
print(lista[:-3:-1])
print(lista[::-1])
print(lista[0::2])
print(lista[1::2])

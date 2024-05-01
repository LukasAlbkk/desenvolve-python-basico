import random

lista = []
for i in range(20):
    lista.append(random.randint(-10,10))

intervalo = []
tamanho = 0 
intervalo_maior = 0
tamanho_maior = 0  

for i in lista:
    if i < 0:
        tamanho += 1
        intervalo.append(i)
    else:
        if tamanho > tamanho_maior:
            tamanho_maior = tamanho
            intervalo_maior = intervalo
        tamanho = 0
        intervalo = []

if tamanho > tamanho_maior:
    tamanho_maior = tamanho
    intervalo_maior = intervalo[:]
    
print(lista)
print(intervalo_maior)
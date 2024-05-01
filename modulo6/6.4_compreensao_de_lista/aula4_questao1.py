lista1 = []
for i in range(20,51):
    lista1.append(i)
pares = [i for i in lista1 if i % 2 == 0]
print(pares)


lista2 = [1,2,3,4,5,6,7,8,9]
quadrados = [i ** 2 for i in lista2]
print(quadrados)


lista3 = []
for i in range(1,101):
    lista3.append(i)
div_7 = [i for i in lista3 if i % 7 == 0]
print(div_7)


lista4 = []
for i in range(0,30,3):
    lista4.append(i)
par_impar = ["par" if i % 2 == 0 else "ímpar" for i in lista4 ]
print(par_impar)
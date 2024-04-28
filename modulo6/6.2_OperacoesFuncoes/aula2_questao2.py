import random

num_elementos = random.randint(5,20)
print("Número de elementos: ",num_elementos)
elementos = []

for i in range(0,num_elementos):
    n = random.randint(1,10)
    elementos.append(n)
print(elementos)
print("Soma: ",sum(elementos))
print(f"Média: {sum(elementos)/len(elementos):.2f}")


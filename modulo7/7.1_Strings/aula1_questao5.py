frase = input("Digite uma frase: ")
indice = []
vogais = 0
for i in range(len(frase)):
    if frase[i] in "aeiou":
        vogais += 1
        indice.append(i)
print(vogais,"vogais")
print("Índices ",indice)
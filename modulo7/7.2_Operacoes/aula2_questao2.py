frase = input("Digite uma frase: ")

for i in "aeiou":
    frase = frase.replace(i,"*")
print(frase)
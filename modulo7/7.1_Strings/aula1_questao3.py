frase = input("Digite a frase: ")
count = 0 

for i in frase:
    if i == " ":
        count += 1
print(count)
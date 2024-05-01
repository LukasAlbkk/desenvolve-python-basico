
frase = input("Digite a frase: ")

vogais = [i for i in frase if i.lower() in 'aeiou']
vogais.sort()

consoantes = [i for i in frase if i.isalpha() and i.lower() not in 'aeiou']


print(frase)
print(vogais)
print(consoantes)


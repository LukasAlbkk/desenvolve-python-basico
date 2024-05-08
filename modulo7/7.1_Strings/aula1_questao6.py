def anagramas(palavra1, palavra2):
    return sorted(palavra1.lower()) == sorted(palavra2.lower())

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

palavras_na_frase = frase.split()
anagramas = [palavra for palavra in palavras_na_frase if anagramas(palavra, palavra_objetivo)]

print("Anagramas:", anagramas)

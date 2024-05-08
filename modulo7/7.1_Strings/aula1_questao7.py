import random

chave = random.randint(1,10)

def encrypt(nomes,chave):
    cifrados = []
    for i in nomes:
        cifrado = ""
        for j in i:
            a = ord(j) + chave 
            cifrado += chr(a)
        cifrados.append(cifrado)
    return cifrados
    
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
a = encrypt(nomes,chave)
print(a)
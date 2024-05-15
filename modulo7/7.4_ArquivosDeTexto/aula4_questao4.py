import random

with open('gabarito_forca.txt','r') as arquivo:
    palavras = arquivo.read().splitlines()
    palavra_aleatoria = random.choice(palavras)
    tamanho = len(palavra_aleatoria)
print(palavra_aleatoria) 

with open('gabarito_enforcado.txt','r') as arquivo2:
    forca = arquivo2.read().split("=========")

underscore = ["-"] * tamanho
print("FORCA : ",*underscore, sep='') # o underscore nao estava aparencendo direito ai troquei pelo -

def imprime_enforcado(x):
    print(forca[x - 1])
    print("ERRO ! Número:",x)
    if x == 7:
        print("O jogo acabou!")
        print("A palavra era:",palavra_aleatoria)
        return "Fim"

count = 0
while True:
    letra_encontrada = False
    letra = input("Digite uma letra: ")
    for i in range(len(palavra_aleatoria)):
        if letra == palavra_aleatoria[i]:
            underscore[i] = letra
            letra_encontrada = True
    print(*underscore,sep='')
    if not letra_encontrada:
        count += 1
        a = imprime_enforcado(count)
        if a == "Fim":
            break

        

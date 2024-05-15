with open('frase.txt','r') as r:
    novo = []
    for i in r:
        palavra = i.split()
        novo.extend(palavra)
        novo.append("\n")

with open("palavra.txt","w") as arquivo:
    for i in novo:
        arquivo.write(i+"\n")
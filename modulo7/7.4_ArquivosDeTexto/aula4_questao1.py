import os

frase = input("Digite uma frase: ")
f = open('frase.txt','w')
f.write(frase)
f.close()
print(os.getcwd())
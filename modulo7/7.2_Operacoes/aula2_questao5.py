import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    frase_embaralhada = []
    for i in palavras:
        if len(i) <= 3:
            frase_embaralhada.append(i)
        else:
            primeira = i[0]
            ultima = i[-1]
            internas = list(i[1:-1])
            random.shuffle(internas)
            embaralhada = primeira + ''.join(internas) + ultima 
            frase_embaralhada.append(embaralhada)
    return ' '.join(frase_embaralhada)

n = input()
a = embaralhar_palavras(n)
print(a)
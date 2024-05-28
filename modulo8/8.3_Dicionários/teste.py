with open('estomago.txt','r') as texto_estomago:
    count = {}
    texto = texto_estomago.read()
    palavras = texto.split()
    for palavra in palavras:
        if palavra in count:
            count[palavra] += 1
        else:
            count[palavra] = 1
    print(count)
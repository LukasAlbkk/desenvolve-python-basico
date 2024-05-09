def remove_pontuacao(frase):
    for i in '.,;?!':
        frase = frase.replace(i,'')
    return frase

while True:
    frase = input("Digite uma frase e fim para encerrar: ")
    frase = frase.lower()
    frase = frase.replace(" ","")
    frase = remove_pontuacao(frase)
    frase_inversa = frase[::-1]
    if frase == "Fim":
        break
    if frase_inversa == frase:
        print(frase,"É palíndromo!")
    else:
        print(frase,"Não é palíndromo!")
   


count = 0
maior = 0
nonato = 0
iria = 0
print("PRIMEIRAS 25 LINHAS: \n")
with open("estomago.txt","r") as estomago:
    for linhas in estomago:
        if count < 25:
            print(linhas, end="")
        count += 1
        if len(linhas) > maior:
            maior = len(linhas)
            linha_maior =  linhas
        if "nonato" in linhas.lower():
            nonato += 1
        if "íria" in linhas.lower():
            iria += 1

    print("NÚMERO DE LINHAS DO ARQUIVO: ",count)
    print("MAIOR LINHA: \n",linha_maior)   
    print("NÚMERO DE MENÇÕES DE NONATO:",nonato)    
    print("NÚMERO DE MENÇÕES DE ÍRIA:",iria)    

n = int(input())
cont = 0
quant_sapos = 0
quant_ratos = 0
quant_coelhos = 0

while cont < n:
    quant = int(input())
    tipo = input()
    if tipo == 'S':
        quant_sapos += quant
    elif tipo == 'R':
        quant_ratos += quant    
    elif tipo == 'C':
        quant_coelhos += quant    
    cont += 1

total = quant_coelhos + quant_ratos + quant_sapos
perc_sapos = (quant_sapos / total) * 100
perc_coelhos = (quant_coelhos / total) * 100
perc_ratos = (quant_ratos / total) * 100
print(f"Total: {total} cobais")
print(f"Total de coelhos: {quant_coelhos}")
print(f"Total de ratos: {quant_ratos}")
print(f"Total de sapos: {quant_sapos}")
print(f"Percentual de coelhos: {perc_coelhos:.2f}%")
print(f"Percentual de ratos: {perc_ratos:.2f}%")
print(f"Percentual de sapos: {perc_sapos:.2f}%")

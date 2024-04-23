distancia = int(input("Digite a distâcia: "))
peso =  int(input("Digite o peso: "))
if distancia <= 100:
    calculo = peso
if distancia >= 101 and distancia <= 300:
    calculo = 1.5 * peso
if distancia > 300:
    calculo = 2 * peso

if peso > 10:
    calculo += 10

print(calculo)
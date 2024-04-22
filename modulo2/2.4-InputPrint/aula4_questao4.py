#entrada do valor a ser analisado
entrada = int(input("digite o valor R$: "))
#calculo com divisao inteira de acordo com o valor da nota 
notas_100 = entrada // 100
#atualizacao do valor da entrada de acordo com a nota que ja foi usada 
entrada = entrada % 100
notas_50 = entrada // 50
entrada = entrada % 50
notas_20 = entrada // 20
entrada = entrada % 20
notas_10 = entrada // 10
entrada = entrada % 10
notas_5 = entrada // 5
entrada = entrada % 5
notas_1 = entrada // 1
entrada = entrada % 1
#saidas da quantidade respectiva de notas 
print(f"{notas_100} nota(s) de 100")
print(f"{notas_50} nota(s) de 50")
print(f"{notas_20} nota(s) de 20")
print(f"{notas_10} nota(s) de 10")
print(f"{notas_5} nota(s) de 5")
print(f"{notas_1} nota(s) de 1")
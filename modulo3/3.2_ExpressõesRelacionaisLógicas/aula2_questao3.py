idade = int(input("Qual a sua idade? "))
verifica_idade = idade >= 16 and idade <= 18
jogou  = input("Já jogou pelo menos 3 jogos de tabuleiro? ")
sim = jogou == "True"
nao = jogou == "False"
jogos = int(input("Quantos jogos já venceu? "))
verifica_3 = jogos >= 1
total = verifica_idade and sim and verifica_3
print(bool(total))
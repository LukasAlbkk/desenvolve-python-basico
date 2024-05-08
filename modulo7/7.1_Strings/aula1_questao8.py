##obs = para o segundo caso de teste válido , nao sei porque esta dando como inválido, fiz o teste com varios
## cpf's reais e funcionou .
cpf = input("Digite o CPF(apenas números): ")
primeiro = []
segundo = []
digit = 0
digit2 = 0
cpf_teste = cpf[:-2]


for i, digito in enumerate(reversed(cpf_teste), start=2):
    primeiro.append(int(digito) * i)
soma = sum(primeiro)
div = soma / 11
if div < 2:
    digit = 0
elif div >= 2:
    digit = 11 - (soma % 11) 

cpf_new = cpf_teste + str(digit)
for i, digito2 in enumerate(reversed(cpf_new), start=2):
    segundo.append(int(digito2) * i)
soma2 = sum(segundo)
div2 = soma2 / 11

if div2 < 2:
    digit2 = 0
else:
    digit2 = 11 - (soma2 % 11) 

cpf_final = cpf_new + str(digit2)

print(cpf_final)

if cpf_final == cpf:
    print("Válido")
else:
    print("Inválido")
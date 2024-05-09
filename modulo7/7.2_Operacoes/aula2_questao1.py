meses = [' ','janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
data = input("Digite a sua data de nascimento: ")
dia, mes, ano = data.split("/")
mes_nome = meses[int(mes)]

print(f"Você nasceu em {dia} de {mes_nome} de {ano}.")
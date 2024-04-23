genero = input("Digite o seu gênero(F ou M): ")
homem = genero == "M"
mulher = genero == "F"
idade = int(input("Digite a sua idade: "))
tempo_servico = int(input("Digite o seu tempo de serviço: "))
verifica = (mulher and idade > 60) or (tempo_servico >= 30) or (homem and idade > 65) or (idade == 60 and tempo_servico >= 25)
print(bool(verifica))
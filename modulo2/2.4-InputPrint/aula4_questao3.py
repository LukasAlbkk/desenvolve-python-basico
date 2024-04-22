#entradas dos produtos , seus precos e suas quantidades
p1 = input("Digite o nome do produto 1: ")
preço1 = float(input("Digite o preço unitário do produto 1: "))
q1 = int(input("Digite a quantidade do produto 1: "))
p2 = input("Digite o nome do produto 2: ")
preço2 = float(input("Digite o preço unitário do produto 2: "))
q2 = int(input("Digite a quantidade do produto 2: "))
p3 = input("Digite o nome do produto 3: ")
preço3 = float(input("Digite o preço unitário do produto 3: "))
q3 = int(input("Digite a quantidade do produto 3: "))
#calculo do preco total da compra 
preço_total = float((preço1*q1) + (preço2*q2) + (preço3*q3))
#saida com as duas casas decimais do preco total
print(f"Total: R${preço_total:.2f}")
num = input("Digite o número de telefone: ")
if len(num) == 8:
   num = "9" + num

print("Número completo: ",num[0:5]+"-"+num[5:])

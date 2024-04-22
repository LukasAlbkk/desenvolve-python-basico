#leitura e conversão para inteiro da temperatura em fahrenheit 
temperaturaF = int(input("qual a temperatura em fahrenheit? "))
#Processamento do valor da temperatura em Celsius
temperaturaC = (temperaturaF - 32) * (5/9)
#Saída já formatada em inteiros para Celsius
print(f"{temperaturaF} graus Fahrenheit sao {int(temperaturaC)} em Celsius")
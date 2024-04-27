import random

num = random.randint(1,10)
i = 1
while i == 1:
    entrada = int(input("Tente adivinhar o número entre 1 e 10: "))
    if entrada > num and abs(entrada - num) >= 3:
        print("Muito alto, tente novamente! ")
    if entrada < num and abs(entrada - num) >= 3:
        print("Muito baixo, tente novamente! ")
    elif abs(entrada - num) <= 2:
        print("Você está perto!!")
    if entrada == num:
        print("Você acertou !!")
        break
        
classe = input("Escolha a classe(guerreiro, mago ou arqueiro): ")
guerreiro = classe == "guerreiro"
mago = classe == "mago"
arqueiro = classe == "arqueiro"
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))
guerreiro = forca >= 15 and magia <= 10
mago = forca <= 10 and magia >= 15
arqueiro = (forca > 5 and forca <= 15) and (magia > 5 and magia <= 15)
resultado = (classe == "guerreiro" and guerreiro) or (classe == "mago" and mago) or (classe == "arqueiro" and arqueiro)
print("Pontos de atributo consistentes com a classe escolhida: ",bool(resultado))
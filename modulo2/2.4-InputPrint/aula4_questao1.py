#leitura do comprimento do terreno em inteiros
comprimento = int(input("qual o comprimento do terreno? "))
#leitura da largura do terreno em inteiros
largura = int(input("qual a largura do terreno? "))
#leitura do preco do m2 do terreno em ponto flutuante
preço = float(input("qual preço? "))
#impressao na formatacao de ponto flutuante do tamanho do terreno assim como seu preco total
print(f"o terreno possui {comprimento * largura} e custa {preço * (comprimento * largura)}")
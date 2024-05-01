lista = []

while True:
    url = input("Digite o url: ")
    if url == "Fim":
        break
    lista.append(url)
    
dominios = []

for url in lista:
    dominio = url[4:-4] 
    dominios.append(dominio)

print("dominios:", dominios)

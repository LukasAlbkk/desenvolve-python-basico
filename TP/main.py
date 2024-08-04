import csv

## Produtos e servicos

produtos = []

def salvar_produtos():
    with open('produtos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(produtos)

def incluirProduto(nome,preco,quantidade):
    produto = [nome,preco,quantidade]
    produtos.append(produto)
    salvar_produtos()

def getProduto(nome):
    with open('produtos.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for linha in reader:
            nomeproduto, preco, quantidade = linha
            if nomeproduto == nome:
                return {nomeproduto,preco,quantidade}
    return 0

def alterar(letra, nomeProd, novoValor):
    with open('produtos.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for linha in reader:
            if letra == "p":
                if linha[0] == nomeProd:
                    linha[1] = str(novoValor)
            elif letra == "q":
                if linha[0] == nomeProd:
                    linha[2] = str(novoValor)
            produtos.append(linha)
        else: print("digite p ou q")
    with open('produtos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(produtos)

def deletarProduto(nomeProd):
    with open('produtos.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for linha in reader:
            if linha[0] != nomeProd:
                produtos.append(linha)
    with open('produtos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(produtos)

def getProdSortbyPrice():
    ordenado = []
    with open('produtos.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for linha in reader:
            nome = linha[0]
            preco = linha[1]
            ordenado.append((nome,preco))
        ordenado.sort(key=lambda x: x[1]) 
    return ordenado

def getProdSortbyQuant():
    ordenado = []
    with open('produtos.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for linha in reader:
            nome = linha[0]
            quant = linha[2]
            ordenado.append((nome,quant))
        ordenado.sort(key=lambda x: x[1]) 
    return ordenado

## usuarios

usuarios = []

def salvarUser():
     with open('usuarios.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(usuarios)

def addUser(login,senha,cargo):
    senhavalida = criarSenha(senha)
    user = [login,senhavalida,cargo]
    usuarios.append(user)
    salvarUser()

def removerUser(login): ##para os gerentes apenas
    with open('usuarios.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for linha in reader:
            if linha[0] != login:
                usuarios.append(linha)
    with open('usuarios.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(usuarios)

def validador_senha(senha):
    if len(senha) >= 8 and not senha.islower() and not senha.isupper() :
        for i in senha:
            if i.isdigit():      
                caracter = "!@#$%*()+=-_"
                for i in caracter:
                    if i in senha :
                        return True
    return False

def criarSenha(senha):
    valido = validador_senha(senha)
    if (valido == False):
        print("A senha não segue os critérios adequados")
    else:
        return senha


def alterarSenha(login,novaSenha): ##para qualquer usuario
    with open('usuarios.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for linha in reader:
            if linha[0] == login:
                linha[1] = criarSenha(novaSenha)
            usuarios.append(linha)
    with open('usuarios.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(usuarios)

def getUser():
    users = []
    with open('usuarios.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for linha in reader:
            users.append(linha[0])
    return users

def getUserIsValid(login,senha):
    with open('usuarios.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for linha in reader:
            if ((linha[0] == login) and (linha[1] == senha)): return True
        else : return False

def getCargo(login):
    with open('usuarios.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for linha in reader:
            if linha[0] == login:
                if linha[2].lower() == "gerente":
                    return "g"
                elif linha[2].lower() == "funcionario":
                    return "f"
    return None


def interfaceUsuario():
    
    print("Bem-vindo ao sistema do supermercado!")
    while True:
        print("\n1. Criar perfil\n2. Login\n3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            login = input("Escolha um login: ")
            print("OBS: Sua senha deve conter pelo menos 8 caracteres, possuir um a letra maiúscula e um caracter especial")
            senha = input("Escolha uma senha: ")
            cargo = input("Digite o cargo (Gerente/Funcionario): ")
            if cargo.lower() in ['gerente', 'funcionario']:
                addUser(login, senha, cargo)
                print("Perfil criado com sucesso!")
            else:
                print("Cargo inválido. Tente novamente.")
        elif opcao == '2':
            login = input("Login: ")
            senha = input("Senha: ")
            usuario = getUserIsValid(login,senha)
            cargo = getCargo(login)
            if usuario == True:
                if cargo == "g":
                    interfaceGerente()
                elif cargo == "f":
                    interfaceFuncionario()
                else:
                    print("Cargo não reconhecido.")
            else:
                print("Login ou senha incorretos.")
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def interfaceGerente():
    while True:
        print("\n--- Menu Gerente ---")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Alterar produto")
        print("4. Listar produtos por preço")
        print("5. Listar produtos por quantidade")
        print("6. Adicionar usuário")
        print("7. Remover usuário")
        print("8. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            incluirProduto(nome, preco, quantidade)
        elif opcao == '2':
            nome = input("Nome do produto a ser removido: ")
            deletarProduto(nome)
        elif opcao == '3':
            nome = input("Nome do produto a ser alterado: ")
            novoPreco = input("Novo preço (deixe vazio para não alterar): ")
            novaQuantidade = input("Nova quantidade (deixe vazio para não alterar): ")
            novoPreco = float(novoPreco) if novoPreco else None
            novaQuantidade = int(novaQuantidade) if novaQuantidade else None
            alterar(nome, novoPreco, novaQuantidade)
        elif opcao == '4':
            p = getProdSortbyPrice()
            print(p)
        elif opcao == '5':
            p = getProdSortbyQuant()
            print(p)
        elif opcao == '6':
            login = input("Login do novo usuário: ")
            senha = input("Senha do novo usuário: ")
            cargo = input("Cargo do novo usuário (Gerente/Funcionario): ")
            addUser(login, senha, cargo)
        elif opcao == '7':
            login = input("Login do usuário a ser removido: ")
            removerUser(login)
        elif opcao == '8':
            break
        else:
            print("Opção inválida. Tente novamente.")

def interfaceFuncionario():
    while True:
        print("\n--- Menu Funcionário ---")
        print("1. Alterar produto")
        print("2. Listar produtos por preço")
        print("3. Listar produtos por quantidade")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do produto a ser alterado: ")
            novoPreco = input("Novo preço (deixe vazio para não alterar): ")
            novaQuantidade = input("Nova quantidade (deixe vazio para não alterar): ")
            novoPreco = float(novoPreco) if novoPreco else None
            novaQuantidade = int(novaQuantidade) if novaQuantidade else None
            alterar(nome, novoPreco, novaQuantidade)
        elif opcao == '2':
            p = getProdSortbyPrice()
            print(p)
        elif opcao == '3':
            p = getProdSortbyQuant()
            print(p)
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")


interfaceUsuario()
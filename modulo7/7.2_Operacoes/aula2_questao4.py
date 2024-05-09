def validador_senha(senha):
    if len(senha) >= 8 and not senha.islower() and not senha.isupper() :
        for i in senha:
            if i.isdigit():      
                caracter = "!@#$%*()+=-_"
                for i in caracter:
                    if i in senha :
                        return True
    return False

senha = input("Digite a sua senha: ")
a = validador_senha(senha)
print(a)
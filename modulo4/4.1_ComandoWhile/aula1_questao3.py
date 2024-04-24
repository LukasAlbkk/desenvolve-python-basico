n1 = int(input())
n2 = int(input())
n3 = int(input())
m = (n1 + n2 + n3)/3
if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

print("Fim")
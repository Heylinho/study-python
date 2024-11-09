print("Digite o número e mostrarei se é PAR ou IMPAR")
numero = int(input("Digite o número inteiro: "))

resto = numero % 2

if resto == 0:
    print(f"O seu número {numero} é igual a PAR")
else:
    print(f"O seu númeor {numero} é igual a IMPAR")
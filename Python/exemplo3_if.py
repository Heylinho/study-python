idade = int(input("Qual é sua idade: "))

if idade >= 70:
    print("Você pode votar, mas não é obrigatório")
elif idade >= 18:
    print("Você é obrigatório a votar")
elif idade >= 16:
    print("Você pode votar")
else:
    print("Você não pode votar")

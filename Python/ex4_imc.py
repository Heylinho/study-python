altura = float(input("Digite a sua altura: "))
peso = float(input("Digite a sua peso(kg): "))

res = peso / (altura * altura)

print(f"Você tem um IMC de {res:.2f}")

if res <= 18.5:
    print("Abaixo do peso")
elif res <=24.9:
    print("Peso normal")
elif res <=29:
    print("Sobrepeso")
else:
    print("Obesidade")


print("Calculador de promoção!")

compra = float(input("Você foi ao mecardo e gasto quantos? R$: "))

if compra > 200:
    promo = compra * 0.85
    print(f"Você gasto {compra} e recebeu um desconto de 15%!! preço da compra agora é : {promo}")

elif compra > 100:
    promo = compra * 0.90
    print(f"Você gasto {compra} e recebeu um desconto de 10%!! preço da compra agora é : {promo}")
else:
    promo = compra * 0.95
    print(f"Você gasto {compra} e recebeu um desconto de 5%!! preço da compra agora é : {promo}")
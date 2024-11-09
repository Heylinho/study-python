print("Entre na sua conta!")

nome = input("Qual é seu login: ")
senha = float(input("Qual é a sua senha: "))

if senha != 123456:
    print("Login errado!")
else:
    if nome != "admin":
        print("Acesso Limitado!")
    else:
        print("Full Acesso")
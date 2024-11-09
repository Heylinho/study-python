print("Conversor de temperatura")

calor = float(input("Qual é temperatura atual: "))

print("Agora escolha entre CELSIUS ou  FAHRENHEIT")
opcao = int(input("[1 - CELSIUS | 2 - FAHRENHEIT]: "))

def switch_case(opcao,calor):
    if opcao == 1:
        fahrenheit = calor *9/5 + 32
        print(f"Seu valor em Fahrenheit é de {fahrenheit}")
    elif opcao == 2:
        celsius = (calor - 32) *5/9
        print(f"Seu valor em Celsius é de {celsius}")
    else:
        print("Opção Inválida")

switch_case(opcao,calor)

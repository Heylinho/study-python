print("Operadores Aritméticos!")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print(f"Agora com {n1} e {n2}, selecione a forma de operação!")
op = int(input("[1 = + | 2 = - | 3 = * | 4 = /]: "))

def switch_case(op, n1, n2):
    if op == 1:
        resultado = n1 + n2
        print(f"Resultado da sua soma: {n1} + {n2} = {resultado}")
    elif op == 2:
        resultado = n1 - n2
        print(f"Resultado da sua subtração: {n1} - {n2} = {resultado}")
    elif op == 3:
        resultado = n1 * n2
        print(f"Resultado da sua multiplicação: {n1} * {n2} = {resultado}")
    elif op == 4:
        if n2 != 0:
            resultado = n1 / n2
            print(f"Resultado da sua divisão: {n1} / {n2} = {resultado}")
        else:
            print("Impossível dividir por 0")
    else:
        print("Escolha inválida")

switch_case(op, n1, n2)

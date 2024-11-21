import random

numero = random.randint(1, 100)

usuarioD = int(input('Digite um número: '))

while numero != usuarioD:
    if numero > usuarioD:
        print('Numero secreto é MAIOR')
    else:
        print('Numero secreto é MENOR')

    usuarioD = int(input('Digite um número: '))

print('Você ganhou!!!!')
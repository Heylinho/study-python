print('Calculador!') 

Digit = int(input('Digite um número: '))
soma = 0

while Digit != 0:
    soma= soma + Digit
    Digit = int(input('Digite um número: '))

print('Soma da sua conta é = {}'.format(soma))
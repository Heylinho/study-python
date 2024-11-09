velo = float(input("Por favor! Digite a velocidade final do seu carro: "))

if velo > 80:
    multa = velo - 80
    multa = multa * 15
    print("Você ultrapassou a velocidade máxima de 80km , cada KM a + é R$15,00 de multa!")
    print(f"Sua multa é de R${multa}")
    
else:
    print("Dentro do limite")

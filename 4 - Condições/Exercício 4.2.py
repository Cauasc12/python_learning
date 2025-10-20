velocidade = int(input("Digite a velociade do seu carro(Km/h): "))
if velocidade > 80: #velocidade máxima = 80
    print("O seu carro foi multado!")
    velocidade_ultrapassada = velocidade - 80
    valorM =  5 * (velocidade_ultrapassada)
    float(valorM)
    print(f"O valor da multa é de R${valorM:5.2f} por ultrapassar o limite em {velocidade_ultrapassada}Km/h")
else:
    print("Sua velocidade esta dentro do limite")
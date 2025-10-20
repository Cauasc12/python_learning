#Programa que calcule o preço a pagar por um carro alugado
preço_dia = float(input("Digite qual o preço por dia do carro: "))
preço_km = float(input("Digite qual o preço por quilômetro rodado com o carro: "))
km_percorrido = int(input("Digite a quantidade de quilômetros percorridos com o carro: "))
dias = int(input("Digite a quantidade de dias em que o carro foi alugado: "))
custo = km_percorrido * preço_km + dias * preço_dia
print(f"O custo total do alguem do carro foi de R${custo:5.2f}")
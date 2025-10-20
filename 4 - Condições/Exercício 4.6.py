#Programa que calcule o preço da passagem
distância = int(input("Digite a distância que deseja ser percorrida(Km): "))
if distância <= 200:
    passagem = 0.5
else:
    passagem = 0.45
custo = distância * passagem
print(f"O custo da passagem vai ser de R${custo:.2f}")

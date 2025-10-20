#Programa que calcule a multiplicação de 2 números usando somente adição
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
rep = n2 #Quantidade de vezes que o prmeiro número 1 vai ser somado
mult = 0
while rep > 0:
    mult += n1
    rep -= 1
print(f"{n1} x {n2} = {mult}")
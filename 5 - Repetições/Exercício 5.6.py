#Programa 6 + 7:calcule a tabuada de um numero escolhido 
tabuada = int(input("Digite o número que deseja saber a tabuada: "))
início = int(input("Digite de que número a tabuada deve começar a ser calculada: "))
fim = int(input("Digite em que número a tabuada deve terminaar de ser calculada: "))
x = início
while x <= fim:
    print(f"{tabuada} x {x} =", tabuada * x)
    x = x + 1
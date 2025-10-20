#Programa que liste em sequência os 10 primeiros múltiplos de 3
x = 3
qnt = 10
limite = x + 3 * qnt
while x <= limite:
    if x % 3 == 0:
        print(x)
    x += 1
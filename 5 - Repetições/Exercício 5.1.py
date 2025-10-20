#Programa que digite uma sequência de números
#Exercício 1 + 2 + 4
n = int(input("Digite o número inicial da sequência: "))
limite = int(input("Digite o número o último número da sequência: "))
#Todos os números
while n <= limite:
    print(n)
    n = n + 1
#Somente os pares
while n <= limite:
    if n % 2 == 0:
        print(n)
    n = n + 1
#Somente os ímpares
while n <= limite:
    if n %2 != 0:
        print(n)
    n = n + 1
#Escreva um programa que verifique se um número é palíndromo.

num = input("Infome o número a ser testado: ")
i = 0
f = len(num) - 1

while f > i and num[i] == num[f]:
    f -= 1
    i =+ 1
if num[i] == num[f]:
    print(f"{num} é um palíndromo!")
else:
    print(f"{num} não é um palíndromo!")
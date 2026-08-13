#Programa que ao ler um número n. Imprima os n primeiros números primos

qnt_de_primos = int(input("Digite a quantiades de primos a gerar: "))

print("2")
numero = 3
contador = 0

while contador < qnt_de_primos - 1:

    limite = int(numero ** (1/2))
    primos = 3

    while primos <= limite:
        if numero % primos == 0: #Não é primo
            break
        primos += 2
    else: #É primo
        print(numero)
        contador += 1
    numero += 2
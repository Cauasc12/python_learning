#Programa que ao digitar o número primo limite, imprime  todos os numeros primos até ele
final = int(input("Digite o número primo limite: "))

print("2")
numero = 3

while numero <= final:
    limite = int(numero ** (1/2))
    primos = 3

    while primos <= limite:
        if numero % primos == 0: #Não é primo
            break 
        primos += 2
    else: #É primo
        print(f"{numero}")
    numero += 2
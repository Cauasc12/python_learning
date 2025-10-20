numero = int(input("Digite o número a ser testado: "))

if numero <= 1:
    print(f"{numero} não é um número primo")
elif numero == 2:
    print(f"{numero} é um número primo!")
elif numero % 2 == 0:
    print(f"{numero} naõ é um número primo!")
else: 
    limite = int(numero ** (1/2))
    primos = 3

    while primos <= limite:
        if numero % primos == 0:
            print(f"{numero} não é um número primo!")
            break
        primos += 2
    else:
        print(f"{numero} é um número primo!")
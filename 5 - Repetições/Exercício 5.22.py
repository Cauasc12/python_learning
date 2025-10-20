#Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
#Imprima a tabuada da operação escolhida.
#Repita até que a opção saída seja escolhida

while True:
    operação = int(input("1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair\nEscolha a operação: "))
    if operação == 5:
        print("Você saiu da plataforma!!")
        break
    elif operação < 5 and operação >= 1:
        tabuada = int(input("Escolha o número da tabuada:"))
        numero = 1
        while numero <= 10:
            if operação == 1:
                print(f"{tabuada} + {numero} = {tabuada + numero}")
            elif operação == 2:
                print(f"{tabuada} - {numero} = {tabuada - numero}")
            elif operação == 3:
                print(f"{tabuada} x {numero} = {tabuada * numero}")
            elif operação == 4:
                print(f"{tabuada} % {numero} = {tabuada / numero}")
            numero += 1
    else:
        print("Operação inválida")
        
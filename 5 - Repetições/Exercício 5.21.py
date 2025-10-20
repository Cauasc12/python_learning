#Reescreva o Programa 5.1 de forma a continuar executando até que o valor digitado seja 0. Utilize repetições aninhadas

while True:
    valor = int(input("Digite o valor a pagar: "))    
    cedulas = 0
    atual = 50
    apagar = valor

    if valor == 0:
        print("O valor digitado foi nulo!")
        break
    else:
        while True:
            if atual <= apagar:
                apagar -= atual
                cedulas += 1
            else:
                print(f"{cedulas} cédula(s) de R${atual}")
                if apagar == 0:
                    break
                if atual == 50:
                    atual = 25
                elif atual == 25:
                    atual = 10
                elif atual == 10:
                    atual = 5
                elif atual == 5:
                    atual = 1
                cedulas = 0
                    
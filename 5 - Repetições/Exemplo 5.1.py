#Programa 5.1 - Contagem de cédulas
#Exercícios 5.16 - 5.20

valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100
apagar = valor

while True:
    if valor < 0.01:
        print("Não existem cédulas disponíveis parra essa quantia ou ela é nula")
        break
    if atual <= apagar: #Se o valor da cédula for menor que o valor a ser pago
        apagar -= atual #Diminui o valor de uma cédula do valor a pagar
        cedulas += 1 #Aumenta em 1 a quantidade de cédulas necessárias
    else: #Se o valor da cédula for maior que o valor a pagar, diminui o valor de cada cédula
        if atual >= 1:
            print(f"{cedulas} cédula(s) de R${atual}")
        else: 
            print(f"{cedulas} moedas de R${atual:.2f}")
        if apagar < 0.01:
            break
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.25
        elif atual == 0.25:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.01
        cedulas = 0

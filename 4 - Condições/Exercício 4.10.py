#Programa que leia 2 números e realize uma operação
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operação = input("1.Adição(+)\n2.Subtração(-)\n3.Multiplicação(*)\n4.Divisão(/)\nDigite a operação que deve ser feita: ")

if operação == "Adição" or operação == "adição" or operação == "+":
    resultado = n1 + n2
    operação = "adição"
elif operação == "Subtração" or operação == "subtração" or operação == "-":
    resultado = n1 - n2
    operação = "subtração"
elif operação == "Multiplicação" or operação == "multiplicação" or operação == "*":
    resultado = n1 * n2
    operação = "multiplicação"
elif operação == "Divisão" or operação == "divisão" or operação == "/":
    resultado = n1 / n2
    operação = "Divisão"
else:
    print("Operação inválida\nDigite um opção adequada!!")
    resultado = 0
print(f"O resultado da {operação} é {resultado}")
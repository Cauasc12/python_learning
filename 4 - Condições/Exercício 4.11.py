#Programa que aprove um empréstimo para a compra de uma casa
#Valor da prestação mensal não pode ser superior a 30% do salário
salário = float(input("Digite o seu salário: "))
casa = float(input("Digite o valor da casa desejada: "))
tempo = int(input("Digite em quantos anos o valor da casa será dividado"))
prestação = casa / (tempo * 12)
if prestação > salário * 0.3:
    print("Resultado da consulta:")
    print(f"Valor da prestação: R${prestação:.2f}")
    print("O Emprestimo não poderá ser oferecido")
    print("Motivo: A prestação mensal da casa ultrapassa 30% do salário do inquilino")
else:
    print("Resultado da consulta:")
    print(f"Valor da prestação: R${prestação:.2f}")
    print("O Emprestimo poderá ser oferecido")
    print("Motivo: A prestação mensal da casa não ultrapassa 30% do salário do inquilino")

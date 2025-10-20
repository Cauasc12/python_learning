#Programa que calcule o aumento de um salário
salário = float(input("Digite o salário inical: "))
aumento = float(input("Digite o aumento(%): "))
aumento_numérico = salário * (aumento / 100)
salário_final = salário + aumento_numérico
print(f"Com um aumento de R${aumento_numérico:5.2f} o salário final é de: R${salário_final:5.2f}")

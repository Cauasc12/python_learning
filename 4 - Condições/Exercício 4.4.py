#Programa que calcule o aumento de salário
salárioI = float(input("Digite o salário do funcionário: "))
pc_aumento = 0.15 #salários abaixo de 1250 recebem um aumento de 15%
if salárioI > 1250: 
    pc_aumento = 0.10
aumento = salárioI * pc_aumento
salárioF = salárioI + aumento
print(f"Salário inical: R${salárioI:.2f}")
print(f"Aumento: R${aumento:.2f}")
print(f"Salário atual: R${salárioF:.2f}")
#Programa 4.3: Cálculo de imposto de renda
salárioB = float(input("Digite seu salário para cálculo do impoosto de renda: "))
base = salárioB
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto +((base - 1000) * 0.2)
salárioL = salárioB - imposto
if base < 1000:
    imposto = 0
print(f"Salário bruto: R${salárioB:.2f}")
print(f"Imposto a pagar: R${imposto:.2f}")
print(f"Salario líquido: R${salárioL:.2f}")
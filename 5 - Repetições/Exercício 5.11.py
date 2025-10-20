#Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. 
#Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período
capital = float(input("Valor inicial depositado:"))
juros = float(input("Taxa de juros mensal (%):"))
mês = 1
tempo = 24
x = capital
while mês <= tempo:
    montante = x * (1 + (juros/100))
    x = montante
    mês += 1
    print(f"R${montante:.2f}")
receita = montante - capital
print(f"Depositando R${capital} a uma taxa de {juros}% ao longo de {tempo} meses, se obtem uma receita de R${receita:.2f}")
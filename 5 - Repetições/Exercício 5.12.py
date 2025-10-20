#Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
#Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.
capital = float(input("Valor inicial depositado:"))
juros = float(input("Taxa de juros mensal (%):"))
investimento = float(input("Depósito mensal: "))
mês = 1
tempo = 24
x = capital
while mês <= tempo:
    montante = x * (1 + (juros/100)) + investimento
    x = montante
    mês += 1
    print(f"R${montante:.2f}")
    
receita = montante - capital
print(f"Depositando R${capital} a uma taxa de {juros}% ao longo de {tempo} meses, se obtem uma receita de R${receita:.2f}")
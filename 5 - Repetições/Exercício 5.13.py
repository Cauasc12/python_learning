#Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. 
#Pergunte também o valor mensal que será pago. 
#Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.

dívida = float(input("Digite a dívida inicial: "))
juros = float(input("Digite o juros mensal: "))
pagamento = float(input("Digite o pagamento mensal: "))

tempo = 0
saldo = dívida
total = 0
if pagamento <= saldo * (juros / 100):
    print("A dívida não pode ser paga: pagamento mensal menor ou igual aos juros.")
else:
    while saldo > 0:
        #Aplica o juros
        saldo = saldo * (1 + juros/100)
        if saldo < pagamento: #o ultimo pagamento quita a divida (independente de ser mais q o necessário)
            total += saldo
            saldo = 0
        else:
            saldo -= pagamento
            total += pagamento
        tempo += 1 

juros_Pago = total - dívida

print("------RESUMO------")
print(f"Dívida inicial: R${dívida:.2f}")
print(f"Taxa de juros: {juros:.2f}%")
print(f"Juros pago: R${juros_Pago:.2f}")
print(f"Valor total pago: R${total:.2f}")
print(f"Tempo para abatimento: {tempo} meses")
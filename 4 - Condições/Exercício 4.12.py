#Programa que cálcule o preço a pagar pelo fornecimento de energia elétrica
energia = int(input("Digite a quantidade de energia(kWh) consumidas: "))
tipo = input("R = Residencial\nC = Comercial\nI = Industrial\nEscolha o tipo de instalação utilizada: ")
if tipo == "R" or tipo == "r": #Residencial
    if energia <= 500:
        preço = 0.40
    else:
        preço = 0.65
elif tipo == "C" or tipo == "c": #Comercial
    if energia <= 1000:
        preço = 0.55
    else:
        preço = 0.60
elif tipo == "I" or tipo == "i": #Industrial
    if energia <= 5000:
        preço = 0.55
    else:
        preço = 0.60
else:
    print("ERROR: Digite uma opção de instalação adequada!!")
custo = preço * energia
print(f"O custo de energia da instalação é de R${custo:.2f}")
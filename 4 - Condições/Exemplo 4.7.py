#Programa 4.7: Conta de telefone com 3 feixas de preço
#Abaixo dde 200 minutos = 0.2 por minuto
#Entre 200 e 400 minutos = 0.18 por minutos
#Acima de 400 minutos = 0.15 por mintos

minutos = int(input("Digite quantos minutos foram utilizados este mês: "))
if minutos < 200:
    custo = minutos * 0.2
else:
    if minutos < 400:
        custo = minutos * 0.18
    else:
        custo = minutos * 0.15
print(f"Você irá pagar R${custo:.2f}")
'''
if minutos < 200:
    custo = minutos * 0.2
elif minutos < 400:
    custo = minutos * 0.18
else:
    custo = minutos * 0.15
'''
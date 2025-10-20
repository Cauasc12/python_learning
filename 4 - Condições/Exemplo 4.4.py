#Programa 4.4: Cálculo de um plano de celular 
plano = input("Qual é se plano de celular? ") #Opções: falapouco e falamuito

if plano != "falamuito" and plano != "falapouco": #Plano inadequado
    print("Não temos esse plano disponível!")
else: #Plano adequadoo
    if plano == "falapouco":
        minutos_no_plano = 100
        extra = 0.20
        preço = 50
    else: #Plano "falamuito"
        minutos_no_plano = 500
        extra = 0.15
        preço = 99  

    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Você vai pagar:")
    print(f"Preço do Plano: R${preço:.2f}")
    suplemento = 0
    if minutos_consumidos > minutos_no_plano: #Exedeu o limite do plano
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
    print(f"Suplemento: R${suplemento:.2f}")
    print(f"Total = R$ {preço + suplemento:.2f}")
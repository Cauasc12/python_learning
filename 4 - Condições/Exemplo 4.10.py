#Programa 4.10: Programa 4.4 melhorado
plano = input("Qual é se plano de celular? ") #Opções: falapouco e falamuito
válido = True

if plano == "falapouco": #Plano adequadoo
    minutos_no_plano = 100
    extra = 0.20
    preço = 50
elif plano == "falamuito":
    minutos_no_plano = 500
    extra = 0.15
    preço = 99
else:
    válido = False
if not válido: #Deixa livre a adição de novos planos sem a mudança das linhas seguintes
    print(f"Erro: O plano {plano} não está disponível")
else:
    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Você vai pagar:")
    print(f"Preço do Plano: R${preço:.2f}")
    suplemento = 0
    if minutos_consumidos > minutos_no_plano: #Exedeu o limite do plano
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
    print(f"Suplemento: R${suplemento:.2f}")
    print(f"Total = R$ {preço + suplemento:.2f}")    
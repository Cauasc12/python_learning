#Programa que calcule o preço final de uma mercadoria com desconto
preço_inial = float(input("Digite o preço inial da mercadoria: "))
desconto = float(input("Digite o desconto dado(%): "))
desconto_numérico = preço_inial * (desconto/100)
preço_final = preço_inial - desconto_numérico
print(f"O valor final da mercadoria com un desconto de R${desconto_numérico:5.2f} será de: R${preço_final:5.2f}")
#Pograma 4.8: Categora x preço
categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
    preço = 10
elif categoria == 2:
    preço = 18
elif categoria == 3:
    preço = 23
elif categoria == 4:
    preço = 26
elif categoria == 5:
    preço = 31
else:
    preço = 0
    print("Categoria inválida\nDigite uma categoria de 1 a 5")
print(f"A categoria escolhida foi a {categoria} e o preço do produto é R${preço:.2f}")
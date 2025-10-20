#Programa que calcule a divisão de 2 números usando somente subtração
dividendo = int(input("Digite o dividendo da divisão: "))
divisor = int(input("Digite o dividor sa divisão: "))
resultado = 0
x = dividendo
if dividendo >= 0:
    while x >= divisor:
        x -= divisor
        resultado += 1
    resto = dividendo - divisor * resultado
else:
    while x < divisor:
        x += divisor
        resultado -= 1
    resto = dividendo + divisor * resultado
print(f"{dividendo} % {divisor} = {resultado}")
print(f"Resto = {resto}")

#resto + divisor * resultado = dividendo
#resto = dividendo - divisor * resultado - divisão positiva
#resto = dividendo + divisor * resultado 0-- divisão negativa
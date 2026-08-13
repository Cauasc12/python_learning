#programa que calcule o resto da divisão inteira entre dois números. 
#Utilize apenas as operações de soma e subtração para calcular o resultado
#Exercício 5.9

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
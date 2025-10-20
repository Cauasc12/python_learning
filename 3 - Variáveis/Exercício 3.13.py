#Conversor de Celsius em Fahrenheit
c = int(input("Digite a temperatura que deseja converter(°C): "))
f = int(9 * c / 5 + 32)
print(f"{c}°C é igual a {f}°F")
#Conversor de Fahrenheit em Celsius
f = int(input("Digite a temperatura que deseja converter(°F): "))
c = int(5/9 * (f - 32))
print(f"{f}°F é igual a {c}°C")
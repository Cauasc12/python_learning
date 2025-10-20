'''
Reescreva o código com if-elif-else:
if a < 10:
    print("a é menor que 10")
if a >= 10 and a < 20:
    print("a é maior ou igual a 10 e mrnor que 20)
if a >= 20:
    print("a é maior ou igual a 20)
'''
num = int(input("Digite um número: "))
if num < 10:
    print(f"{num} é menor que 10")
elif num <= 20:
    print(f"{num} está entre 10 e 20")
else:
    print(f"{num} é maior que 20")
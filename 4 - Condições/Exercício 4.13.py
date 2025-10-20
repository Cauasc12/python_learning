'''
Reescrever o código usando a inversão de condição:
if a > b:
    print("a é maior que b")
else:
    print("b é maior que a")
'''
n1 = float(input("Digie o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
if not n1 > n2:
    print(f"{n2} é maior que {n1}")
else:
    print(f"{n1} é maior que {n2}")
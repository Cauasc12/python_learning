#Escreva um programa para controlar uma pequena máquina registradora. 
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. 
#Seu programa deve exibir o total das compras depois que o usuário digitar 0.
#Qualquer outro código deve gerar a mensagem de erro “Código inválido”.

total = 0
qnt = 0
preco = 0

while True:
    c = int(input("Digite o código: "))
    if c == 0:
        break
    elif c == 1:
        preco = 0.5
    elif c == 2:
        preco = 1
    elif c == 3:
        preco = 4
    elif c == 5:
        preco = 7
    elif c == 9:
        preco = 8
    else:
        print("Código Inválido!!")
        continue  
    q = int(input("Qual a quantidade comprada: "))
    total += preco * q
    qnt += q

print(f"-----RESUMO-----")
print(f"Valor total: R${total:.2f}")
print(f"Quantidade de itens: {qnt}")
print("-----------------")
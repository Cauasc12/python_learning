#Escreva um programa que leia números inteiros do teclado.
#O programa deve ler os números até que o usuário digite 0 (zero). 
#No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

qnt = 0
soma = 0

while True:
    n = int(input("Digite um número inteiro para a soma ou 0 para sair: "))
    if n == 0:
        break
    else:
        qnt += 1
        soma += n

media = soma / qnt
print(f"-----RESUMO-----")
print(f"Soma dos números: {soma}")
print(f"Quantidade de números: {qnt}")
print(f"Média: {media:.2f}")
print("-----------------")
#Modificação de um programa que corrige um teste de múçtipla escolhha com 3 questões
aluno = input("Digite o nome do aluno: ")
pontos = 0
questão = 1
while questão <= 3:
    resposta = input(f"Respostas da questão {questão}: ")
    if questão == 1 and (resposta == "b" or resposta == "B"):
        pontos += 1
        quest1 = "Correta"
    elif questão == 1 and (resposta != "b" or resposta != "B"):
        quest1 = "Errada"
    if questão == 2 and (resposta == "a" or resposta == "A"):
        pontos += 1
        quest2 = "Correta"
    elif questão == 2 and (resposta != "a" or resposta != "A"):
        quest2 = "Errada"
    if questão == 3 and (resposta == "d" or resposta == "D"): 
        pontos += 1
        quest3 = "Correta"
    elif questão == 3 and (resposta != "d" or resposta != "D"):
        quest3 = "Errada"
    questão += 1
print(f"Resultado: \n Questão 1 = {quest1} \n Questão 2 = {quest2} \n Questão 3 = {quest3}")
print(f"{aluno} fez {pontos} ponto(s)")

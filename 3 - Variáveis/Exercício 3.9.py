#Programa que coverta dias, horas, minutos e segundos em somente segundos
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos_recebidos = int(input("Digite a quantidade de segundos: "))
segundos_dias = dias * 86400
segundos_horas = horas * 3600
segundos_minutos = minutos * 60
segundos_total = int(segundos_recebidos + segundos_minutos + segundos_horas + segundos_dias)
print(f"{segundos_total} segundos")
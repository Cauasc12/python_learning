#Programa que calcule o tempo de uma viagem 
velocidade = int(input("Digite a velocidade média do automóvel(Km/h): "))
distância = float(input("Digite a distância a ser percorrida(Km): "))
tempo = float(distância / velocidade)
print(f"O tempo esperado para percorrar {distância}km em {velocidade}km/h é de {tempo:.2f} horas")
tempo_s = tempo * 3600
horas = tempo_s // 3600
horas_restantes = tempo_s % 3600
minutos = horas_restantes // 60
segundos = horas_restantes % 60
print(f"O tempo esperado para percorrar {distância}km em {velocidade}km/h é de {horas}h {minutos}m e {segundos}s")
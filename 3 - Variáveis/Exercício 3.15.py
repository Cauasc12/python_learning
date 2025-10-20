#Pograma que calcule a redção do tempo de vida de um fumante
cigarros_dias = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Digite a quantos anos você fuma: "))
dias_fumando = anos_fumando * 365
cigarros_total = cigarros_dias * dias_fumando
segundos_perdidos = (cigarros_total * 10) * 60
dias_perdidos = segundos_perdidos // 86400
print(f"O fumante em questão perderá {dias_perdidos} dias de vida")

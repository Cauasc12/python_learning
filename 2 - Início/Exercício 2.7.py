#Cálculo de medio ponderada
notateste = 6
notatrabalho = 8
notaprova = 7
pesoteste = 20
pesotrabalho = 30
pesoprova = 50
divisão = pesoteste + pesotrabalho + pesoprova
print((notateste * pesoteste + notaprova * pesoprova + notatrabalho * pesotrabalho) / divisão)
totalteste = notateste * pesoteste
totalprova = notaprova * pesoprova
totaltrabalho = notatrabalho * pesotrabalho
print((totalteste + totalprova + totaltrabalho) / divisão)
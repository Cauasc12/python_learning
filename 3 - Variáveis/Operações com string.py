#CONCATENAÇÃO
s = "ABC"
print(s + "C")
print(s + "D" * 4)
print(s + "x4 = " + s * 4)

#Versão antiga de COMPOSIÇÃO
nome = "João"
idade = 22
grana = 51.34
print("%s tem %d anos e apenas R$%5.2f no bolso" % (nome, idade, grana))
print("%12s tem %3d anos e apenas R$%5.2f no bolso" % (nome, idade, grana))
print("%-12s tem %-3d anos e apenas R$%5.2f no bolso" % (nome, idade, grana))
#Versão moderna de COMPOOSIÇÃO(format)
nome = "João"
idade = 22
grana = 51.34
print("{} tem {} anos e apenas R${} no bolso".format(nome, idade, grana))
print("{:12} tem {:3} anos e R${:5.2f} no bolso".format(nome, idade, grana))
print("{:<12s} tem {:<3} anos e R${:5.2f} no bolso".format(nome, idade, grana))
#versão atual de COMPOSIÇÃO(f-string) FORMA UTILIZADA
nome = "João"
idade = 22
grana = 52.34
print(f"{nome} tem {idade} anos e R${grana} no bolso")
print(f"{nome:12} tem {idade:3} anos e R${grana:5.2f} no bolso")
print(f"{nome:<12s}tem {idade:<3} anos e R${grana:5.2f} no bolso")

#FATIAMENTO
s = "ABCDEFGHI"
print(s[:2])
print(s[:5])
print(s[2:4])
print(s[:8])
print(s[1:])
print(s[0:-2])
print(s[-5:7])
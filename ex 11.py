soma = 0
notas = list(range(10))
for i in range(10):
    nota = float(input("Digite a nota "+ str(i+1) +": "))
    notas[i] = nota
print ("Notas: ", notas)
for x in notas:
    soma += x
media = soma/len(notas)
print ("Média: ", media)

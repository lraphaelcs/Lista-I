n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
notas=[n1, n2]
media = sum(notas)/2
print("Média: ", media)
if media >=6 :
    print("Aprovado!")
else:
    print("Reprovado.")

x = int(input("Digite um número de 1 a 10: "))
if x > 10: 
    print("Número maior que 10!")
elif x < 1: 
    print("Número menor que 1!")
else: 
    for i in range (1, 11):
        print(x, " x ",i," = ", x*i)

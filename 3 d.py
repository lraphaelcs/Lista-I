from usuario import User 
x = 1
while x==1:   
    a = (input("Digite o nome do usuário: ")) 
    b = int(input("Digite a idade do usuário: ")) 
    u = User(a, b)
    u.save()
    x = int(input("Digite (1) se deseja adicionar mais um usuário ou outro número para finalizar: "))
print(User.all())

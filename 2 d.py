sentence = "Practice Problems to Drill List Comprehension in Your Head."
lista = list(sentence)
[lista.remove(i) for i in lista if i == "a"]
[lista.remove(i) for i in lista if i == "e"]
[lista.remove(i) for i in lista if i == "i"]
[lista.remove(i) for i in lista if i == "o"]
[lista.remove(i) for i in lista if i == "u"]
print(lista)

sentence = "Practice Problems to Drill List Comprehension in Your Head."
sentence = sentence.split()
sentence = [i.replace(".", "") for i in sentence]
[print(i) for i in sentence if len(i)<5]

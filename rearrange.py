import random

text = input("Insert Sentence: ")
# text = "How now brown cow"
text = text = text.split(' ')
printText = random.shuffle(text)
text = ' '.join(text)
print(text)

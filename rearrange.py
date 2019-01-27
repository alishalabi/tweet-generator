import random

text = input("Insert Sentence: ")
# text = "How now brown cow"
# TODO: Find better naming convension
text = text.split(' ')
# TODO: Understand what is going on with random.shuffle ()
random.shuffle(text)
text = ' '.join(text)
print(text)

import random

text = input("Insert Sentence: ")
text = text.split(' ')
# TODO: Understand what is going on with random.shuffle ()
random.shuffle(text)
text = ' '.join(text)
print(text)

import sys
import random

# Step 1: Read words file
# Note: Kind of fuzzy on this, used Nicolai's sample to get un-stuck
f = open("/usr/share/dict/words", 'r')
content = f.read().split()
f.close()

# Sample dictionary to work with
sample_dict = ['Apple', 'Blue', 'Clue',
               'Dear', 'Eegg', 'Fall', 'Great', 'Hello']

# Step 2: Select a random set of words, based on Int input
word_count = int(input("Enter number of words: "))
# word_count = 2
selected_words = []
for i in range(word_count):
    # word_index = random.randint(0, len(sample_dict) - 1)
    word_index = random.randint(0, len(content) - 1)
    selection = content[word_index]
    content.remove(selection)
    selected_words.append(selection)


# Step 3: Put words together into a sentence
# TODO: Figure out if we need the following code:
# random.shuffle(text)

finished_sentence = ' '.join(selected_words)

# Step 4: Output sentence
print(finished_sentence)

# Test section
# print(word_count)
# print(selection)
# print(selected_words)
# print(finished_sentence)

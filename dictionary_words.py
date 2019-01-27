import sys
import random

# Step 1: Read words file

# Sample dictionary to work with
sample_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Step 2: Select a random set of words, based on Int input
word_count = int(input("Enter number of words: "))
# word_count = 2
selected_words = []
for i in range(word_count):
    word_index = random.randint(0, len(sample_dict) - 1)
    selection = sample_dict[word_index]
    sample_dict.remove(selection)
    selected_words += selection


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

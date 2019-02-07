''' This is the file for challenge 3.2 - stochastic
sampling using lists of lists'''

old_text = "one Fish two fish red Fish blue fish"

# Convert sample to array (more readable)
text = old_text.split(' ')

histogram = []

# Inspire by Jackson Ho


def update_histogram(word):
    word = word.lower()
    word_found = False
    for word in histogram:
        if word == histogram[0]:
            word_found = True
            word[1] += 1
            break
    if not word_found:
        histogram.append([word, 1])


def create_histogram():
    for item in text:
        update_histogram(item)


create_histogram()
print(text)
print(histogram)

old_text = "one Fish two fish red Fish blue fish"

# Convert sample to array (more readable)
text = old_text.split(' ')

histogram = {}


def update_histogram(word):
    word = word.lower()
    word_found = False
    for key in histogram.keys():
        if key == word:
            word_found = True
            histogram[key] += 1
    if word_found == False:
        histogram.update({word: 1})


def create_histogram():
    for item in text:
        update_histogram(item)


create_histogram()

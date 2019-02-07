import random

old_text = "one Fish two fish red Fish blue fish"

# Convert sample to array (more readable)
text = old_text.split(' ')

histogram = {}


def update_histogram(word):
    ''' Marianna: I recommend writing a doc string to explain complex functions.  '''
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


def sample():
    ''' Marianna: I recommend writing a doc string to explain complex functions.  '''
    create_histogram()
    total_words = 0
    total_prob = 0
    for count in histogram.keys():
        total_words += histogram[count]
    random_num = random.uniform(0, 1)
    for key in histogram.keys():
        word_prob = histogram[key] / total_words
        total_prob += word_prob
        if total_prob >= random_num:
            selected_word = key
            return selected_word
            break


def word_frequency(histo):
    count_dictionary = dict()
    sample_size = 10000
    # sample()

    # Populate dictionary count
    for item in histo.keys():
        # print(item)
        # count_dictionary.update({item: 0})
        # histo[item] = 0
        count_dictionary[item] = 0

    # Run multiple times (many)
    for i in range(sample_size):
        selected_word = sample()
        count_dictionary[selected_word] += 1

    print(count_dictionary)


# sample()
create_histogram()
word_frequency(histogram)

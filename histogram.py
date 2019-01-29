old_sample = "one fish two fish red fish blue fish"
sample = old_sample.split(' ')

histogram = {}


def find_and_update_dictionary(word):
    word_found = False
    for key in histogram.keys():
        if key == word:
            word_found = True
            histogram[key] += 1
    if word_found == False:
        histogram.update({word: 1})


def read_sample():
    for item in sample:
        find_and_update_dictionary(item)
    print(histogram)

# def create_histogram(text):
#     return text


read_sample()

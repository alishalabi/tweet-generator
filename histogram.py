old_sample = "one fish two fish red fish blue fish"
sample = old_sample.split(' ')

histogram = {}


def update_historgram(word):
    word_found = False
    for key in histogram.keys():
        if key == word:
            word_found = True
            histogram[key] += 1
    if word_found == False:
        histogram.update({word: 1})


def create_histogram():
    for item in sample:
        update_historgram(item)
    print(histogram)


create_histogram()

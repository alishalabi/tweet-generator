sample_histogram = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}


def frequency(word, histogram):
    word_count = 0
    for key in histogram.keys():
        if key == word:
            word_count = histogram[key]
    print("Word count for '" + str(word) + "': " + str(word_count))


frequency("fish", sample_histogram)

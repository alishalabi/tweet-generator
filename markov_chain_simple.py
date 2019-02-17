old_text = "one fish two fish red fish blue fish"

# Convert sample to array (more readable)
text = old_text.split(' ')
text.append("STOP")

histogram = {}


def update_histogram(word):
    word = word.lower()
    word_found = False
    for key in histogram.keys():
        if key == word:
            break
    if word_found == False:
        histogram.update({word: {}})


def init_histogram():
    for item in text:
        item = item.lower()
        update_histogram(item)


def update_chain():
    count = 0
    for item in text:
        if item != "STOP":
            position = count
            count += 1
            next_word = text[(int(position) + 1)]
        print(str(item) + str(position) + str(next_word))


init_histogram()
print(histogram)

update_chain()

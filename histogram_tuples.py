old_text = "one Fish two fish red Fish blue fish"

# Convert sample to array (more readable)
text = old_text.split(' ')

# Inspired by Jackson Ho
# def update_histogram(word):
#     word = word.lower()
#     word_found = False
#     for key in histogram.keys():
#         if key == word:
#             word_found = True
#             histogram[key] += 1
#     if word_found == False:
#         histogram.update({word: 1})
#
#
# def create_histogram():
#     for item in text:
#         update_histogram(item)
#
#
# create_histogram()
# print(histogram)


def create_histogram(text_file):
    tuple_list = list()
    for word in text_file:
        found = False
        for index, value in enumerate(tuple_list):
            if value[0] == word:
                found = True
                num = value[1] + 1
                del tuple_list[index]
                tuple_list.append((word, num))
                break
        if not found:
            tuple_list.append((word, 1))
    print(tuple_list)


create_histogram(text)

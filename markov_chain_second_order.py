from pprint import pprint
from dictogram import Dictogram
import random

old_text = "how much wood would a woodchuck if a woodchuck could and would chuck wood"

# Convert sample to array (more readable)
text = old_text.split(' ')
# text.append("*STOP*")

# markov_chain = {}
#
#
# def update_histogram(word):
#     word = word.lower()
#     word_found = False
#     for key in markov_chain.keys():
#         if key == word:
#             break
#     if word_found == False:
#         # markov_chain.update({word: Dictogram()})
#         markov_chain[word] = Dictogram()
#
#
# def init_histogram():
#     for item in text:
#         item = item.lower()
#         update_histogram(item)
#
#
# def update_chain():
#     count = 0  # Adding count for relative position (more reliable than index)
#     for item in text:
#         if item != "*STOP*":  # Checking for hard stop token
#
#             position = count  # Using relative position
#             count += 1
#             # Getting next word for each item
#             next_word = text[(int(position) + 1)]
#             print(item + ' -> ' + next_word)
#             # TODO: Update Markov dictionary
#             # for key in markov_chain[item].keys():
#             #     if key != "*STOP*":
#             markov_chain[item].add_count(next_word)
#             # word_found = False
#             # if key == next_word:
#             #     word_found = True
#             #     histogram[item][key] += 1
#             # if word_found == False:
#             #     markov_chain[item].add_count({next_word: 1})
#     pprint(markov_chain)
#
#
# init_histogram()
#
# update_chain()


# Refactored method :D
def create_markov_chain(word_list):
    """Create and return a new Markov chain using the given list of words."""
    markov = {}
    for index in range(len(word_list) - 1):
        key_1 = word_list[index]
        key_2 = word_list[index + 1]
        next_word = word_list[index + 1]
        word_group = (key_1, key_2)
        # print(word + ' -> ' + next_word)
        if word_group != "*STOP*":
            if word_group in markov:
                markov[word_group].add_count(next_word)
            else:
                markov[word_group] = Dictogram({next_word: 1})
    # pprint(markov)
    return markov


# Got unstuck through Rinni Swift's code sample https://github.com/RinniSwift/Tweet-Generator/blob/master/markov.py
def generate_new_sentence(markov_chain):
    num_words = 1
    current_word_group = random.choice(list(markov_chain.keys()))
    sentence = [current_word_group[0]]
    # print(sentence)

    # print(current_word_group)
    #
    while num_words < 9:
        # if (current_word) == "*STOP*":
            #     break

        sentence.append(current_word_group[1])
        next_word_dictionary = markov_chain[current_word_group]

        # Case: There is only a single value at a markov chain's key
        if len(next_word_dictionary) == 1:
            current_word_group = (current_word_group[1], list(
                next_word_dictionary.keys())[0])
            # break

        # Case: There are multiple values at a markov chain's key
        elif len(next_word_dictionary) > 1:
            chance = 0
            random_num = random.random()
            for key, value in next_word_dictionary.items():
                chance += (value / len(next_word_dictionary))
                if chance >= random_num:
                    new_word_group = current_word_group
                    break
            current_word_group = new_word_group

        num_words += 1

    sentence = " ".join(sentence)
    print(sentence)


test_chain = (create_markov_chain(text))
# print(test_chain)
generate_new_sentence(test_chain)

from pprint import pprint
from dictogram import Dictogram

old_text = "one fish two fish red fish blue fish"

# Convert sample to array (more readable)
text = old_text.split(' ')
text.append("*STOP*")

markov_chain = {}


def update_histogram(word):
    word = word.lower()
    word_found = False
    for key in markov_chain.keys():
        if key == word:
            break
    if word_found == False:
        # markov_chain.update({word: Dictogram()})
        markov_chain[word] = Dictogram()


def init_histogram():
    for item in text:
        item = item.lower()
        update_histogram(item)


def update_chain():
    count = 0  # Adding count for relative position (more reliable than index)
    for item in text:
        if item != "*STOP*":  # Checking for hard stop token

            position = count  # Using relative position
            count += 1
            # Getting next word for each item
            next_word = text[(int(position) + 1)]
            print(item + ' -> ' + next_word)
            # TODO: Update Markov dictionary
            # for key in markov_chain[item].keys():
            #     if key != "*STOP*":
            markov_chain[item].add_count(next_word)
            # word_found = False
            # if key == next_word:
            #     word_found = True
            #     histogram[item][key] += 1
            # if word_found == False:
            #     markov_chain[item].add_count({next_word: 1})
    pprint(markov_chain)


init_histogram()

update_chain()


def create_markov_chain(word_list):
    """Create and return a new Markov chain using the given list of words."""
    markov = {}
    for index in range(len(word_list) - 1):
        word = word_list[index]
        next_word = word_list[index + 1]
        print(word + ' -> ' + next_word)
        if word in markov:
            ...
        else:
            ...
    return markov

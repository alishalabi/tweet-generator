from create_histogram import create_histogram
from create_histogram import update_histogram
import random

old_text = "one Fish two fish red Fish blue fish"

# Convert sample to array (more readable)
text = old_text.split(' ')

histogram = {}


def sample(histogram):
    create_histogram()
    print(histogram)
    sample_key = random.randint(0, len(histogram) - 1)
    sample_word = histogram[sample_key]
    print(sample_word)
    print(sample_key)


sample(text)

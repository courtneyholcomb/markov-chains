"""Generate Markov text from text files."""

import random #import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read().replace("\n", " ")


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # split into list
    words = text_string.split(" ")

    # loop through range of list length
    for i in range(len(words) - 2):
        # create tuple for list[i] and list[i+1] as dict key
        bi_gram = (words[i], words[i + 1])
        # chains[tuple] = chains.get(chains[tuple] + next_word, next_word)
        chains[bi_gram] = chains.get(bi_gram, []) + [words[i + 2]]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    # while loop:
    while True:
        # if words == []
        # choose random key tuple from chains & add key[0] & key[1] to words list
        if words == []:
            current_key = random.choice(list(chains))
            words.extend([current_key[0], current_key[1]])

        current_key = (words[-2], words[-1])
        chosen_word = random.choice(chains[current_key])
        words.append(chosen_word)

    
    # for latest two words in list (current_key),
    # pick random word from chains[(word1, word2)] (chosen_word)
    # add that word to words list


    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

# print(chains)

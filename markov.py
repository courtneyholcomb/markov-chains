"""Generate Markov text from text files."""

from random import choice
import sys
from string import punctuation


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as file:
        return file.read()
    # text2 = open(file_path2).read().replace("\n", " ").replace("  ", " ").rstrip()


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.
    """

    chains = {}

    # split into list
    words = text_string.split()

    # loop through range of list length
    for i in range(len(words) - n):
        # create tuple for list[i] and list[i+1] as dict key
        n_gram = tuple(words[i:i + n])
        # chains[tuple] = chains.get(chains[tuple] + next_word, next_word)
        chains[n_gram] = chains.get(n_gram, []) + [words[i + n]]

    return chains


def compare_two_sources(source1, source2):
    # loop thru source1, check if keys match any keys in source2
    for key in source1:
        # if match, add source1[key] to source2[key]
        # if no match, create key and add value
        source2[key] = source2.get(key, []) + source1[key]

    return source2
    

def make_text(chains):
    """Return text from chains."""

    words = []

    # while loop:
    while True:
        # if words == []
        # choose random key tuple from chains & add n keys to words list
        if words == []:  # exercise! find another way to check empty list
            # create list of keys where key[0][0] isupper() == True
            capital_keys = [key for key in chains if key[0][0].isupper()]

            current_key = choice(capital_keys)

            n = len(current_key)
            words.extend(current_key[:n])

        # for last n words in list (current_key)
        current_key = tuple(words[-n:])

        # try, except KeyError: break
        try:
            # pick random word from chains[(word1, word2)] (chosen_word)
            chosen_word = choice(chains[current_key])
            # add that word to words list
            words.append(chosen_word)
            # print(chosen_word)

        except KeyError:
            break

    strung_words = " ".join(words)

    # remove anything after last punctuation
    if strung_words[-1] not in punctuation:

        for i in range(len(strung_words)):

            if strung_words[-i] in punctuation:
                strung_words = strung_words[:-i + 1]
                break

    return strung_words


chain1 = make_chains(open_and_read_file(sys.argv[1]), int(sys.argv[3]))
chain2 = make_chains(open_and_read_file(sys.argv[2]), int(sys.argv[3]))

sources_combined = compare_two_sources(chain1, chain2)

generate_text = make_text(sources_combined)

print(generate_text)

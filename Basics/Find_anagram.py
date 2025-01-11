# Author: Siddardha Chelluri
# Github: SidCh1

# ===================================================================================================

# Problem:

# Write a function find_anagrams(word, word_list) that
# takes a string word and a list of strings word_list.
# The function should return a list of all anagrams of word from the word_list.

# ===================================================================================================

# Solution:


def find_anagrams(word, word_list):

    # Sort the characters of the input word
    sorted_word = sorted(word)
    print(sorted_word)

    # Find words in the list that match the sorted characters of the input word
    anagrams = []
    for w in word_list:
        if sorted(w) == sorted_word:
            anagrams.append(w)

    return anagrams


# Example usage
word = "listen"
word_list = ["enlist", "google", "inlets", "banana", "silent"]

result = find_anagrams(word, word_list)
print(result)

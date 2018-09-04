"""
CP1404/CP5632 Practical - Suggested Solution
Count word occurrences in a string
"""

unique_words = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = unique_words.get(word, 0)
    unique_words[word] = frequency + 1

# Print the unique words and their frequencies,
# in alphabetical order
words = list(unique_words.keys())
words.sort()
# use the max function to find the maximum of the values produced by the
# generator function (like a list comprehension) of lengths of words
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, unique_words[word]))

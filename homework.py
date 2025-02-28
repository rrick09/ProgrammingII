

# HW

# Homework

import requests

link = "https://www.gutenberg.org/cache/epub/132/pg132.txt"

result = requests.get(link)
# print(result.text)
unique_words = {}
punctuation = ",.'!?-=()"
for line in result.text.splitlines():
    for p in punctuation:
        line = line.replace(p, "")
    words = line.split()
    for word in words:
        unique_words[word] = unique_words.get(word, 0) + 1

print("Number of unique words in The art of war:", len(unique_words))

link = "https://www.gutenberg.org/cache/epub/1232/pg1232.txt"

result = requests.get(link)
# print(result.text)
unique_words = {}
punctuation = ",.'!?-=()"
for line in result.text.splitlines():
    for p in punctuation:
        line = line.replace(p, "")
    words = line.split()
    for word in words:
        unique_words[word] = unique_words.get(word, 0) + 1

print("Number of unique words in The prince:", len(unique_words))

print(" 'The art of war' has more unique words than 'The prince'")

# print(unique_words)
# print(unique_words["man"])
# print(unique_words["the"])

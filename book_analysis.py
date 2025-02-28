import requests

link = "https://www.gutenberg.org/cache/epub/84/pg84.txt"

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

freq = list(unique_words.values())
freq = sorted(freq, reverse=True)
freq = freq[:10]
print(freq)
for f in freq:
    for key, value in unique_words.items():
        if value == f:
            print(key)

# print(unique_words)
# print(unique_words["man"])
# print(unique_words["the"])
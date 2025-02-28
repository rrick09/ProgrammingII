# find_words_in_file

def find_words(filename):
    """
    prints the 3 letter words starting with b
    :param filename: the name of the file
    :return: Nothing
    """
    with open(filename, 'r') as f:
        for line in f:
            # need to break down the line into words
            words = line.split()  # by default splits by space
            # check each word
            for word in words:
                if len(word) == 3 and word.upper()[0] == "B":
                    print(word)


find_words("input.txt")


# Multiple_of_6

def get_multiple_6():
    """
    resturns a multiple of 6 that was entered by the user.
    :return: int a number
    """
    while True:
        try:
            n = input("Please give me a multiple of 6:")
            n = int(n)
            if n % 6 == 0:
                return n
            if n / 6 == n // 6:
                return n
            else:
                print("that is not a multiple of 6")
        except ValueError:
            print("you have not entered a number")


get_multiple_6()

# Dictionary_example

d = {}  # empty dictionary
eng_to_spa = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_to_spa)
eng_to_spa["i"] = "yo"
eng_to_spa["am"] = "soy"
eng_to_spa["spanish"] = "espanol"
print(eng_to_spa)
sentence = "i am spanish"
words = sentence.split()
for word in words:
    print(eng_to_spa[word])
eng_to_spa.update({"yes": "si", "no": "no"})  # updated dict
print(eng_to_spa)
del eng_to_spa["no"]  # that is how you remove a key/ value from dict
print(eng_to_spa)

# print(eng_to_spa.popitem()) # not very useful since its hard to know which is the last one
print(eng_to_spa.pop("two"))

if "tree" in eng_to_spa:
    print(eng_to_spa["tree"])
else:
    print("i dont know that word")

print(eng_to_spa.get("tree", "unknown word"))

for key in eng_to_spa:
    print(f"{eng_to_spa[key]} means {key}")
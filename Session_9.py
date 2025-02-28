# Session 9

# file_example
fp = open("text.txt", "r")  # r is by default, so no really needed
print(fp.read())  # prints the entire content of the file
fp.close()  # good practice to close the file

# same exact thing with content manager
with open("text.txt", "r") as fp:
    print(fp.read())

# lets read from the same file, line by line
print("Read the file line by line")
line_number = 1
with open("text.txt", "r") as fp:
    for line in fp:  # we iterate over the file, line by line
        print(f"{line_number}:{line}", end="")  # ask print not to add a new line
        # print(line.rstring())
        Line_number += 1

print("done printing")
print("done with the code")

# file_example_write

# lets create a virtual diary
with open("diary.txt", "a") as fp:
    text = input("How do you feel today? (type q to quit): ")
    while True:
        text = input("How do you feel today? (type q to quit): ")
        if text == "q":
            break
            fp.write(f"{text}\n")  # this is the same
        # fp.write(text + "\n")

# sum_10_random

import random

sum = 0
for i in range(10):
    sum += random.randint(1, 100)

print(sum)


# Function_examples

def greet():
    """
    Simple function that just prints hello
    :return: None
    """
    print("Hello!")

    def greet2(name):
        """
        Simple function that greets a person
        :param name: The name of a person
        :return: None
        """
        print(f"Hello, {name}")

    greet2("Jane")
    greet("Mary")


def special_op(a, b):
    """
    Special op is 10xa+b
    :param a: first number
    :param b: second number
    :return: value, 10a+b
    """
    result = 10 * a + b


print(special_op(10, 2))
print(special_op(2, 10))
result = special_op(8, 9)
print(f"the special op for 8 and 9 is: {result}")
print(special_op(b=8, a=9))
print(special_op())
print(special_op(a=9))


def bond_greet(name):
    print(f"The name is: {name}")


def bondise_name(first_name, last_name):
    return f"{last_name}, {first_name}, {last_name}"


print(bondise_name("John", "Doe"))
bond_greet(bondise_name(first_name="John", last_name="Doe"))
bond_greet(bondise_name())

# diary.txt

# text.txt
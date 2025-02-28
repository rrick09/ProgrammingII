# for_example

# sum the fisrt 10 numbers
sum = 0
for num in range(1, 101):  # the last one is excluded, so it goes from 1 to 100
    sum = sum + num
print(sum)

# rewrite using while loop ^
sum = 0
num = 0

while num < 100:  # Goes from 1 to 100
    num = num + 1
    sum += num  # same thing as sum = sum + num
print(sum)

# print multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # to separate woth a new line between blocks

i = 20
print("i i i")
print(f"{i} {21 + i} i i ")

# simple_string_example

s1 = "banana"
s2 = 'banana'
print(s1, s2)
s1 = 'And John said: "How are you". The person replied: "I\'m smart"'
print(s1)
s1 = "I can print \" and another\""
print(s1)

# including, starts from 0
s = "0123456789"
print(s[1], s[7], s[9])
print(s[-1], s[-4])
print(f"the lenght is: {len(s)}")

# string_operation

s1 = "hello"
s2 = "world"
print(s1 + " " + s2)

s1 = "hello"
s2 = 4 * s1  # you can only multiply by positive intenger !!
print(s2)
print((4 // 2) * s1)  # 4/2 is not input

# string_slices

s = "0123456789"
print(s)
print(s[1:2])  # first index is include, last index is excludes
print(s[4:7])
print(s[:7])  # if yout omit the fist index, it starts from beginning
s = "I go to school early in the morning"
print(s[:20])
print(s[20:])  # all the way to the end
print(s[:])  # the whole thing
print(s[::2])  # this means steps of 2 (every second character)
print(s[::-1])
print("racecar"[::-1])
s = "Was it a car ir a cat I saw?"
print(s[::-1])

# string_methods

s = "hello"
print(dir(s))
useful_methods = [m for m in dir(s) if "__" not in m]
print(useful_methods)

print(help(s.capitalize))
print(s.capitalize())

print("HELLO".casefold())

print("hello".center(50))
print("hello".center(50, "*"))

print("I see a little dove".count("e"))
print("banananananannananananana".count("ana"))
x = "I do not cok nor compare"

s = "Bob goes home to meet so they can take their bob and go bobing"
pos = 0
while True:
    start = s.find("bob", pos)
    if start == -1:
        break
    print("found bob on position", start)
    pos = start + 1

item = ["cat", "rat", "mouse", "house"]
print(" ".join(item))

print("I LIKE to go KiKING!!".lower().upper())

print("i love to go skiing".title())

# replace items inside the string
print("i love to go skiing".replace(" ", "$"))

# split, makes a list of the string by the delimiter
print("i like to go skiing".split())

# while_examples

# you have 3 lives, you roll a dice, if you get a 6 you win
# if you do not get a 6, you lose 1 life
from random import randint

lives = 10
while lives > 0:  # as long as i have more lives
    # roll the dice
    dice = randint(1, 6)
    if dice == 6:
        print("You rolled 6! You win!")
        break
    lives = lives - 1
    print("You rolled a", dice, "you have", lives, "left")

if lives == 0:
    print("You lose!")
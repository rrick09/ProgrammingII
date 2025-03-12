# Session 5 and 6

# exceptions_examples

name = input("What is your name")
print("Hello", name)
age = input("How old are you?")
try:
    age = int(age)  # i am tryng to covert it to number,specify the value as an integer to avoid errors
    # new_age = age / 0
except ValueError:
    print("you are trying to trick me")
    print("better luck next time")
except ZeroDivisionError:
    print("You cant divide by zero")
except:
    print("something unexpected happened")
else:  # this happens if no error occurs
    print("you were probably born in", 2024 - age)
finally:
    print("Thanks for playing")

#for examples
# sum the first 10 numbers
sum = 0
for num in range(1, 11): # 11 is excluded, so it goes from 1 to 10
    sum = sum + num
    print(sum)

# rewrite it using while loop
sum = 0
num = 0
while sum < 100:
    num = num + 1
    sum += num
print(sum)

# print multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} X {j} = {i*j}")
    print() # to separate with a new line between blocks

i = 20
print("i i i ")
print(f"{i} {21+i} i i ")

# if_examples

a = 90
b = 20
if a > b:
    print(a, "is greater tha", b)
elif a == b:
    print(a, "is equal to", b)
else:
    print(a, "is less than", b)

#while examples
# you have 3 lives, you roll a dice, if you get a 6 you win
# if you do not get a 6, you lose 1 life
from random import randint

lives = 3
while lives > 0: # as long as a I have more lives
    # roll the dice
    dice = randint(1,6)
    if dice == 6:
        print("You rolled a 6, you win")
        break
    lives = lives - 1
    print("you rolled a", dice, "you have", lives, "left")
if lives == 0:
    print("you lose")




















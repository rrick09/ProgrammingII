# Session 5

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

# if_examples

a = 90
b = 20
if a > b:
    print(a, "is greater tha", b)
elif a == b:
    print(a, "is equal to", b)
else:
    print(a, "is less than", b)

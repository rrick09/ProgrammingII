 #virtual_bartender

from random import choice

drinks = ("gin", "vodka", "whiskey", "rum", "tequila", "absinthe", "sake")
# print(choice(drinks))
level_of_degeneration = ("1", "2", "3", "4", "5")
# print(choice(level_of_degeneration))
name = input("Hey I am the virtual bartender. Whats your name? ")
try:
    age = input("You look a bit too young to drink, how old are you?")
    age = int(age)
    country = input("You dont look from here, where are you from? ")
    legal = False
    if age >= 21:
        legal = True
    elif age > 18 and (country != "USA" or country != "UAE"):
        legal = True
    elif age > 16 and country == "Luxembourg":
        legal = True
except ValueError:
    print("Dont play games with me")
else:
    if legal:
        print("Great, im serving", choice(drinks), "tonight",
              "also from one to five of the degeneration levels this night its feeling like a",
              choice(level_of_degeneration))
    else:
        print("Go away lil boy dont let me call the cops on you")

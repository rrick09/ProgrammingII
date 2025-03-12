# methods examples
s = "hello"
print(dir(s))
useful_methods = [m for m in dir(s) if "__" not in m]
print(useful_methods)
print(help(s.capitalize))
print(s.capitalize())

print("HELLO".casefold()) # same as lower() method
print("HELLO".center(50))
print("HELLO".center(50, "*"))

print("I see a little dove".count("e")) # how many times do I see 'e'
print("anananananananannanananannananananananananananananan".count("ana"))
x = "I do not cook nor compare"
print(f"There are {x.count("o")}os inside: '{x}'")
print("hellooooooooooooolloo".find("l", 10))

s= "bob goes home to meet bob so they can take their bob and go bobing"
pos = 0
while True:
    start = s.find("bob", pos)
    if start == -1:
        break
    print("found bob on position", start)
    pos = start + 1

    items = ["cat", "rat", "mouse", "house"]
print(" ".join(items))

print("I LIKE to go HIKING".lower().upper())
print("I like to go skiing".title())

# replace, replaces item inside the string
print("I like to go skiing".replace(" ", "***"))

# split makes a list of the string split by the delimiter
print("i like to go skiing".split())

# simple str
s1 = "banana"
s2 = 'banana'
print(s1, s2)

s1= 'And John said: "How are you". The person replied: "Who is talking?" '
print(s1)

s1= 'And John said: "How are you". The person replied: "I\'m smart?" '
print(s1)

#indexing, starts from 0
s = "0123456789"
print(s[1], s[7], s[9])
print(s[-1], s[-4])
print(len(s))
print(f"the length is: {len(s)}")

# str operations
s1 = "hello"
s2 = "world"
print(s1 + " " + s2)
print(s1)
print("hello")
s1 = "hello"
s2 = 4*s1 # you can only multiply by positive integer!!
print(s2)
print((4//2)*s1) # integer division, result will always be an integer, so you use //

# str slices

s = "0123456789"
print(s)
print(s[1:2]) # first index is included, second index is excluded
print(s[4:7])
print(s[:7]) # if you want to omit the first index, it starts from beginning

s = "I go to school early in the morning"
print(s[:20])
print(s[20:]) # includes all the way to the end

print(s[:]) # the whole thing
print(s[::2]) # this means stop of 2 (every second character)
print(s[::-1])
print("racecar"[::-1])

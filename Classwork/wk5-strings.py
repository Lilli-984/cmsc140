esc_double = "This is \"fine\" now."
esc_single = 'This string\'s formatting is okay.'

rawstring = r'This will print \' exactly as I say \"\"'

print (rawstring)

trip_quotes = """This is a string
that can span multiple lines.
Cool!"""
print(trip_quotes)

name = "Acacia Lee Ackles"
print(name[0])
print(name[0:6])
print(name)

firstname = name[0:6]

#Unlike list, you can’t change a part of a string by 
# assigning a new character to it.

print(firstname in name)
#True
print("Hello" in "Hello")
#True
print("j" in "fox")
#False

splitname = name.split()
print(splitname)


# similar to how you could do for key, value in dict.items()
first, middle, last = name.split()
print(first)
print(middle)
print(last)

newname = name.split('a')
print(newname)
# whatever you split on gets deleted from the split string; 
# it’s used as a delimiter.

my_list = ["hello", "python", "class"]
nospace = "".join(my_list)
space = " ".join(my_list)
print(nospace)
print(space)

fruit = "apples"
num = 7
print("I have " + str(num) + " " + fruit + ".")
print("I have %s %s" % (num, fruit))

newname = name.upper()
print(newname)
newname = name.lower()
print(newname)

if newname.isupper():
    print("We are shouting!".upper())
else:
    print("we are whispering")

space_string = "      Hello!  "
print(space_string.lstrip())
print(space_string.rstrip())
print(space_string.strip())

cool_string = "ooooo Hello this is my string ooooooo"
print(cool_string.strip('o'))
this_string = "Today is cold"

def alt_case(string):
    new_string = ""
    this = True
    for letter in string:
        if this:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
        if letter.isalpha():
            this = not this
        
    return new_string

new_string = alt_case(this_string)
print(new_string)
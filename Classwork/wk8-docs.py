import random
import copy

""" subjects = ["English", "Math", "Science", "Humanities"]
random.shuffle(subjects)
print(subjects)
#shuffles in place 

new_list = random.sample(subjects, k = len(subjects))
print(new_list)
print(subjects) """

##Errror handling

 # x = list(range(20))

# the max value in this list will be 19, not 20, becuase of 0 indexing
#assert x[-1] == 20
# this ca let us know that we were wrog
# assert x[-1] == 20, f"Expected 20, got {x[-1]}"
#this can help us see whats actually correct

orig_list = [2, 9, 20, 54]
new_list = copy.deepcopy(orig_list)
new_list[0] = 11
print(new_list)
assert orig_list[0] == 2, f"expected 2, got {orig_list[0]}"
for x in orig_list:
    if x == 2:
        print(x)

#try except
x = input("Please enter a number:")
try:
    x = int(x)
    print(f"the square of your number is: {x**2}")
except TypeError:
    print("Not a recognizable number.")
    # specifying typeerror , value error, can catch certain errors, when possible

import re


print("What year were you born?")
birth_year = int(input())

print("Have you already had a birthday this year?")
past_birthday = input()
yesRegex = re.compile(r'y|yes', re.I)
noRegex = re.compile(r'n|no', re.I)
if re.search(yesRegex, past_birthday):
    age = 2022 - birth_year
    print("You are", age, "years old. ")
elif re.search(noRegex, past_birthday):
    age = 2021 - birth_year
    print("You are", age, "years old. ") 
else:
    print("Please try again, invalid input, please answer yes or no.")
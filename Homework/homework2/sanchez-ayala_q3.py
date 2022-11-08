

print("What year were you born?")
birth_year = int(input())

print("Have you already had a birthday this year?")
past_birthday = input()
match past_birthday:
    case 'yes'| 'y'|'Yes'|'Y':
        past_birthday = True
    case 'no'|'No'|'N'|'n':
        past_birthday = False
    
if past_birthday == True:
    age = 2022 - birth_year
    print("You are", age, "years old. ")
else:
    age = 2021 - birth_year
    print("You are", age, "years old. ")
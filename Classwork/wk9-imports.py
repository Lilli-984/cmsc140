from hw5_q1 import alt_case


print("Please enter a string: ")
string = input()
while string != "stop":
    new_string=(alt_case(string))
    print (new_string)
    print("Please enter a string: ")
    string = input()


""" # print("Hello")
# num = input("Enter a number: ")
# print("Your number was: ", num)
# name_length = len("acacia")
# print(name_length)

# print(len("acacia"))

# print(4)
# print(7==3)

# my_sum = 0 
# for i in range(1,21):
#     my_sum += i
# print(my_sum)

def our_first_function():
    print("this is a function")

our_first_function()
print("This is after the function")

def excited_print(my_string):
    return my_string + "!!!!!"
string1 = excited_print("hello")

# def number_add_2(num):
#     print(num +2)
# number_add_2(73)

def adder(num1, num2):
    my_sum = num1 + num2
    return my_sum


#Excerisice 1
def exponent(n1, n2):
    num = n1**n2
    return num
print(exponent(7,3))

def is_equal(num1, num2):
    if num1 == num2:
        print("this is equal")
    else:
        return "They are not equal"
is_equal(7,8)
is_equal(1,1)
 """""" 
#Exercise 2 Part A
print("Enter a number:")
start = int(input())
def collatz(start):
    while start>1:
        if (start % 2) == 0:
            start = int(start/2)
            print("Div by 2:", start)
        else:
            start = int((start*3)+1)
            print("Times 3 plus 1:", start)
collatz(start)
 """
#Exercise 32 part B
print("Enter a start:")
start = int(input())
print("Enter an end")
stop = int(input())
def longest_collatz(start, stop):
    longest = 0
    length = 0
    for x in range(start,(stop+1)):
        counter = 0
        num = x
        while x >1:
            if (x % 2) == 0:
                x = int(x/2)
                counter += 1
            else:
                x = int((x*3)+1)
                counter += 1
            if counter > length:
                length = counter
                longest = num
    return longest
longest_collatz(start, stop)
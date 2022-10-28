def my_sum(start, end):
    num = start
    while num<end:
        num += 1
        start += num
    return(start)

def countdown(start_num, difference):
    print("Countdown:")
    while start_num>=0:
        print(start_num)
        start_num -= difference
        
def function_chooser():
    print("Welcome to the function chooser. Please choose a function.")
    print("1 = Cumulative Sum")
    print("2 = Countdown")
    print("Your choice: ")
    choice = int(input())
    if choice == 1:
        print("Please enter a first number:")
        start = int(input())
        print("Please enter the second number:")
        end = int(input())
        a = my_sum(start, end)
        print("The sum of every number between those two numbers is: ",a)
    elif choice == 2:
        print("Please enter a start number:")
        start_num = int(input())
        print("Please enter a number to count by:")
        difference = int(input())
        countdown(start_num, difference)

def silly_program():
    x = 0
    # Q2 MARKER
    while x < 2:
        for i in range(3):
            print(i)
            if i == 2:
                print(i, "is my favorite number")
        x += 1
x = 5 
# Q1 MARKER
print("This is my program.")
print(silly_program())
""" print("Enter a number:")
start = int(input())
counter = 0
while start>1:
    if (start % 2) == 0:
        start = int(start/2)
        print("Div by 2:", start)
        counter += 1
    else:
        start = int((start*3)+1)
        print("Times 3 plus 1:", start)
        counter += 1
print ("Length of chain: ",counter) """

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
# To make our terrible number guesser less terrible, we could make it so that the 
#program let you know if you got it right or wrong. In addition to that,
#we could also let the user know if they are too low or too high in their guess.
print("Welcome to the random number guesser.")
print("Please input a number between 1 and 10: ")
yourNum = int(input())
myNum = 5
while yourNum != myNum:
    if yourNum > myNum:
        print("You chose", yourNum,", which is higher than the number I chose.")
        print("Please input a number between 1 and 10: ")
        yourNum = int(input())
    elif yourNum < myNum: 
        print("Your number is lower than the number I chose")
        print("Please input a number between 1 and 10: ")
        yourNum = int(input())     
print("You got it right! My number was", myNum)
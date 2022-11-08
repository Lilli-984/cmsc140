print("Welcome to the random number guesser.")
print("Please input a number between 1 and 100: ")
yourNum = int(input())
import random
myNum = random.randint(1, 100)
while yourNum != myNum:
    if yourNum > myNum:
        print(yourNum," is too high. Try again:")
        yourNum = int(input())
    elif yourNum < myNum: 
        print(yourNum, "is too low. Try again.")
        yourNum = int(input())     
print("You got it! The correct number was:", myNum)


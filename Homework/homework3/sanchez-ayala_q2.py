import random
def random_number_guesser():
    print("How many guesses?")
    guesses = int(input())
    print("Welcome to the random number guesser.")
    print("Please input a number between 1 and 100: ")
    yourNum = int(input())
    myNum = random.randint(1, 100)
    while guesses > 1 and yourNum != myNum:
        if yourNum > myNum:
            guesses -= 1
            print(yourNum," is too high. Try again. (",guesses," guesses left)")
            yourNum = int(input())
        elif yourNum < myNum: 
            guesses -= 1
            print(yourNum, "is too low. Try again. (",guesses," guesses left)")
            yourNum = int(input()) 

    if yourNum == myNum:
            print("You got it! The correct number was:", myNum)

    else:
        print("Sorry! You lost! The correct number was: ",myNum)


    random_number_guesser()
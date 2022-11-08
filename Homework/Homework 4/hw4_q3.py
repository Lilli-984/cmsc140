
import random

def random_number_guesser():
    print("How many guesses?")
    total_guesses = int(input())
    guesses = total_guesses
    print("Welcome to the random number guesser.")
    print("Please input a number between 1 and 100: ")
    yourNum = int(input())
    myNum = random.randint(1, 100)

    guess_list = [yourNum]

    def average_func():
        average = 0
        total = 0
        for x in guess_list:
            total += x
            average = total/total_guesses
        print("The average of all your guesses is: ",average)

    while guesses > 1 and yourNum != myNum:
        if yourNum > myNum:
            guesses -= 1
            print(yourNum," is too high. Try again. (",guesses," guesses left)")
            yourNum = int(input())
            guess_list = guess_list + [yourNum]
        elif yourNum < myNum: 
            guesses -= 1
            print(yourNum, "is too low. Try again. (",guesses," guesses left)")
            yourNum = int(input())     
            guess_list = guess_list + [yourNum]
    if yourNum == myNum:
        print("You got it! The correct number was:", myNum)
        average_func()
    else:
        print("Sorry! You lost! The correct number was: ",myNum)
        average_func()

random_number_guesser()


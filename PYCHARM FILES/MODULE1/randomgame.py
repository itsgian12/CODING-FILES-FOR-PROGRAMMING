from random import randint
import sys
answer = randint(int(sys.argv[1],sys.argv[2]))


while True:
    try:
        guess = int(input("Enter your guess between 1 and 10: "))
        if 0 < int(guess) < 11:
            if int(guess) == answer:
                print("You are amazing, how did you do that.")
                break
        else:
            print("hey bozo, i said 1-10")
    except ValueError:
        print("Please enter a valid number")
        continue

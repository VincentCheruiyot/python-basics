#Number game intro as per video no. 26

import random  

#generate a random number between 1 to 10
secret_num=random.randint(1, 10)
guesses = []

while len(guesses)<3:
    try:
        #get a number guess from the player
        guess =int(input("Guess a number between 1 and 10: "))
    except ValueError:
        print("{} isn't a number!".format(guess))
    else:
        #compare guess to secret number
        if guess==secret_num:
            print("You got it! My number was {}".format(secret_num))
            break
else:
    print("That's not it!")
guesses.append(guess)

#safely make an int
#limit guesses
#too high message
#too low message
#play again

game()


#print hit/miss

#variable, functions, classes, lists



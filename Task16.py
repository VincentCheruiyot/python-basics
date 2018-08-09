#Letter game refinement as per video 29

import random

#make a list of words
words = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon',
]
while True:
    start=input("Press enter/return to start, or enter Q to quit")
    if start.lower()=='q':
        break

    #pick a random word
    secret_word=random.choice(words)
    bad_guesses=[]
    good_guesses=[]

    while len(bad_guesses)<7 and len(good_guesses)!=len(list(secret_word)):
        #draw spaces
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, ends='')
            else:
                print('_',end=='')

            print('')
            print('Strikes:{}/7'.format(len(bad_guesses)))
            print('')

    #take guess
    #draw guessed letters and strikes
    #print out win/lose






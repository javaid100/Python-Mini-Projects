# ======= Hangman Game ===============

import random

name = input("Enter your name: ") 
print("Good Luck!", name)

words = ['rainbow', 'laptop', 'programming', 'python', 'player', 'condition', 'reverse']
word = random.choice(words)     # Function will choose one random word from this list of words
print('Length of the word = ', len(word))

print("============================================")
print("=========== Guess the characters ===========")
print("============================================")

turns = 5    # Number of turns 
guesses = ''

while turns > 0:
    guess = input("Enter a character: ")
    guesses += guess

    failed = 0  
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1    
             
    if failed == 0:
        print("******* You Win *******")
        print("The word is: ", word)
        break
     
    # check input with the characters in word
    if guess not in word:  
        turns -= 1
        print("Wrong")   
        print("You have", turns, 'more guesses left')   
        if turns == 0:
            print("======= You Loose =======")


# Hangman Project Documentation

## Milestone 1 - Setup the environment
Familiarised with Git commans and GitHub platform 

## Milestone 2 - Create the variables for the game
Completed all the given tasks and successfully upload the codes to Github.

The following are the written Python codes


import random
word_list = ['apple', 'banana', 'orange', 'pineapple', 'peach']
print (word_list)
# 
print ("{} {} {} {} {}".format("apple", "banana", "orange", "pineapple", "peach") )
word = random.choice(word_list)
# 
print (word)
guess = input ("Please enter a single letter")

if len(guess)==1:
    print ("Good guess!")
else:
    print ("Oops! That is not a valid input.")
print (guess)


## Milestone 3 - Check if the guessed character is in the word


check_guess and ask_for_input functions were created to group block of codes.

The check_guess function will take the guessed letter as an argument and check if the letter is in the word. The function will first convert the guesses word to be in lower case.

The ask_for_input function will iteratively check if the guessed letter exist inside a word. It will also perform nested function as the check_guess function is being called internally.


### Heading 2
#### Heading 3
##### Heading 4

- satu
    - satu satu
- dua
- tiga

1. lagi satu
2. lagi dua

> hello

#
# Create a new script called milestone_3.py. This file will contain the code for the third milestone.

#Define the __init__ method of the Hangman class.

#Step 1. Create a class called Hangman.

#Step 2. Inside the class, create an __init__ method to initialise the attributes of the class. 
#Pass in word_list and num_lives as parameters. Make num_lives a default parameter and set the value to 5.


class Hangman:
  def __init__(self, word_list , num_lives):
    self.num_lives = 5
    self.word_list = [word_list]
    word = random.choice(self.word_list)
    word_guessed =[]
    for i in range(len(word)):
      word_guessed.append(" ") 
    num_letters = len(word)
    list_of_guesses = []


# Step 3. Initialise the following attributes:

# word: The word to be guessed, picked randomly from the word_list. 
# Remember to import the random module into your script.

# word_guessed: list - A list of the letters of the word, with '' for each letter not yet guessed. 
# For example, if the word is 'apple', the word_guessed list would be ['', '', '', '', '']. 
# If the player guesses 'a', the list would be ['a', '', '', '', ''].
# num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.
# num_lives: int - The number of lives the player has at the start of the game.
# word_list: list - A list of words.
# list_of_guesses: list - A list of the guesses that have already been tried. 
# Set this to an empty list initially.


# In this task, you will create a method that will ask the user to guess a letter and 
# another method that will check if the guess is in the word.
# Remember that a method is a function that is defined inside a class.
# Let's create the check_guess method.

# Step 1: Define a method called check_guess. Pass the guess to the method as a parameter. 
# In the body of the method, write the code for the following steps:
# Convert the guessed letter to lower case

# Create an if statement that checks if the guess is in the word
# In the body of the if statement, print a message saying "Good guess! {guess} is in the word."

# You will continue with the logic of the check_guess method in the next task. 


def check_guess(guess):
	guess.lower()
	if guess in word:
    print("Good guess!", guess, "is in the word.")
    for i in range(len(word)):
      if guess == word[i]:
      word_guessed.insert(i, guess)
    
    num_letters -= 1
  
  else:
    self.num_lives -= 1
    print ("Sorry,", guess, "is not in the word.")
    print ("You have", self.num_lives, "lives left.")

   list_of_guesses.append(guess)

# For now, let's create the ask_for_input method.
# Step 1. define a method called ask_for_input. In the body of the method, do the following:

def ask_for_input():
  while True:
    guess = input("Please enter a single letter")
    if len(guess)>1:
      print("Invalid letter. Please, enter a single alphabetical character.")
    elif guess in self.list_of_guesses:
      print("You already tried that letter!")
    else check_guess(guess)
      list_of_guesses.append(guess)
      break
#Create a while loop and set the condition to True.
#Ask the user to guess a letter and assign this to a variable called guess.

# Create an if statement that runs if the guess is NOT a single alphabetical character.
# In the body of the if statement, print a message saying "Invalid letter. Please, enter a single alphabetical character."
# Create an elif statement that checks if the guess is already in the list_of_guesses.
# In the body of the elif statement, print a message saying "You already tried that letter!".
# If the guess is a single alphabetical character and it's not already in the list_of_guesses:
# Create an else block and call the check_guess method. Remember to pass the guess as an argument to this method.
# Add the guess to the `list_of_guesses.

# Step 2. Call the ask_for_input method to test your code.

#Return to your check_guess method and extend it to replace the underscore(s) in the word_guessed 
#with the letter guesssed by the user.

# In the if block of your check_guess method, after your print statement, do the following:
# Create a for-loop that will loop through each letter in the word.
# Within the for-loop, do the following:
# Create an if statement that checks if the letter is equal to the guess.
# In the if block, replace the corresponding "_" in the word_guessed with the guess. 
# HINT: You can index the word_guessed at the position of the letter and assign it to the letter.

# Outside the for-loop, reduce the variable num_letters by 1.

# Define what happens if the guess is not in the word you are trying to guess.
# Step 1. In the check_guess method, Create an else statement.
# Step 2: Within the else block:
# Reduce `num_lives' by 1.
# print a message saying "Sorry, {letter} is not in the word."
# print another message saying "You have {num_lives} lives left."
# Step 3. Lastly, append the guess to the list_of_guesses. 
# Ensure you do this outside the else block so that the letter can be appended 
# to the list_of_guesses in both conditions.
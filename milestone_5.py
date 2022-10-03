# %%
import random

class Hangman:
  def __init__(self, word_list , num_lives):
    self.num_lives = 5
    self.word_list = [word_list]
    self.word = random.choice(word_list)
    self.word_guessed =[]
    for i in range(len(self.word)):
      self.word_guessed.append(" ") 
    self.num_letters = len(self.word)
    self.list_of_guesses = []

  def check_guess(self, guess):
    guess.lower()
    if guess in self.word:
      print("Good guess \'",guess,"\' is in the word")
      for i in range(len(self.word)):
        if guess == self.word[i]:
          self.word_guessed[i] = guess
          self.num_letters -= 1
      
    else:
      self.num_lives -= 1
      print ("Sorry,", guess, "is not in the word.")
      print ("You have", self.num_lives, "lives left.")

    self.list_of_guesses.append(guess)

  def ask_for_input(self):
    while(True):
      guess = input("Please enter a single letter")
      if len(guess)>1:
        print("Invalid letter. Please, enter a single alphabetical character.")
      elif guess in self.list_of_guesses:
        print("You already tried that letter!")
      else:
        self.check_guess(guess)
        break

def play_game():
  word_list = ["apple", "orange", "banana", "peach", "kiwi"]
  num_lives = None
  Game = Hangman(word_list, num_lives)
  while(True):
    if Game.num_lives == 0:
      print("You lost!")
      print("The word is: \"",Game.word,"\"")
      break
    elif Game.num_letters > 0:
      Game.ask_for_input()
    elif Game.num_lives != 0 and Game.num_letters == 0:
      print("Congratulations! You won!")
      print("The word is: \"",Game.word,"\"")
      break
    else:
      break

play_game()
# %%

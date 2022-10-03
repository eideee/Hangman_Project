# %%
import random
word_list = ['apple', 'banana', 'orange', 'pineapple', 'peach']

word = random.choice(word_list)
guess = input("Please enter a single letter")

if guess in word:
    print("Good guess!", guess, "is in the word.")
else:
    print ("Sorry,", guess, "is not in the word. Try again.")

#while word.startswith(guess, 0, 1)!=True:
#	guess = input("Sorry, its not in the word. Try again.")
#else:
#    print("Good guess!", guess, "is in the word.")

#print (word)
# %%

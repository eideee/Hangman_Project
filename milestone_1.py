# %%
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
# %%

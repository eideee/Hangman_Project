def check_guess(guess):
	guess.lower()
	while word.startswith(guess, 0, 1)!=True:
		guess = input ("Sorry, its not in the word. Try again.")
	else:
   		print ("Good guess!", guess, "is in the word.")


def ask_for_input(guess):
	
	while len(guess)>1:
    		guess = input("Please, enter a single alphabetical character.")
 	if len(guess)==1:
        	break

	check_guess(guess)
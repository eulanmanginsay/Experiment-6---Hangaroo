import random
ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
wordList = ['apple','eye','programming', 'ponkan', 'angel','pineapple', 'seventeen', 'serenity', 'power','clone']
secretWord = random.choice(wordList); length_word = len(secretWord); lettersGuessed =[]; guessWord =[]
	

def start():
	print ("Play Hangaroo!")
	start()
	
def secret():
    for character in secretWord:
        guessWord.append("_")
	        
print ("The word you have to guess is made up of ", length_word, "characters")
print (' '.join(guessWord))
print ("You have 4 chances of guessing the letters!") 
	        
def guessing():
	    turns = 0
	    while turns < 5:
	        print ("\n", ' '.join(ABC))
	        guess = input("Letter: \n").lower()
	        
	        if guess not in ABC:
	            print ("Sorry! Try another letter: ")
	            turns +=1
	            print("Mistakes Made: ", turns)
	        elif guess in lettersGuessed:
	            print("You have already guessed that letter: ")
	        else:
	            lettersGuessed.append(guess)
	            if guess in secretWord:
	                print ("Nice! ")
	                for x in range(0, length_word):
	                    if secretWord[x] == guess:
	                        guessWord[x] = guess
	                        print(' '.join(guessWord))
	                ABC.remove(guess)
	            else:
	                print("Sorry! Try Again: ")
	                ABC.remove(guess)
	                turns += 1
	                print("Mistakes Made: ", turns)
	                if turns == 5:
	                    print("You killed the kangaroo!.")
	                    print("The secret word was:", secretWord)
	                    print("GAMEOVER!")
	                    break
	        if '_' not in guessWord:
	                        print("You have guessed the word correctly!")
	                        break              
secret()
guessing()


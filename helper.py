import random

def rules():
	"""
Hangman Rules :
1. Think of a word to be guessed.
2. The word is represented by a series of dashes, each representing a letter.
3. Guess letters one at a time.
4. If the guessed letter is in the word, all occurrences of that letter are revealed.
5. If the guessed letter is not in the word, a part of the hangman is drawn.
6. Continue guessing letters until you either solve the word or make too many incorrect guesses.

Cool?"""

	clearscreen()


def clearscreen():
	print("\033[H\033[J")
	
	
def wordpicker():
    wordfile=open("wordfile.txt")
    wordlist=[wrd.rstrip() for wrd in wordfile]
    word=random.choice(wordlist)
    return word


def parts():
    rawparts=open('hangmanparts.txt').readlines()
    parts_list=[rawparts[u_lim-7:u_lim] for u_lim in range(49,7,-7)]
    return parts_list


def display_changer(curr_display,status,guess):
        curr_display=list(curr_display)
        for index,letter in status:
                if letter==guess:
                        curr_display[index]=letter
                        status.remove((index,letter))
                        break
        return ''.join(curr_display),status


def checker(guess,status):
        for i,j in status:
                if j==guess:
                        return True
        else:
                return False

                                
def addwords():
	wordfile=open("wordfile.txt",'a')
	for count in range(int(input("\nHow many words do you wish to add? "))):
                                new_word=input("\nEnter word: ")
                                new_word+="\n"
                                wordfile.write(new_word)
	else:
                                input("Words added sucessfully!")
                                
def removewords():
	...
import admin,random,os

def rules():                    #Contains a documentation of the rules of hangman
        """
\n\t\tHANGMAN Rules:

+ A word is chosen for you which you must guess.

+ The word is represented by a series of dashes, each representing a letter.

+ Guess letters one at a time.

+ If the guessed letter is in the word, only one occurrence of that letter is revealed even if there is more than one occurence.

+ If the guessed letter is not in the word, a part of the hangman is drawn.

+ Continue guessing letters until you either solve the word or the man is completely hanged. If the man gets hanged completely, you lose!.

Cool?"""

        clearscreen()


def clearscreen():      #Calling this will clear the terminal window (won't work in the IDLE)
        print("\033[H\033[J")
        os.system('cls' if os.name == 'nt' else 'clear')
	
	
def wordpicker():       #Picks a word for the player to guess
        wordfile=open("wordfile.txt")
        wordlist=[wrd.rstrip() for wrd in wordfile]
        word=random.choice(wordlist)
        return word


def parts():                #Makes a list of the parts of hangman to manipulate in main.py
        rawparts=open('hangmanparts.txt').readlines()
        parts_list=[rawparts[u_lim-7:u_lim] for u_lim in range(7,50,7)]
        return parts_list

def display_changer(curr_display,status,guess):                 #Helps change the word status display as the player guesses letters
        curr_display=list(curr_display)
        for index,letter in status:
                if letter==guess:
                        curr_display[index]=letter
                        status.remove((index,letter))
                        break
        return ''.join(curr_display),status


def checker(guess,status):              #Checks if the guess is present in the letter
        for i,j in status:
                if j==guess:
                        return True
        else:
                return False

                                
def addwords():         #Used in admin.py to add words to wordfile
        clearscreen()
        wordfile=open("wordfile.txt",'a')
        for count in range(int(input("\nHow many words do you wish to add? "))):
                new_word=input("\nEnter word: ")
                new_word+="\n"
                wordfile.write(new_word)
        else:
                input("Words added sucessfully!")
        wordfile.close()

                                
def removewords():      #Used in admin.py to remove words from wordfile
        clearscreen()
        input("WARNING:Continuing will remove all words from wordfile!")
        admin.authenticity()
        wordfile=open('wordfile.txt','w')
        wordfile.close()
        input("All words have been removed!")

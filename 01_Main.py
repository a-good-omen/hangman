import sys,admin,helper

start=input("""\t\t\t----HANGMAN----

                                O_|
                               /|     
                               / \\

                               
                     Press ENTER to start!""")

helper.clearscreen()
user=input("\nEnter username: ")

if user=='admin':
        admin.call()            #Invoke admin.py to make some administrator changes

while True:
        choice=input(f"""\nWelcome {user}! How do you want to continue?
        1. How to play?
        2. PLAY game
        3. Exit game

        I {user} choose option number """)

        if choice=='1': input(helper.rules.__doc__); helper.clearscreen()
        elif choice=='2': helper.clearscreen(); break
        elif choice=='3': input("Leaving already?Fine, Exitting...."); sys.exit()
        else: input("No such option!? "); helper.clearscreen()

input("Loading......")

word=helper.wordpicker()                    #Picks a word
display='_'*len(word)
hangman=helper.parts()
chance=7                                    #Player gets 6 chances cause only those many parts to draw for the hangman
progress=list(enumerate(word))              #A list containing the index of each word and the corresponding letter
guesscount=0


while True:
        helper.clearscreen()
        if chance!=1 and display!=word:
                hangman_status=hangman[7-chance]
                for curr_hang in hangman_status: print(curr_hang,end="")
                
                if chance==0: break
                guess=input(f"\nStatus: {display} \nYour Guess ({chance-1} chances):")
                guess=guess.lower()
                
                if len(guess)!=1:
                        input("Your guess should consist one letter\n")
                        continue
                result=helper.checker(guess,progress)

                if result==True:
                    input("\nThat's Correct!\n")
                    display,progress=helper.display_changer(display,progress,guess)
                else:
                    chance-=1
                    input(f"\nSorry, no such letter! T_T ({chance} chances left!)\n")
                guesscount+=1

        else:
                break

for curr_hang in hangman_status: print(curr_hang,end='')        #Shows the player the man's condition at game ka end
input(f"CONGRATS! You win! (Took you {guesscount} turns!)" if display==word else f"Sorry, your word was \"{word}\" and you had {display.count('_')} letter(s) more to guess")

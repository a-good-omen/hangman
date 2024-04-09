import admin,helper

start=input("""\t\t----HANGMAN----

                   \t          Press ENTER to start!""")

user=input("\nEnter username: ")

if user=='admin':
        admin.call()

while True:
	choice=input(f"""\nWelcome {user}! How do you want to continue?
	1. How to play?
	2. PLAY game
	3. Exit game
	
	I {user} choose option number """)

	if choice=='1': input(helper.rules.__doc__);helper.clearscreen()
	elif choice=='2': helper.clearscreen(); break
	elif choice=='3': input("Thank you! Exitting...."); exit()
	else: input("No such option!? "); helper.clearscreen()

input("Loading......")

word=helper.wordpicker()
display='_'*len(word)
hangman=helper.parts()
chance=7
progress=list(enumerate(word))
guesscount=0

while True:
    helper.clearscreen()
    if chance!=0 and display!=word:
        hangman_status=hangman[chance-7]
        for curr_hang in hangman_status: print(curr_hang,end="")     
        if chance==0: break
        guess=input(f"\nStatus: {display} \nYour Guess ({chance} chances):")
        guess=guess.lower()
        if len(guess)!=1:
        	input("Your guess should consist one letter\n")
        	continue
        result=helper.checker(guess,progress)

        if result==True:
            print("\nThat's Correct!\n")
            display,progress=helper.display_changer(display,progress,guess)
        else:
            chance-=1
            print(f"\nSorry Incorrect :( ({chance} chances left!)\n")
        guesscount+=1

    else:
        break
        
print("CONGRATS! You win!" if display==word else f"Sorry, you had {display.count('_')} letter(s) more to guess")
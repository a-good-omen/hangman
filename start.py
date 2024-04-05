import admin,helper

user=input("""\t\t----HANGMAN!!----

                   \t          Press ENTER to start!""")

if user=='admin':
	admin.call()

word=helper.wordpicker()
display='_'*len(word)
hangman=helper.parts()
chance=7
progress=list(enumerate(word))

while True:
    if chance:
        hangman_status=hangman[chance-7]
        for curr_hang in hangman_status: print(curr_hang)     
        guess=input(f"{display} \nYour Guess:")
        guess=guess.lower()
        result=helper.checker(guess,progress)

        if result==True:
            print("\nThat's Correct!")
            display,progress=helper.display_changer(display,progress,guess)
        else:
            chance-=1
            print(f"\nSorry Incorrect :( ({chance} chances left!)")
            
    else:
        break

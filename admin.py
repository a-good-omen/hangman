import sys,helper

x="*****"


def authenticity():
        helper.clearscreen()
        global x
        for count in range(3):
                pwd=input("\nEnter current password:")
                if pwd!=x:
                        print("Access DENIED!!")
                else:
                        input("Access GRANTED") 
                        break
        else:
                print("UNAUTHORIZED!")
                sys.exit()


def password_changer():
                helper.clearscreen()
                global x
                authenticity()
                x=input("\nEnter new password: ")
                input("Password changed!")        


def call():
        global x,wordfile
        authenticity()

        for chance in range(5):
                helper.clearscreen()
                choice=input("""\nWhat would you like to do?
                        1. Add words
                        2. Remove Words
                        3. Change ADMIN Password
                        4. Continue with the program?
                                
                        As the ADMIN, I wish to """)

                if choice=="add words":
                        helper.addwords()

                elif choice=="remove words":
                                words=wordfile.readlines()
                                for count in range(int(input("\nHow many words do you wish to remove?"))):
                                        rem_word=input("Enter word to be removed: ")
                                        rem_word+="\n"
                                        if rem_word in words:
                                                for pos in range(len(words)):
                                                         if words[pos]==rem_word:
                                                                 del words[pos]
                                        else:
                                                print("Word not present in file!")                                

                elif choice=="change the password":
                        password_changer()

                elif choice=="continue with the program":
                        print("Exitting...")
                        helper.clearscreen()
                        break
				
                else:
                        continue
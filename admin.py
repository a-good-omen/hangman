import sys

wordfile=open("wordfile.txt",'a+')
x="*****"


def authenticity():
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
		global x
		authenticity()
		x=input("Enter new password: ")
		input("Password changed!")	
	    		
	    			    			    			    			    		
def call():
	global x,wordfile
	authenticity()
	
	for chance in range(5):
		choice=input("""\nWhat would you like to do?
			1. Add words
			2. Remove Words
			3. Change ADMIN Password
			4. Continue with the program?
				
			As the ADMIN, I wish to """)
				
		if choice=="add words":
			for count in range(int(input("\nHow many words do you wish to add? "))):
				new_word=input("\nEnter word: ")
				new_word+="\n"
				wordfile.write(new_word)
			else:
				input("Words added sucessfully!")
			
		elif choice=="remove words":
				words=wordfile.readlines()
				for count in range(int(input("\nHow many words do you wish to remove? "))):
					print("NOTE: Letter Case is important!\n")
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
			print("\nThank you!")
			break
	
		else:
			continue
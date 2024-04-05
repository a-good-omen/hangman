import random


def wordpicker():
    wordfile=open("wordfile.txt")
    wordlist=[wrd.rstrip() for wrd in wordfile]
    word=random.choice(wordlist)
    return word


def parts():
    rawparts=open('hangmanparts.txt').readlines()
    parts_list=[rawparts[u_lim-7:u_lim] for u_lim in range(7,49,7)]
    return parts_list

        
def display_changer(curr_display,status,guess):
	for index,letter in status:
		if letter==guess:
			curr_display[index]=letter
			status.remove((index,letter))
			break
	return ''.join(curr_display),status
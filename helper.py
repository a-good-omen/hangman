import random


def wordpicker():
    wordfile=open("words.txt")
    wordlist=[wrd.rstrip() for wrd in wordfile]

    word=random.choice(wordlist)

    return word


def parts():
    rawparts=open('hangmanparts.txt').readlines()
    parts_list=[rawparts[u_lim-7:u_lim] for u_lim in range(7,49,7)]

    return parts_list

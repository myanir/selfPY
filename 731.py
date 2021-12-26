def show_hidden_word(secret_word, old_letters_guessed):
    x=1#check if all letter guessed
    for letter in secret_word:
        if letter in old_letters_guessed:
            print (letter,end=" ")
        else:
            print("_ ",end=" ")
            x=0
    return x

old_letters_guessed=['a','y','t','n','p','o','h']
import random
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
#secret_word = random.choice(WORDS)
secret_word = "python"
win=show_hidden_word(secret_word, old_letters_guessed)
if win == 0:
    print ("\nfalse")
else:
    print("\nwin")
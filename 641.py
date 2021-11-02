
def is_valid_input(guess, list_allready_guessed):
    lng = len(guess)
    if lng == 1:
        if guess.isalpha():
            if guess not in list_allready_guessed:
                list_allready_guessed += [guess]
                print(guess.lower())
                return True
            else:
                print("this char allready guessed")
                sorted_used_letter=sorted(list_allready_guessed)
                print("you tried:", *sorted_used_letter)
                return False
        else:
            print("your guess is not a char(E2)")
            return False
    else:
        if guess.isalpha():
            print("your guess is more than 1 char (E1)")
            return False
        else:
            print("your guess is more than 1 char and is not only letters (E3)")
            return False


#main()
n = 0
list_allready_guessed = []
while n < 10:
    guess = input("please enter1 char for your guess: ")
    isvalid = is_valid_input(guess, list_allready_guessed)
    print(isvalid)
    n += 1

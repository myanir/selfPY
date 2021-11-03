guess = input("please enter1 char for your guess: ")
lng = len(guess)
if lng == 1:
    if guess.isalpha():
        print(guess.lower())
    else:
        print("your guess is not a char(E2)")
else:
    if guess.isalpha():
        print("your guess is more than 1 char (E1)")
    else:
        print("your guess is more than 1 char and is not only letters (E3)")

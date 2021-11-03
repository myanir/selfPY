def sequence_del(my_str):
    new_string = ""
    current_letter = ""
    for  letter in my_str:
        if letter != current_letter:
            current_letter = letter
            new_string+=current_letter
    return new_string
nn = input("please enter a string: ")
new_str=sequence_del(nn)
print (new_str)


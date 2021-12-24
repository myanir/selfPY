def arrow(my_char, max_length):
    for i in range(max_length+1):
        print(my_char*i)
    for i in range(max_length):
        print(my_char * (max_length-1-i))


c = input('choose 1 char')
max = int(input("enter max length"))
arrow(c,max)
#function check if the last charcter avilable beofore in the  string
def last_early(my_str):
    last=my_str[-1]
    if last in my_str[:-1]:
        print("ok")
    else:
        print("False")
        return True
str_to_chk=input("please enter a string to check if the last charcter showed before: ")
str_to_chk=str_to_chk.lower()
last_early (str_to_chk)


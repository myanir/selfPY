#function check if the last charcter avilable beofore in the  string
def last_early(my_str):
    last=my_str[-1]
    if last in my_str[1:-2]:
        return True
str_to_chk=input("please enter a string to check if the last charcter showed before: ")
ok=last_early (str_to_chk)
if ok ==True:
    print(ok)
else:
    print ("False")
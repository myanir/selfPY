import string
def numbers_letters_count(my_str):
    a=0
    n=0
    for i in my_str:
        chk=i.isnumeric()
        if chk:
            n+=1
        else:
            a+=1
    return (n,a)
    #return None


#st=input("enter sentense with numbers :")
#numbers_letters_count(st)
numbers,letters=(numbers_letters_count("Python 3.6.311"))#print number of nunmbers and number of not numbers
print("number of numbers:",numbers,"\nnumber of letters",letters)



words=["yanir","melamed","yanir"]
user_choise=0
x=user_choise


def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


print("1)print items list\n"
      "2)print number of items\n"
      "3)enter  item to check if allready in list\n"
      "4)enter item and will show you how many in list\n"
      "5)which item to delete from list?")
print(   """6)add item to list"
7)forbiiden items (short then 3 char or with notnumeric
8)remove duplicates from list
9)exit""")
while x != 9:
    x = int(input("choose from menu "))
    if x == 1 :
        for i in range(len(words)):
            print (words[i])
    if x == 2:
        print (len(words))
    if x == 3 :
        tochk=input("which item to check if exist in the list? ")
        if tochk in words:
            print("the item exist")
        else:
            print ("the item not in the list")
    if  x == 4:
        tochk = input("which item to check if exist in the list? ")
        countX(words, tochk)
        print('{} has occurred {} times'.format(tochk, countX(words, tochk)))
    if x == 5:
        tochk = input("which item to delete( if exist in the list)? ")
        if tochk in words:
            words.remove(tochk)
            for i in range(len(words)):
                print(words[i])
    if x == 7:
        tochk = input("which item to add to the list? ")
        words.append(tochk)
    if x == 8:
        words = list(dict.fromkeys(words))
        print(*words)
    if x == 9:
        break




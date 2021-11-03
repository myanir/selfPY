def greater(list, n):
    newlist=[]
    for num in list:
        if n<num :
            newlist+=[num]

    return (newlist)

list = [6,4,8,9,22,11,44,32,12]
nn = int(input("please enter a number: "))
new=greater(list, nn)
print(sorted(new))

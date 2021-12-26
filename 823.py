
def mult_tuple(tuple1, tuple2):
    for x in tuple1 :
        for y in tuple2:
            newlist.append([x,y])
            newlist.append([y, x])
    print(newlist)
    tup=tuple(newlist)
    print(type(tup))


newlist=[]
first_tuple = (1, 2)
second_tuple = (4, 5)
new=mult_tuple(first_tuple, second_tuple)




def shift_left(mylist):
    print("my original list:",mylist)
    long = len(mylist)
    end = mylist[0]
    n=0
    while n<long-1:
        mylist[n]=mylist[n+1]

        n=n+1
    mylist[-1]=end
    print(mylist)


name=list("yanir")
shift_left(name)

salad = ("cucumber", "tomato", "onion")
print(type(salad))

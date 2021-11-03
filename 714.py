def squared_numbers(start, stop):
    while (start <= stop):
        print (start**2)
        start+=1

x=int(input('enter small number:'))
y=int(input('enter big number:'))
squared_numbers(x, y)

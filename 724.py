def seven_boom(end_number):
    for i in range (0,end_number+1):
        if ("7" in str(i)) or  (i % 7==0):
            print ("BOOM")
        else:
            print(i)

end_number=int(input("enter number:"))
seven_boom(end_number)

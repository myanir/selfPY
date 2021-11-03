def filter_teens(num1=13, num2=13, num3=13):
    sum=fix_age(num1)+fix_age(num2)+fix_age(num3)
    print("the sum of the ages of the children between 15 to 16 :\n",sum)

def fix_age(age1):
    if (age1 < 15 and age1 > 12) or (age1 > 16 and age1 < 20):
        return 0
    else:
        return age1

def main():

    sum1=0
    num1 = int(input("eneter age1 : "))
    num2 = int(input("eneter age2 : "))
    num3 = int(input("eneter age3 : "))
    #filter_teens(13, 16, 13)
    filter_teens(num1, num2 ,num3)
main()
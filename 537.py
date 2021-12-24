def chocolate_maker(small, big, x):
    large = 5
    mini = 1
    print(small * mini, "+", large * big, "?", x)
    size = (small * mini + large * big)
    print("size=", size, ",x=", x)
    if (x < size) or (x == size):
        print("True")
    else:
        print("False")


def main():
    s = int(input("enter the number of small chocolate (1cm) : "))
    b = int(input("enter the number of big chocolate (5cm) : "))
    x = int(input("enter the length of the chocolate line : "))
    chocolate_maker(s, b, x)


main()

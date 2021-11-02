def chocolate_maker(small, big, x):
    large = 5
    mini = 1
    print(small * mini, "+", large * big, "?", x)
    if x == (small * mini + large * big):
        print("True")
    else:
        print("False")


def main():
    s = int(input("enter the number of small chocalete (1cm) : "))
    b = int(input("enter the number of big chocalete (5cm) : "))
    x = int(input("enter the length of the choclete line : "))
    chocolate_maker(s, b, x)


main()

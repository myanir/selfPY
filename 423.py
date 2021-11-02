print("enter temp end with c/f")
tmp = str(input())
tmpdigits = int(tmp[:-1])
if tmp[-1] == "c" or tmp[-1] == "C":
    print("celcius to farenhite:")
    Far = (tmpdigits * 9/5) + 32
    print(Far)
elif tmp[-1] == "f" or tmp[-1] == "F":
    Cel = (tmpdigits - 32) * 5 / 9
    print("farenhie to celcius:", Cel)
else:
    print("wrong input")

import string
txt = str(input("enter 5 word:"))
long = len(txt)
half = long//2
print("txt half long:", half)
print("txt full length:", long)
print(txt[0:half].upper() + (txt[half+1:]))
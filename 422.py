print("enter a word:")
txt = str.upper(input())
back = txt[::-1]
print (txt, back)
if txt.upper() == back:
    print("ok")
else:
    print("not")

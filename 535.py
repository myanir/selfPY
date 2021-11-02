def distance(num1, num2, num3):
    a = abs(num2) - abs(num1)
    b = abs(num3) - abs(num1)
    if (a == 1) or (b == 1):
        if (a > 2) or (b > 2):
            return True
        else:
            return False
    else:
        return False
ok = distance(1, 2, 4)
print(ok)

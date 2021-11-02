"""
check if random ip is private or public"""
import random
def ipgenerator():
    oct1 = random.randint(0,223)
    oct2 = random.randint(0,255)
    oct3 = random.randint(0, 255)
    oct4 = random.randint(0, 255)
    ip=[oct1, oct2, oct3, oct4]
    print(ip)
    return ip


def chk(ip):
    if ip[0] == 10:
        return True
    else:
        if ((ip[0] == 172) and (ip[1]>15 and ip[1]<32)):
            #print("private")
            return True
        else:
            if ((ip[0] == 192) and (ip[1] == 168)):
                #print ("private")
                return True
            else:
                #print("public")
                return False


address=ipgenerator()
isprivate = chk(address) #([172,16,0,0])
if isprivate == True:
    print("private")
else:
    print("public")




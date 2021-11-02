number = int(input ("enter number 3 digits"))
a=int(number//100)
a1=number%100 #42
b=a1//10
c=a1%10
sum=a+b+c
print ("a=",a,"a1=",a1,"b=",b,"c=",c)
print ("total",sum)

print("each:",number//3,"sherit:",number%3)
if ((number%3==0)) : print("no sherit") 
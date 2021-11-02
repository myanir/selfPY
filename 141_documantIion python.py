print ("""
      _    _
...  | |  | |
...  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
...  |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
...  | |  | | (_| | | | | (_| | | | | | | (_| | | | |
...  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
...                       __/ |
...                      |___/
""")
import random
print(random.randint(5, 10)) #random number

course = "python" # mishtane -->object (string)
unit_name = 'variables' #object string
unit_number = 2 #object integer
movie_long =7.25 #float
current_unit=unit_number
next_unit=current_unit+1
print("ive allready mastered",current_unit-1,"units in python")

hungry=true
number_of_sandwiches=2
i_am_hungry=number_of_sandwiches<4 #boolean i_am_hungry=true (0=false) 
#operators == / != / not / number_of_sandwiches == 2 and cups_of_key == 6 /(number_of_sandwiches == 2) or (cups_of_key == 6)
#operators for string : "breeak" in "breakfast" --> true
# help() #help("in") to exit q
#operattors : in (for text) == for compare , and\or
# \ to continue to next line
#0 = false in boolean(logic) all other numbers =true

print("""	Example	Try it
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y """)

name=input("please enter your name")
print ("hello ,",name)

_ #show the last result

number=input("enter number")
print(int(number)**2) #casting
float(number)#casting

type(veriable) #מציג סוג המשתנה
import.math
math.sqrt(25)


function_name (parameter1,parameter2)

object.method_name(parameter1,parameter2) #קריאה למטודה עבור האובייקט
                                           # האובייקט הןא פרמטר 0 עבור המטודה
"print me in uppercase".upper()
"1".zfill(5) #method on string object

x=str(x) #שינוי סוג המשתנה
\n #new line
\t #tab

card_str="joker"
card_str[0] #take the index value from string
card_str[-5] # take the index value from string(count from the end) -->output will be J
card_str[0:2] #חיתןך 2המקומות הראשונים
card_str[1:-1] #output oke
card_str[0:4:2]#string[start:stop:step] -->output jkr#גוזר רק האי זוגי למקרה זה בלבד
#STR IS IMMUTABLE # לא ניתן לשנות ערך מחרוזת אלא רק ההצבעה על ערך חדש

iterable #ניתן לחזור עליו

len(msg) #length of msg

"string".upper()

IndentationError #שגיאת הזכה

nameError #  שגיאה מתנאי שמצביעה על כך שהמשתנה _____ אינו מוגדר,כלומר לא חשבנו על ערך שמתקבל בעבור התנאי , כדי להמנע מכך מוגדר להגדיר למשתנה ערך התחלתי.

שגיאה מסוג nameError שמצביעה על כך שהמשתנה message אינו מוגדר.
#לעיתים בכתיבת תוכנית אנחנו פותחים בלוק אבל עדיין לא "ממלאים" אותו בקוד. במקרה כזה נשתמש בפקודה שמדלגת - pass.
#פקודה זו שימושית בין השאר כשרוצים להריץ חלק מתוכנית כדי לבדוק אותה, אך לפני שכתבנו חלקים אחרים.
#דוגמה לשימוש ב-pass:
if python_grade > 90: #אחרי תנאי צריך נקודותיים
  print("I'm so proud of you!")
else:
  pass # TODO: print(<Add a motivational statement>)




where_peterpan="neverland"
where_snowwhite="forest"
where_peterpan,where_snowwhite=where_snowwhite,where_peterpan#החלפת ערך בין משתנים

using debugger:
python -m pdb <filename>

txt="yanir"
txt.isalpha()
txt.upper()
txt.lower()

#בעת כתיבת קוד באינטרפרטר, תוכלו להיעזר במשתנה שנקרא "_" (קו תחתי). במשתנה זה נשמרת באופן אוטומטי התוצאה של הפעולה האחרונה שהתבצעה.
-------------------
using functions:
#def func_name(parameter):
#func_name(argument) calling the function and sending the argument that will be accept by the fuction as parameter
#for any functio i need to document which argumrnt i pass the functio and what is her type (wrong parameter type will cause type_error
global variable example:
    a = 0
    def my_function():
        global a
        a = 3
        print(a)

    my_function() -->output 3
    print(a)-->output 3

--------------------
example2:
c = 1
def foo3():
    c = c + 1
    print (c)

foo3() --->error c not defined in function
print(c)
--------------------
תיעוד פונקציה
def  num_of_water_bottles():
###  discriptiom what the function do
:param  <parameter name>:<what the parameter is use for
:type   <parameter name>: parameter_type:   float/int/....
:return:    <discription which value we return /return None
:rtype: which type we return (var/float/...)

==============================
my_math.py
def add(num1, num2):
    print("The result is:", num1 + num2)

def main():
    add(3,1)

if __name__ == "__main__":
    main()
כעת נריץ שוב את הקובץ another_program.py (שכולל יבוא לקובץ הספרייה my_math וקריאה לפונקציה (2 ,5)add מתוכו):

another_program.py
import my_math

my_math.add(5, 2)
The result is: 7

#build a list
letters="science"
list_of_letters=list(letters)
print(list_of_letters) # see the list
#===============================
#keeping values of list to variables:
cool_trick = [1, 2, 3]
a, b, c = cool_trick
>>> a
1
>>> c
3
#===============================
obj_list.append()# TO ADD SOMETHING TO LIST
or
obj_list+=list_nema["___"]
obj_list.remove()# TO REMOVE SOMETHING FROM LIST
obj_list.count(value) #how many times the value in the list
obj_list.sort() #SORT LIST , IT WILL UPDATE THE LIST TO THE SORTED ORDER
ma(obj_list) #MAX VALUE IN THE LIST
sorted(obj_list) #create new list with sorted oredered values
sorted(obj_list,key=len) # create new sorted list order by the key value (ex:len,asc)
"obj_in_list" in list # check if value in list or not
=============================================================================
FOR:

animal_sounds=[["bear","roar"],["dog","hav"],["deer","bellow"]]

for item in animal_sounds:
    print ("the sound a "+item[0] + " makes:\t"+ item[1])

animal="giraffe"
for letter in animal:
    print (letter.upper())


>>> nums = [0,1,2,3,4]
>>> for num in nums:
...     print num

for num in range (9,2,-1): #range(start,stop,step) range(5) will proint 0 till 4

    print (num)

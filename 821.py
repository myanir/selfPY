#https://www.youtube.com/watch?v=yVGSeRcQfyI
#string formatting
#https://pyformat.info/

data = ("self", "py", 1.543)
format_string = "Hello"

print(format_string  + " %s %s learner, you have only %3.1f units left before you master the course!" %data)

#Hello self.py learner, you have only 1.5 units left before you master the course!
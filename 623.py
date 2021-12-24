"""print odd variable(from input zugi) from the list add , and add the last word"""
def format_list(my_list):
    zugi_last = (seperator.join(my_list[::2]+[my_list[-1]]))
    return zugi_last

my_list = ["hydrogen", "helium", "lithium", "beryllium","boron", "magnesium"]
seperator=", "
x=format_list(my_list)
print(x)

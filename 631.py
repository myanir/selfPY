#check is lists are equal
def are_lists_equal(list1, list2):
    list1a=sorted(list1)
    list2a=sorted(list2)
    return (list1a==list2a)

list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
y=are_lists_equal(list1, list2)
print(y)
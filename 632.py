#which value in the list in the longest
def longest(my_list):
    longest_string = max(my_list, key=len)
    print(longest_string)
    return None



list1 = ["111", "234", "2000", "goru", "birthday", "09"]
longest(list1)
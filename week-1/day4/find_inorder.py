import unittest
def contains(ordered_list, number):
    i = 0
    length =len(ordered_list) - 1;
    while (i <= length):
        temp = i + (length-i)/2
        if ordered_list[temp] == number :
            return True
        if ordered_list[temp] < number :
            i = temp + 1
        else:
            length = temp- 1;
        

    return False





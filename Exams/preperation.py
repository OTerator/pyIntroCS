# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 23:37:12 2025

@author: Ori
"""

#1
def has_digit(n, snum):
    
    return snum in list(str(n))

# print(has_digit(1234, "5"))
# print(has_digit(12034, "0"))


#2
def rec_has_digit(n, snum):
    
    if n<10:
        return n == int(snum)
    
    return rec_has_digit(n//10, snum) or n%10 == int(snum)



def rec_has_digit2(n, snum):
    
    if n<10:
        return n == int(snum)
    elif n%10 != int(snum):
        return rec_has_digit(n//10, snum)
    
    
# print(rec_has_digit2(1234, "5"))
# print(rec_has_digit2(12034, "0"))



#3
def int_to_str(n):
    
    nstring = str(n)
    
    if len(nstring) <= 3:
        return nstring
    
    return int_to_str(n//1000) + "," + str(n-(n//1000)*1000)

# print(int_to_str(1234567876543))
    



#4
def remove_from_list(l, x, m, n):
    
    if m >= n:
        if l[m] == x:
            l.pop(m)
            return 1
        return 0
    
    if l[n-1] == x:
        l.pop(n-1)
        return remove_from_list(l, x, m, n-1) + 1
    
    return remove_from_list(l, x, m, n-1)

    
def mainx():
    lst = ['a', 2, 1, 'x', 7, 9, 2, 2, 1, 6, 2]
    lst2 = [0, 1, 2, 9, 9, 9, 1, 2, 9, 1, 2, 9, 1, 2, 9, 9, 9]
    
    # print(remove_from_list(lst, 2, 0, 10))
    # print(lst)
    
    print(remove_from_list(lst2, 9, 3, 16))
    print(lst2)
    
# mainx()



#5
def sort_by_first(mat):
    
    
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 08:53:09 2025

@author: Ori
"""

#1
def flatList(lst):
    
    if not lst:
        return list()
    
    return lst[0] + flatList(lst[1:])

# print(flatList([[1], [2,3], [4]]))


#2
def findInList(lst, n):
    
    if not lst:
        return -1
    
    if lst[0] == n:
        return 0
    
    tmp = findInList(lst[1:], n)
    
    return -1 if tmp == -1 else tmp+1

# print(findInList([1, 2, 3, 4, 5, 6], 4))
# print(findInList([1, 2, 3, 4, 5, 6], 7))


#3
def isDivBy3(n):
    
    n = -n if n<0 else n #absolute value
    
    if n<10:
        return n in {0, 3, 6, 9}
    
    else:
        n = n//10 + (n - (n//10)*10)
        #   n//10 + last digit
    
    return isDivBy3(n)

# print(isDivBy3(126)) 
# print(isDivBy3(127))
# print(isDivBy3(9999999999))   
# print(isDivBy3(-123))



#4
'''unfinished'''
# def permutationsInserter(char, s): # ('a', "bc")
    
#     if not lst:
#         return list()
    
#     return [] permutationsInserter(char, s)
    
    

# def permutations(s):
    
#     if len(s) == 1:
#         return [s]
    
#     return permutations(s[1:])
    

#7
def numPairs(lst, target):
    
    if len(lst) < 2:
        return 0
    
    first = sum([1 if lst[0] + x == target else 0 for x in lst[1:]])
    
    return first + numPairs(lst[1:], target)

# print(numPairs([1, 2, 3, 4, 5], 6))
# print(numPairs([3, 4, 1, 7, 6, 2], 7))
# print(numPairs([2, 4, 1, 5, 13, 2, 8, 7], 9))

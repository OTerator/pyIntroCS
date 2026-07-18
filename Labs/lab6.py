# -*- coding: utf-8 -*-
"""
Created on Tue May 13 09:06:09 2025

@author: Ori
"""

#1
def rangeList(n):
    
    return [i for i in range(n)]

# print(rangeList(21))


#2
def squaredRangeList(n):
    
    return [i**2 for i in range(n)]

# print(squaredRangeList(15))


#3
def multiplyLists(lst1, lst2):
    
    return [lst1[i]*lst2[i] for i in range(len(lst1))]

# print(multiplyLists([1,2,3], [4,5,6]))


#4
def mod_n_only(lst, n):
    
    return [i for i in lst if i%n == 0]

# print(mod_n_only([1, 2, 3, 4, 5, 6, 7], 3))


#5
def wordLenList(s, w):
    
    sLst = s.split()
    return [len(i) for i in sLst if(i != w)]

# print(wordLenList("the quick brown fox jumps over the lazy dog", "the"))


#6
def maxList(lst1, lst2):
    
    return [max(a, b) for a, b in zip(lst1, lst2)]

# print(maxList([2, 1, 2, 1, 5, 9], [1, 2, 1, 2, 8, 7]))


#7
def even_or_odd(lst):
    
    return ["even" if i%2 == 0 else "odd" for i in lst]
    
# print(even_or_odd([1,2,3,4]))


#8
def palindromicWords(lst):
    
    return [s for s in lst if(s[::-1]==s)]

# print(palindromicWords(["madam", "racecar", "apple", "noon"]))


#9
def howManyBelow(lst, treshold):
    
    determination = [1 if i < treshold else 0 for i in lst]
    return sum(determination)

print(howManyBelow([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))


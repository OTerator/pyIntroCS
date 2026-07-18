# -*- coding: utf-8 -*-
"""
Created on Sun May 18 23:20:21 2025

@author: Ori
"""

#1
empty = []
# print(type(empty))


#2
lst = ['a', 2, 3, 7, "b"]
# print(lst)


#3
# print(len(lst))


#4
def countEvens(n):
    #return a list with all even numbers from 1 to n.
    
    return [i for i in range(1, n+1) if i%2 == 0]

# print(countEvens(50))


#5
def cutLst(lst):    
    return lst[::2]

# print(cutLst(lst))

#6
def calculation(lst1, lst2, lst3):
    
    nSum = sum(lst1) + sum(lst2) + sum(lst3)
    print("sum =", nSum)
    
    MultLst = [lst1[i]*lst2[i]*lst3[len(lst3)-(i+1)] for i in range(len(lst1))]
    
    newLst = []
    for i in range(len(lst1)):
        newLst += [lst1[i], lst2[i], lst3[i]]
    
    return newLst, MultLst
    
    
print(calculation([1,2,3], [4,5,6], [7,8,9]))
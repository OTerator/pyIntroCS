# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 08:54:49 2025

@author: Ori
"""
import random

def leftRtn(lst):
    
    lst.append(lst.pop(0))
    return lst
    
def rightRtn(lst):
    
    lst.insert(0, lst.pop())
    return lst


#1
def div_by_n_only_ver_1(lst, n):
    
    newLst = []
    
    for i in lst:
        if i % n == 0:
            newLst.append(i)
        
    return newLst

#2
def div_by_n_only_ver_2(lst, n):    
    
    i = 0
    while (i < len(lst)):
        if lst[i] % n != 0:
            lst.pop(i)
            continue
        i += 1
            
        
#4
def closest_to_target(lst, target):

    d = target - lst[0]
    closest = lst[0]

    for i in lst:
        check = target - i
        if (abs(check) < abs(d)): #closer
            d = check
            closest = i
            
    return closest


#5
def mergeSortedLists(lst1, lst2):
    """recieves lists of integers sorted by values and combines all 
    into one sorted list"""
    
    sortedList = []
    i = 0
    j = 0
    
    while (i < len(lst1) and j < len(lst2)):
        if lst1[i] < lst2[j]:
            sortedList.append(lst1[i])
            i += 1
        else:
            sortedList.append(lst2[j])
            j += 1
    sortedList += lst1[i:]
    sortedList += lst2[j:]
        
    return sortedList

#6
def digit_counter(lst):
    
    digitCounts = []
    
    for i in range(10):
        counter = 0
        for j in lst:
            if (i == j):
                counter += 1
        digitCounts.append(counter)
            
    return digitCounts
  
      
#7
def cyclic_shift_list():
    
    size = int(input("Please enter size: "))
    newLst = []
    
    for i in range(size):
        newLst.append(random.randint(0, 99))
    print("Random list:", newLst, "\n")
    
    newLst = [1, 2, 3, 4, 5]
    print("Temporary", newLst)
    
    steps = -1
    while(steps != 0):
        steps = int(input("PLease enter steps: "))
        
        if(steps > 0):
            for s in range(steps):
                rightRtn(newLst)
                
        elif(steps < 0):
            for s in range(0, steps, -1):
                leftRtn(newLst)
                
        else:
            print("bye!");
            continue;
            
        print(newLst)


#8
def flatten_nested_lst(lst):
    
    flattenedLst = []
    
    for i in lst:
        
        for j in i:
            flattenedLst.append(j)
            
    
    return flattenedLst


#list comprehension
def flattenLst(lst):
    
    return [j for i in lst for j in i]
#gg


#9
def makeLst(n):
    
    nLst = []

    for i in range(1, n+1):
        
        tempLst = [j+1 for j in range(i)]
        nLst.append(tempLst)

    return nLst


def main():
    
    # l = [1, 2, 3, 4]
    # print(rightRtn(l))
    # l2 = ["a", 'b', 'c', 'd']
    # print(leftRtn(l2))
    
    # l = [1, 2, 3, 4, 5, 6, 7]
    # print(div_by_n_only_ver_1(l, 3))
    # print(l)
    # print("----")
    # print(l)
    # div_by_n_only_ver_2(l, 3)
    # print(l)
    
#5
    # print(closest_to_target([1, 3, 7, 10, 14], 9))

#6
    #print(digit_counter([0, 1, 2, 0, 0, 6, 7, 1]))

#7
    #cyclic_shift_list()
    
#8
#     fl = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     print(flattenLst(fl))
    
#     fn = [[1, 2, 3], [4], [5, 6], 7, 8, 9]
#     print(flatten_nested_lst(fl))
    
#9    
    
    print(makeLst(10))
    
    # l1 = [1, 3, 5]
    # l2 = [2, 4, 6, 8, 9]
    # print(mergeSortedLists(l1, l2))
    
main()

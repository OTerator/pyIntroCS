# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 15:17:04 2025

@author: Ori
"""

def merge(sorted1, sorted2):
    
    i, j = (0, 0)
    
    sortedLst = []
    
    for k in range(len(sorted1)):
        minVal = 0
        if sorted1[i] < sorted2[j]:
            minVal = sorted1[i]
            i += 1
        else:
            minVal = sorted2[j]
            j += 1
            
        sortedLst.append(minVal)
        
    if j < len(sorted2):
        sortedLst.append(sorted2[j:])
    else:
        sortedLst.append(sorted1[i:])
    
    return sortedLst


def mergesort(lst):
    if len(lst) <= 1:
        return lst
    
    return merge(mergesort(lst[:len(lst)//2]), mergesort(lst[len(lst)//2:]))


print(mergesort([48,8,4,23,84,3,-2,8,5]))
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 11:09:04 2025

@author: Ori
"""

def find_multiple_indices(lst, n):
    
    return [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] % n == 0]

# print(find_multiple_indices([[1,2,3],[4,5]], 2))




def is_uniform(lst):
    
    vals = [sum([int(c) for c in s]) for s in [str(n) for n in lst]]
    vals2 =[sum(int(c) for c in str(n)) for n in lst] #[22,111,3] -> sum()
    # print(vals2)
    
    return len(set(vals)) == 1


print(is_uniform([21, 111, 3]))
#gg
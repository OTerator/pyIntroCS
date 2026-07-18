# -*- coding: utf-8 -*-
"""
Created on Mon May 12 14:44:57 2025

@author: Ori
"""

def addlst(lst1, lst2):
    
    return [lst1[i]+lst2[i] for i in range(len(lst1))]


lst1 = [1, 2, 3, 4]
lst2 = [3,5,7,9]

print(addlst(lst1, lst2))
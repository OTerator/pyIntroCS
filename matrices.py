# -*- coding: utf-8 -*-
"""
Created on Mon May 12 15:53:13 2025

@author: Ori
"""

import numpy as np


def indexMatrice(n):
    
    return np.matrix([[n*i + j for j in range(n)] for i in range(n)])

print(indexMatrice(4))




def main():
    a = [[2,3,5], [4,-1,7], [5,10,8]]
    
    r1 = a[0]
    r2 = a[1]
    r3 = a[2]
    
    print(a == [r1, r2, r3])
    
    for i in range(len(a)):
        print (a[i] [i], end = ' ')
    
    
    sum = 0
    for i in range(len(a)):
        sum += a[i] [i]
    print (sum)
        
# main()
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 16:21:57 2025

@author: Ori

מועד א תשפג
"""                 

import numpy as np


def makeMat(n):
    
    return [list(range(i, i+n)) for i in range(1, n**2+1, n)]

# print(makeMat(2))


def swap(mat, p1, p2):
    temp = mat[p1[0]][p1[1]]
    mat[p1[0]][p1[1]] = mat[p2[0]][p2[1]]
    mat[p2[0]][p2[1]] = temp



def reverseDia(mat):
    
    n = len(mat[0])
    for i in range(n//2):
        swap(mat, (i, i), (n-1-i, n-1-i))

# test = makeMat(11)
# print(np.matrix(test))

# reverseDia(test)
# print(np.matrix(test))


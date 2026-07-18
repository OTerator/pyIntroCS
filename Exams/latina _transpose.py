# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 09:20:12 2025

@author: Ori
"""


def transpose(mat):
    
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]

mtrx = [[1,2,3], [4,5,6]]
print(transpose(mtrx))


def is_latin(m):
    
    mTrans = transpose(m)
    
    maxVal = max(len(m), len(mTrans))
    
    
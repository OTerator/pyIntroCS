# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 12:07:57 2025

@author: Ori
"""

def avg(mat):
    
    n = len(mat)
    valsum = 0
    
    for row in mat:
        valsum += sum(row)
        
    return valsum / n**2



def maxMatrix(mat_lst):
    
    max_avg = 0
    
    for mat, i in mat_lst.enumarte():
        avg_val = avg(mat)
        if max_avg < avg_val:
            max_avg = avg_val
            max_i = i
            
    return max_i
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 09:54:23 2025

@author: Ori
"""

def dim(m_dict): # {0:[(1,2)], 2:[(0,7), (2,3)], 3:[(2,6)]}
    
    rows = max(m_dict) + 1
    max_col = 0
    
    for v in m_dict:
        if max(m_dict[v]) > max(m_dict[max_col]):
            max_col = v
    
    return rows, max_col


# print(dim({0:[(1,2)], 2:[(0,7), (2,3)], 3:[(2,6)]}))



def unfold(m_dict):    # {0:[(1,2)], 2:[(0,7), (2,3)], 3:[(2,6)]}
    
    rows, columns = dim(m_dict)
    new_mat = [[0 for j in range(columns)] for i in range(rows)]
    
    for k in m_dict: # k=key=row
        for tup in m_dict[k]: #(col,num)
            new_mat[k][tup[0]] = tup[1]
    
    return new_mat


# print(unfold({0:[(1,2)], 2:[(0,7), (2,3)], 3:[(2,6)]}))



def fold(mat):
    
    return {k:[(col, val) for col, val in enumerate(row) if val != 0] for k, row in enumerate(mat) if sum(row) != 0}


print(fold(unfold({0:[(1,2)], 2:[(0,7), (2,3)], 3:[(2,6)]})))

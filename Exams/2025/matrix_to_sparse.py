# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 09:02:30 2025

@author: Ori
"""

# 3 (5)
def matrix_to_sparse(txt):
    
    try:
        file = open(txt)
        text = file.readlines() # ['0 0 3 0\n', '0 0 0 0\n', '5 0 0 8\n', '0 0 0 0']
        file.close()
    except:
        print(f"{txt} was not found.")
        return
    
    
    string_rows = [s.strip('\n') for s in text]
    string_mat = [s.split() for s in string_rows]
    mat = [[int(s) for s in row] for row in string_mat]
    
    mat_dict = {i:{j:k for j, k in enumerate(mat[i]) if k != 0} for i in range(len(mat)) if sum(mat[i]) != 0}
    
    return mat_dict, len(mat)

# print(matrix_to_sparse("mat.txt"))
# print(matrix_to_sparse("mat2.txt"))
# print(matrix_to_sparse("mat3.txt"))


def empty_rows_indices(txt):
    
    mat_dict, rows = matrix_to_sparse(txt)
    
    return [i for i in range(rows) if i not in mat_dict.keys()]
    
    
print(empty_rows_indices("mat.txt"))


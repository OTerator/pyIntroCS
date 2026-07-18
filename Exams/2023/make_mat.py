# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 19:01:37 2025

@author: Ori
"""

def make_mat(n):
    
    return [[i*n + j for j in range(1, n+1)] for i in range(n)]


def reverse_diagonal(mat):
    
    n = len(mat)
    
    for i in range(n//2):
        
        mat[i][i], mat[n-i-1][n-i-1] = mat[n-i-1][n-i-1], mat[i][i]
        
        
def main():
    
    usr_input = int(input("Enter a size for the square matrix: "))
    
    matrix = make_mat(usr_input)
    
    reverse_diagonal(matrix)
    
    print(matrix)
    
main()

# 0 1 2 3 4 5 6
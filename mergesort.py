# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 13:23:42 2025

@author: Ori
"""


def rec_sum(lst):
    
    if len(lst) == 0:
        return 0
    return rec_sum(lst[1:]) + lst[0]


def rec_sum_half(lst):
    
    if len(lst) == 0:
        return 0
    
    
    


def rec_sum_h(lst, left, right):
    
    if left >= right:
        return 0
    
    return lst[left] + rec_sum_h(lst, left + 1, right)


def merge(A, B):
    m = len(A); n = len(B)
    C = [0 for i in range(m+n)]
    i=0; j=0; k=0;
    
    while i<m and j<n:
        if A[i] < B[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
        k += 1
    C[k:] = A[i:] + B[j:] # append remainder, as one is empty anyways.
    
    return C
    


def mergesort(lst):
    
    n = len(lst)
    if n<=1:
        return lst
    
    A = mergesort(lst[:n//2])
    B = mergesort(lst[n//2:])
    C = merge(A, B)
    
    return C

# O(n log2(n)) complexity is great  :)
z
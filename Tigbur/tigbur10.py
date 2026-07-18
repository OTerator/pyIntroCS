# -*- coding: utf-8 -*-
"""
Created on Mon May 26 16:10:54 2025

@author: Ori
"""





def binarySearchHelper(arr, num, start, finish):
    
    mid_i = start + (((finish - start) // 2)+1)
    
    
    if arr[mid_i] == num:
        return mid_i
    if start >= finish:
        return -1
    if num > arr[mid_i]:
        return binarySearchHelper(arr, num, mid_i, finish)
    
    return binarySearchHelper(arr, num, mid_i, finish)


def binary_search(arr, num):
    return binarySearchHelper(arr, num, 0, len(arr)-1)

print(binary_search([-3, 0, 1, 5, 7, 8, 90], 1))
# -*- coding: utf-8 -*-
"""
Created on Mon May 19 14:33:05 2025

@author: Ori
"""

def lesson():
    
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    
    i = (len(l)//2)-1
    print(l[i::-1] + l[:i:-1])
    
# lesson()

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
arr = [7, 5, 8, 1, -3, 90, 0]
# swap(arr, 2, 3)
print(arr)

def bubbleSort(arr):
    
    for i in range(len(arr)-1):    
        for j in range(len(arr)-1-i):
            if(arr[j] > arr[j+1]):
                swap(arr, j, j+1)    
    

# print(bubbleSort(arr))


def bubbleSortV2(arr, n):
     
    if n == 1:
        return
    
    for i in range(n):
        if(arr[i] > arr[i+1]):
            swap(arr, i, i+1)
    print(arr)
    bubbleSortV2(arr, i)


# bubbleSortV2(arr, len(arr)-1)
# print(arr)

def selectionSortV1(arr):
    
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if(arr[j] > arr[j+1]):
                swap(arr, j+1, j)
                
selectionSortV1(arr)
print(arr)


def minIndexOfArray(arr, startingIndex):
    
    minIndex = 0
    minValue = arr[startingIndex]
    for i in range(startingIndex, len(arr)):
        if minValue > arr[i]:
            minValue = arr[i]
            minIndex = i
    return minIndex

# print("min index =", minIndexOfArray(arr, 0))


def selectionSortRec(arr, startingIndex):
    print(startingIndex)
    if startingIndex == len(arr):
        return
    
    minIndex = minIndexOfArray(arr, startingIndex)
    swap(arr, startingIndex, minIndex)
    print(arr)
    selectionSortRec(arr, startingIndex + 1)

# selectionSortRec(arr, 0)
# print(arr)
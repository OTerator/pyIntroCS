# -*- coding: utf-8 -*-
"""
Created on Tue May 20 09:53:42 2025

@author: Ori
"""
import numpy as np

indexMat = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# matrix (m x n) m - rows, n - columns.

#1
def getRow(mat, m):
    return mat[m]

# print(getRow(indexMat, 1))


#2
def getCol(mat, n):
    return [mat[i][n] for i in range(len(mat))]

# print(getCol(indexMat, 1))


#3
def getMainDia(mat):
    '''assume mat is a Square Matrix'''
    
    return [mat[i][i] for i in range(len(mat))]

# print(getMainDia(indexMat))


#4
def getSecDia(mat):
    '''assume mat is a Square Matrix'''
    
    return [mat[i][len(mat)-1-i] for i in range(len(mat))]

# print(getSecDia(indexMat))


#5  #generates a square 0 matrix of order 'n' given. 
def makeZeroMat(n): #Square mat in R^n
    return [[0 for j in range(n)] for i in range(n)]

# print(np.matrix(makeZeroMat(3)))

  
#6
def makeMatrix2(n):     #Square mat in R^n
    return [[j for j in range(n)] for i in range(n)]

# print(np.matrix(np.matrix(makeMatrix2(3))))


#7
def createIndexMatrix(n): #Square mat in R^n
    return [[n*i+j for j in range(n)] for i in range(n)]

# print(np.matrix(createIndexMatrix(3)))


#8
def makeMultTable(n):
    return [[i*j for j in range(1, n+1)] for i in range(1, n+1)]

# print(np.matrix(makeMultTable(3)))


#9
def makeIdentityMat(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

# print(np.matrix(makeIdentityMat(3)))


#10
def makeNestedLst(n):
    
    return [[j+1 for j in range(i)] for i in range(1, n+1)]

# print((makeNestedLst(5)))


#11
def flattenMatrix(mat):
    return [mat[i][j] for j in range(len(mat[0])) for i in range(len(mat))]

print(flattenMatrix(indexMat))
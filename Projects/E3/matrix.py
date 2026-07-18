# -*- coding: utf-8 -*-
"""
Student: Ori Almog
ID: [redacted]
Assignment no. 3
Program: matrix.py

"""

def transposeMatrix(mtrx):  
# composes a list of nested lists containing elements of 
# 'the same row' (shared indexes) from the original matrix.

    return [[row[col] for row in mtrx] for col in range(len(mtrx[0]))]



def multMatrix(m1, m2):
# i is determined by the length of each row in m1; iterating row-by-row of in m1, 
# multiplying by each column in m2 (k).
# j = columns in m1 = rows in m2, and is responsible for the most-inner iteration:
# going through each row of m1 (by iterating through the element's column index: m1[i][start of the row -> end])
# and each column of m2 accordingly (iterating through the element's column index: m1[start of the row -> end][k]))

    return [[sum([m1[i][j] * m2[j][k] for j in range(len(m1[0]))]) for k in range(len(m2[0]))] \
              for i in range(len(m1))] 



def printMatrix(mtrx):
# prints a space-formatted version of the matrix. since the highest given amount of digits is 3, if we count a 
# negative sign aswell the greatest possible string length per number would be 4, hence; between two integers 
# we have at least 2 spaces and if all are positive, 3 or more up to 5.

    for row in mtrx:
        for n in row:
            print(n, end = " "*(6-len(str(n))))
        print()



def main():
    
    file = open("matrices.txt", mode = 'r')
    text = file.readlines()
    file.close()
    
    cleanTxt = [s.strip() for s in text]
    
    mtrxA = []
    mtrxB = []
    currentMatrix = mtrxA
    cleanTxt.remove(cleanTxt[0])
    
    for line in cleanTxt:
        
        try:
            currentMatrix += [[int(s) for s in line.split()]]
            
        except ValueError:
            if line.__contains__("="):
                currentMatrix = mtrxB
    
    mtrxAB = multMatrix(mtrxA, mtrxB);
    printMatrix(mtrxAB)
    print()
    printMatrix(transposeMatrix(mtrxAB))

main()
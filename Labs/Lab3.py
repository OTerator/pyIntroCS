# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 08:53:51 2025

@author: Ori
"""

def starRectangle(n_Columns, m_Rows):
    
    for iRow in range(n_Columns):
        
        for jColumn in range(m_Rows):
            print("*", end ="")
            
        print("")


def signRectangle(n, m, sign):
    
    for i in range(n):
        
        for j in range(m):
            print(sign, end ="")
            
        print("")


            
def signFrame(n, m, sign):
    
    for i in range(1, n+1):
        
        for j in range(1, m+1):
            
            if (i == 1 or i == n):
                print(sign, end = "")
                
            else:
                
                if(j == 1 or j == m):
                    print(sign, end = "")
                    
                else:
                    print(" ", end = "")
        print("")
        


def multiTable(size):
    
    for i in range(1, size+1):
        
        print("")
        
        for j in range(1, size+1):
            print(i * j, end = "\t")


"5"
def triangleV1(n):
    
    for i in range(n+1):
        print(i*"*")
        
        
"6"
#א#
def triangleV2(n):
    
    for i in range(n+1):
        print(i*"*")

    while (i != 0):
        i -= 1
        print(i*"*")

def triangleV2_2(n):
    
    for i in range(n+1):
        print(i*"*")
    
    for i in range(n-1, 0, -1):
        print(i*"*")
   
    

#ב#
#case
def triangleNumsFunnyInverse(n):
    
    for i in range(1, n+1):
        
        for j in range(0, i):
            print(i-j, end = "")
        print("")
        
#fix
def triangleNums(n):
    
    for i in range(1, n+1):
        
        for j in range(i, 0, -1):
            print(i+1-j, end = "")
        print("")



#ג#
#case
def triangleNumsInverseFlipped(n):
    
    for i in range(n, 0, -1):
        
        for j in range(i):
            print(n-j, end = "")
        print("")

#fix
def triangleNumsInverse(n):
    
    for i in range(1, n+1):
        
        for j in range(i):
            print(n-j, end = "")
        print("")



#ד#
def funnyCurveStars(n):
    
    for i in range(n, 0, -1):
        
        for j in range(n+1):
            
            if (j < i):
                print(" ", end = "")
            else:
                print("*", end = "")
                print((j-i)*"*", end = "")
        print("")
        
        
        
def triangleStars(n):
    
    for i in range(n, 0, -1):
        
        for j in range(n+1):
            
            if (j < i):
                print(" ", end = "")
            else:
                print("*", end = "")
        print((j-i)*"*", end = "")
        print("")
        

def identityMatrix(n):
    
    for i in range(n):
        
        for j in range(n):
            
            if (i==j):
                print(1, end=" ")
            else:
                print(0, end=" ")
        print("")
                
    
#8    
def evenCount(lst):
    
    cnt = 0
    
    for i in lst:
        
        if (i%2 == 0):
            cnt += 1
    
    return cnt


#9א#
def maxNum(lst):
    
    return max(lst)


def myMax(lst):
    
    nMax = lst[0]
    for i in lst:
        
        if (i > nMax):
            nMax = i
    
    return nMax


#10א#
def sumNum(lst):

    return sum(lst)    

    
def mySum(lst):
    
    nSum = 0
    for i in lst:
        nSum += i
        
    return nSum


#11
def multiplyLists(lst1, lst2):
    
    if (len(lst1) != len(lst2)):
        return "List lengthes are not equal"
    
    newList = []
    
    for i in range(len(lst1)):
        newList.append(lst1[i]*lst2[i])
    
    return newList
            
    
#12
def divisibleElements(lst, n):
    
    nLst = []
    
    for i in lst:
        if (i%n == 0):
            nLst.append(i)
            
    return nLst

#13
def allDivsblUnder1k(n):
    
    if (n<1 or n>100):
        return "input range 1 - 100"
    
    lstOneK = []
    for i in range(1, 1001):
        lstOneK.append(i)
    
    return divisibleElements(lstOneK, n)
        
    

#main    
def main():
    
    #starRectangle(3, 6)
    #signRectangle(3, 6, "$")
    #signFrame(3,6,"!")
    multiTable(4)
    #triangleV2_2(5)
    #triangleNums(5)
    #triangleNumsInverse(5)
    #triangleStars(5)
    #identityMatrix(4)
    l = [100,2,300,-4,55,6,7,800,-9,10,0,0]
    #print(evenCount(l))
    #print(maxNum(l))
    #print(myMax(l))
    #print(sumNum(l))
    #print(mySum(l))
    l2 = [10,0.5,0.5,-1,0.2,2,1,0.01,1,-5,100,69]
    l3 = [1,2,3]
    l4 = [4,5,6]
    #print(multiplyLists(l3, l4))
    #print(multiplyLists(l,l2))
    l3 = [2,3,7,5,6,4]
    #print(divisibleElements(l3, 3))
    # print(allDivsblUnder1k(2))
    

main()    

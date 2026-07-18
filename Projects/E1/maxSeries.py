# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 18:20:22 2025

@author: Ori

Student: Ori Almog
ID: [redacted]
Assignment no. 1
Program: maxSeries.py

"""

def maxSeries():
    
    """
    This function repetitively recieves integer inputs from the user until 0 is given.
    Once done, it prints:
        - Average of all integers (not including the final 0)
        - Max value and its cell number
        - Min value and its cell number
        
    """
    
    nextInt = int(input("Enter numbers, 0 to stop: \n"))
    
    if (nextInt == 0):
        print("average = 0")
        print("max value - none.")
        print("min value - none.")
        return
    
    intCount = 1
    intSum = nextInt
    
    maxInt = nextInt
    maxCell = 1
    
    minInt = nextInt
    minCell = 1
        
    
    while(nextInt != 0):
        
        if (maxInt < nextInt):
            maxInt = nextInt
            maxCell = intCount
            
        elif (minInt > nextInt):
            minInt = nextInt
            minCell = intCount        
            
        nextInt = int(input())
        intCount += 1
        intSum += nextInt
    
    
    intAverage = intSum / (intCount -1)
    
    print("average =", intAverage)
    print("max value is", maxInt, "in cell", maxCell)
    print("min value is", minInt, "in cell", minCell)    
    

def main():
    
    maxSeries()
    
    
main()

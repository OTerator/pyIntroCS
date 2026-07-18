# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 00:07:20 2025

@author: Ori

Student: Ori Almog
ID: [redacted]
Assignment no. 1
Program: decSeries.py

"""

def decSeries(N):
    
    """ 
    This program recieves 'N' numbers in the order they are given
    and checks for a decending series (on a consistent streak).
    Each iteration increases the count if the series continues to decrease, and otherwise, restarts while
    keeping track of the longest streak to count.
        
    By definition, considering a decending series cannot have only one component, we first count both compared 
    components at once, and only then proceed to increase their count by one/restart the current count.
    
    """
    
    currentStreak = 0
    longestStreak = 0
    currentNum = int(input())
    lastNum = currentNum
    
    for i in range(1, N):
        
        currentNum = int(input())
        
        if (currentNum < lastNum):
            
            if (currentStreak == 0):
                currentStreak = 1
                
            currentStreak += 1
                
            if (currentStreak > longestStreak):
                longestStreak = currentStreak
            
        else:
            currentStreak = 0
        
        lastNum = currentNum
    
        
    print("Longest streak count =", longestStreak)
            

def main():
    
    decSeries(10)
    

main()

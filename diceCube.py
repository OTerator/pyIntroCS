# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 14:37:10 2025

@author: Ori
"""
import random

def cube(n, m):
    
    mCount = 0
    for i in range(n):
        p = random.randint(1, 6)
        print(p)
        if (p == m):
            mCount += 1
            
    return mCount

def main():
    
    print("cnt = ", cube(int(input("Amount of Iterations: ")), (int(input("int between 1-6: ")))))

main()
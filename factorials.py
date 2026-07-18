# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 14:15:11 2025

@author: Ori
"""

def factorials(high):
    
    factorial = 1
    
    for i in range(1, high + 1):    
        factorial *= i
        print(str(i) + "! = ", factorial)
        
        
def main():
    factorials(50)
    
    
main()
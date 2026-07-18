# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 11:29:37 2025

@author: Ori
"""

def main():
    
    howManyOdd()
    

def howManyOdd():
    
    n1 = int(input("Please enter the first number: "))
    n2 = int(input("Please enter the second number: "))
    n3 = int(input("Please enter the third number: "))
    n4 = int(input("Please enter the fourth number: "))
    
    print(n1%2 + n2%2 + n3%2 + n4%2)
    
    
main()
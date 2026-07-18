# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 14:54:22 2025

@author: Ori
"""

def factorial(n):
    
    if n <= 1:
        return 1
    
    return factorial(n-1) * n

# print(factorial(4))



def loopGcd(a, b):
    
    while a%b != 0:
        a, b = b, a%b
        
    return b




def gcd(a, b):
    
    if a<b :
        return gcd(b, a)
    
    if a%b == 0:
        return b
    
    return gcd(b, a%b)



# print(loopGcd(84, 48))
# print(gcd(84, 48))



def recSum(lst):
    
    if len(lst) == 0:
        return 0
    
    return recSum(lst[1:]) + lst(0)



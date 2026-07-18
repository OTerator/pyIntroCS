# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 17:16:59 2025

@author: Ori
"""

def decompose(n):
    
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return [i] + decompose(n//i)
    
    return [n]


print(decompose(252))
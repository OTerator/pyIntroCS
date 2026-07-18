# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 11:20:46 2025

@author: Ori
"""


def pi(h=0.001):
    
    n = 0
    a_n = ((-1)**n)*(4/(2*n + 1)) # 4
    pi = 0
    
    while abs(a_n) >= h:
        
        pi += a_n
        n += 1
        a_n = ((-1)**n)*(4/(2*n + 1))

    return pi

print(pi())
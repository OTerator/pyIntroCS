# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 14:42:55 2025

@author: Ori
"""

def countDiv(lst, a):
    
    cnt = 0

    for n in lst:
        
        if n % a == 0:
            cnt += 1
            
    return cnt


def main():
    
    l = [1, 2, 3, 4, 5, 6]
    
    print(countDiv(l, 2) )

main()
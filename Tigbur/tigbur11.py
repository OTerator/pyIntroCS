# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 17:51:26 2025

@author: Ori
"""


def power(n, p):
    
    if p == 0:
        return 1
    
    return power(n, p-1) * n


# print(power(2, 9))




def find_ab(s):
    
    if len(s) < 2:
        return 0
    
    first = 1 if s[:2]=='ab' else 0
    
    if len(s) == 2:
        return first
    
    return first + find_ab(s[1:])


print(find_ab("ababababbbaaabaabbb"))

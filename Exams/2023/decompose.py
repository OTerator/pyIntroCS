# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 19:45:33 2025

@author: Ori
"""

def decompose(n):
    
    if n < 1:
        return []
    
    for i in range(2, int(n**0.5)+1):
        
        if n % i == 0:
            return [i] + decompose(n//i)
    
    return [n]


print(decompose(1))


# def decompose(n):
    
#     for i in range(2, int(n**0.5)+1):
        
#         if n % i == 0:
#             return f"{i}*" + decompose(n//i)
    
#     return f'{n}'
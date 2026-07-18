# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 15:22:41 2025

@author: Ori
"""


def reduct(lst):
    
    l = list()
    cntPos = 0
    cntNeg = 0
    
    isPositive = True if l[0] > 0 else False
    
    for n in lst:
        
        if n > 0:
            
            cntPos += 1
            
            if isPositive == False:
                l.append(cntNeg)
                cntNeg = 0
                isPositive = True
        
        else:
            cntNeg -= 1
            
            if isPositive:
                l.append(cntPos)
                cntPos = 0
                isPositive = False
                
    l.append(cntPos) if isPositive else l.append(cntNeg )
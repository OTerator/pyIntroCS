# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 12:38:07 2025

@author: Ori
"""

def reverseList(l):
    
    
    for i in range(len(l)//2):
        j = len(l)-1-i
        l[i], l[j] = l[j], l[i]
        
    print(l)
    
def main():
    
    l = [1,2,3,4,5]
    print(l)
    reverseList(l)
 
main()
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 13:24:08 2025

@author: Ori
"""


def square(n):
    return n*n

def main():
    
    lst = [1, 2, 3, 4, 5]
    
    sqrDict = {x:square(x) for x in lst}
    # print(sqrDict)
    
    sqrLst = list(map(square, lst))
    # print(sqrLst)
    
    
main()
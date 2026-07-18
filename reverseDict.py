# -*- coding: utf-8 -*-
"""
Created on Wed May 21 12:42:01 2025

@author: Ori
"""

#dictionary

eng_spa = {"red":"rojo", "green": "verde", "black":"negro"} 

# print(eng_spa["green"])

d = {'a':1, 'b':2, 'c':3}

# print(d['a'])

def reverseDict(d):
    d2 = {}
    for key in d:
        
        print(d2)
        print(key , d[key])
        d2[d[key]] = key
        print(d2)
        print("-------")
        
    return d2

reverseDict = reverseDict(d)
# print(reverseDict(d))

# print("is", reverseDict[3])


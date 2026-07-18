# -*- coding: utf-8 -*-
"""
Created on Tue May 13 21:00:19 2025

@author: Ori
"""

def makeTri(tStr, h): #recieves the instructing string from the get_string_triangle function.
    
    ci = 0 #Currect Index
    triList = [] #Each index represents a row
    for l in range(h):
        nextRow = ""
        for r in range(h+l):
            nextRow += tStr[ci]
            ci += 1
        triList.append(nextRow)
    
    for r in triList:
        print(r)
        
def main():
    
    print("go open triangle.py from T2")
    # makeTri(get_string_triangle(string, height), height)

main()
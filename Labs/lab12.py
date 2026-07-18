# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 09:01:01 2025

@author: Ori
"""

#1
def subMatrix(mat, i, j):
    
    return[[mat[row][col] for col in range(len(mat[0])) if mat[row][col] != mat[row][j]]\
           for row in range(len(mat)) if mat[row] != mat[i]]
    

# print(subMatrix([[1,2,3], [4,5,6], [7,8,9]], 1, 0))




#2
def joinDict(d1, d2):
    
    dictIntersection = set(d1.keys()).intersection(set(d2.keys()))
    
    return [(d1[c],d2[c]) for c in dictIntersection]

# print(joinDict({10: "dog", 20: 157, 30: "cat", 40: 17}, {5:"apple", 10: 13, 15: "orange", 20: "banana"}))


def isMutual(tpl, d1, d2):
    
    inverse = (tpl[1], tpl[0])
    mutuals = joinDict(d1, d2)
    
    return tpl in mutuals or inverse in mutuals


def test2():
    
    d1 = {10: "dog", 20: 157, 30: "cat", 40: 17}
    d2 = {5:"apple", 10: 13, 15: "orange", 20: "banana"}
    print(isMutual(('dog', 13), d1, d2))
    print(isMutual((13, 'dog'), d1, d2))
    print(isMutual(('cat', 13), d1, d2))
    
# test2()




#3

def getAvrg(grades):
    
    names = {tpl[0].lower() for tpl in grades}
    scores = [[grade[1] for grade in grades if name == grade[0].lower()] for name in names]
    averages = [sum(s)/len(s) for s in scores]
    
    return {name:average for (name,average) in zip(names,averages)}

    
def test3():
    
    l1 = [('Yael',90), ('eli', 85), ('Yosef', 88), ('yael', 95), ('Eli', 80)]
    print(getAvrg(l1))
    
# test3()



#4

def isAnagram(s1, s2):
    
    d1 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0,}
    d2 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0,}
    
    for c in s1:
        d1[c] += 1
    
    for c in s2:
        d2[c] += 1
        
    return d1 == d2

print(isAnagram("silent", "listen"))

# def groupAnagrams(lst):
    
    
    

# -*- coding: utf-8 -*-
"""
Created on Mon May 12 16:54:01 2025

@author: Ori
"""
import random

def main():
    divBy11 = [i for i in range(1, 101) if i%11==0]
    divBy11 = tuple(divBy11)
    print(divBy11) 
#main()


def randTuple(n):
    
    t = tuple()
    for i in range(n):
        t += (random.randint(10, 50),)
    print(t, t[n//2])
    
# randTuple(100)


def charInStr(string):
    chars = tuple()
    for char in string:
        chars += (char,)
    return chars

# print(charInStr("Hello"))


def charInStrReverse(string):
    chars = tuple()
    for char in string[::-1]:
        chars += (char,)
    return chars

# print(charInStrReverse("Hello"))


def f():
    initials = {"Yossi":6, "Dafna":17, "Noam": 26, "Sapir": 26, "Ori": 22}
    initials["Guy"] = 34
    initials["Shimmy"] = 69
    
    print(initials["Noam"])
    print(sum(initials.values())/len(initials.keys()))
    
    for name, age in initials.items():
        print(f"{name}'s age is {age}")

# f()
        
#6
def squaresAndRoots(n):
    
    return {i: (i**2, i**0.5) for i in range(n)}

# print(squaresAndRoots(7))


#Set:
    
#6
def rand30():
    
    return {random.randint(1, 20) for i in range(30)}

# print(rand30())

#8
def uniquePrices(lst1, lst2):
    
    return set(lst1)|set(lst2) #Union

print(uniquePrices([1,2,3] , [2,3,4]))
    
    
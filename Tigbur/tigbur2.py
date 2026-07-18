# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 17:09:49 2025

@author: Ori
"""

def isGreater(x, y):
    
    return x > y


def printEquation(x, y):
    
    if (x > y):
        print("x > y")
        
    elif (x == y):
        print("x = y")
        
    else :
        print("x < y")
    

def compare():
    
    num1 = int(input("Enter num 1: "))
    num2 = int(input("Enter num 2: "))
    
    if num1 != num2:
        return num1*num2
    
    else:
        return num1 + num2
    
    
def totalPrice(entryPrice, childAge):
    
    parentsCost = entryPrice*2
    childCost = entryPrice
    
    if (childAge <= 1):
        childCost *= 0.5
    
    elif childAge > 1 and childAge <= 3:
        childCost *= 0.7
        
    elif childAge < 12:
        childCost *= 0.75
        
    else:
        print("no discount:")
    
    return parentsCost + childCost


#6
def canJump(contestantStep, judgeCap):
    
    if contestantStep % judgeCap == 0:
        print(contestantStep / judgeCap)
        
    else:
        print("can")
        return -1



def main():
    
    print("Total price =", totalPrice(100, 50))
    
    
main()
        
        
        
        
        
        
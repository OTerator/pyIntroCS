# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 19:07:25 2025

@author: Ori
"""

def main(): {
        
        # digitSumSimple()
        
    
        print(newDigitSum())
        
        }

# def digitSumSimple():
    
#     number = int(input("Please enter a 3 digit number of your choice: "))
    
#     n1 = number % 10
#     number //= 10
    
#     n2 = number % 10
#     number //= 10
    
#     n3 = number % 10
#     number //= 10
    
#     nSum = n1 + n2 + n3
#     print(nSum);
    
    
def newDigitSum(nSum):

    number = int(input("Please enter a 3 digit number of your choice: "))

    while (number > 0):
        nSum += number % 10
        number //= 10
    
    return(nSum);

    
    
main()
# -*- coding: utf-8 -*-
"""
Created on Mon May  5 16:43:32 2025

@author: Ori
"""

def a():
        
    lst = [i*j if i*j > 10 else i+j for i in range(9) if i%2 == 0 for j in range(10) if j%3 == 0]
    
    print(lst)
    
def taxedPrice():
    
    tax = 1.17
    
    while True:    
        try:
            price = float(input("Enter a price: "))
            txdPrice = price*tax
            print("After tax:", txdPrice)
            break
        except TypeError:
            print("Error: Input has to be a number.")
  
            
def division(n1, n2):
    
    try:
        n1, n2 = float(n1), float(n2)
    except:
        print("One of the given values is not a number.")
        return
    
    try:
        quotient = n1/n2
    except:
        print("You can't divide by zero.")
        return
    print("quotient =", quotient)
    

def stringSubGroup(string):
    return [char for char in string]


def nRange(infimum, supremum):
    return[n for n in range(infimum, supremum + 1)]


def fstChar(string):
    return[char[0] for char in string.split()]


def rtrnPositiveLst(lst):
    return [n for n in lst if n > 0]


def divisiblesOfEight():
    return [n for n in range(100, 300) if n%8 == 0]


def containsThree():
    return [n for n in range (40, 135) if '3' in str(n)]


def digitsInStr(string):
    return[char for char in string if char.isdigit()]


def startsWithA(lst):
    return [string for string in lst if string[0] == 'A']


def exponentsOfTwo():
    return [2**exponent for exponent in range(15)]


def squaresUptoTen():
    return [n**2 for n in range(1, 11) if n%2 == 0]

def rootsUptoTen():
    return [n**2 if n%2==0 else n**0.5 for n in range(1, 11)]


def isMaximum(n, group):
    return len([maximum for maximum in group if maximum >= n]) == 0



def main():
    
    # taxedPrice()
    # division(input("nominator: "), input("denominator: "))
    # print(stringSubGroup("abcdefghij"))
    # print(nRange(0,50))
    # print(fstChar("oh my god , what the fuck? I don't care"))
    # print(rtrnPositiveLst([-5, 0, 5, 1, 6]))
    
    # print(containsThree())
    # print(digitsInStr("H3llo h0w ar3 you do1ng 2day?"))
    # print(startsWithA(["Aviel", "Ori", "David", "Ahmed"]))
    # print(exponentsOfTwo())
    # print(squaresOfTen())
    # print(rootsUptoTen())
    # print(lesserThan([1, 2, 3, 4], 5))
    
main()
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 17:26:28 2025

@author: Ori
"""

def main():
    
    #calculateParkDiscount(50)
    #studentsParkDiscount(40, 7)

    print("Counting: (Package count, remaining ice creams) =", calculateIceCreamPackages())


def numType():
    
    num = input("Enter a number: ")
    print(type(num))
    
    
def pseudoToPy():
    
    x = int(input("Enter your first integer: "))
    y = int(input("Now the second: "))
    
    print("\nThe difference between the first and the second integers is =", x-y)
    print("Accordingly, their quotient is =", x/y)
    print("And without the remainder =", x//y)
    print("Finally, just the remainder (residual) =", x%y)
    
    
def calculateParkDiscount(ticketPrice):
    
    discountedPrice = 0.8 * ticketPrice
    print("After a 20% discount, the new price is", discountedPrice)
    
    return (discountedPrice)
    
    
def studentsParkDiscount(ticketPrice, studentCount):
    
    discountedStudent = calculateParkDiscount(ticketPrice)
    
    print ("Per", studentCount, "students, the original price is", studentCount * ticketPrice)
    print ("And after discount the new price is", studentCount * discountedStudent)
    
    
def calculateIceCreamPackages(iceCreamCount = int(input("Ice creams to package = "))):
    
    packageCount = iceCreamCount // 20
    remainingIceCreams = iceCreamCount % 20
    
    return (packageCount, remainingIceCreams)
    



def calculateExponent():
    
    base = int(input("Enter a number of choice, for a base: "))
    exponent = int(input("and a second, for its exponent: "))
    
    print("So,", base, "raised by", exponent, "=", base**exponent)
    

main()
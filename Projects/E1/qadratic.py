# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 14:05:18 2025

@author: Ori

Student: Ori Almog
ID: [redacted]
Assignment no. 1
Program: qadratic.py

"""
import math


def quadratic(a, b, c):
    
    """
    Calculates root solutions for quadratic equations (set equal to 0):
        ax^2 + bx + c = 0
        
    With the use of the Quadratic Formula:
        x(1,2) = [-b +-sqrt(b^2 - 4ac)] / 2a
        
    Conditions derived from the formula:
        - 'a' would never be set to 0. (as such case wouldn't be quadratic to begin with,
          but rather from the family set of: " bx+c = 0  =>  x = -c/b ").
        - some expressions may not wield real solutions for x.
        
    """
    
    if (a == 0):
        print("Expression is not a quadratic (a = 0).")
        print("")
        return
    
    discriminant = b**2 - (4*a*c)
    
    if (discriminant < 0):
        print("No solution for x.")
        print("")

    elif (discriminant == 0):
        print("One solution:")
        print(-b / (2*a))
        print("")
            
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        
        print("Two solutions:")
        print(x1, ",", x2)
        print("")
    
    
def main():
    
    """
    The main function, repetitively executes quadratic(a, b, c), until three zeros are given.
    
    """
    
    while(True):
        
        a = float(input("Enter first parameter (a): "))
        b = float(input("Enter second parameter (b): "))
        c = float(input("Enter third parameter (c): "))
        quadratic(a, b, c)
        
        if (a==0 and b==0 and c==0):
            break;
        
    
main()

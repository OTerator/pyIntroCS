# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 18:54:13 2025

@author: Ori
"""

def calculateAge():
    
    currentAge = float(input("Please enter your age: "));
    currentYear = int(input("enter the current year: "));
    futureYear = int(input("enter a future year of choice: "));
    futureAge = currentAge + futureYear - currentYear;
    
    print("in", futureYear, "you'll be", futureAge, "years old");
    
    
calculateAge();

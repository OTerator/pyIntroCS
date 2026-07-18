# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 16:26:24 2025 

@author: Ori

Student: Ori Almog
ID: [redacted]
Assignment no. 1
Program: dice3.py

"""
import random

def dice3(n, k):
    
    """ 
    Rolls 3 dice at once, 'n' times. for each iteration, we check if all 3 landed on the same
    number, in which case - a count for such senario increments by +1.
    in case the count reaches a value of 'k' identical trios, we note the amount of attempts taken.

    """
        
    triple = 0
    
    for i in range(n):
        
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        d3 = random.randint(1, 6)
        
        print(d1, d2, d3)
        
        if (d1 == d2 == d3):
            triple += 1
            
            if (triple == k):
                reach = i+1                 
            
            
    if (triple >= k):
        
        print("Reached", k, "equal series after", reach, "games")
    
    else:
        print("None or less than", k, "equal series have been reached.")
    
    
    
def main():
    
    dice3(int(input("Please enter n: ")), int(input("Please enter k: ")))

main()

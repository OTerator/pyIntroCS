# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 12:44:10 2025

@author: Ori
"""

def stars():
    msg = str(input("Please enter a phrase: "));
    sCount = int(input("Enter how many stars to print"));
    
    print(sCount*"*" + msg + sCount*"*");

stars();
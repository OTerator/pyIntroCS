# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 18:46:15 2025

@author: Ori
"""


def main():
    
    avgThreeNums();


def avgThreeNums():
    
    n1 = int(input("Enter number 1: "));
    n2 = int(input("Enter number 2: "));
    n3 = int(input("Enter number 3: "));
    
    sum = n1 + n2 + n3;
    avg = sum/3
    
    print(avg);    
    
    
main();
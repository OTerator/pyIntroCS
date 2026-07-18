# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 12:46:16 2025

@author: Ori
"""


# fiboDict = {0:1, 1:1}

def hanoi(src, via, target, discs):
    if discs > 0:
        hanoi(src, target, via, discs-1)
        print(src, '--->', target)
        hanoi(via, src, target, discs-1)
        

def main():
    disc_cnt = int(input("Enter a number of discs: "))
    hanoi('A', 'B', 'C', disc_cnt)
    

if __name__ == '__main__':
    main()


# O(2^n) Complexity :(

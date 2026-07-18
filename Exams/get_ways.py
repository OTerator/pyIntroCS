# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 11:39:18 2025

@author: Ori
"""


def getWays(score):
    
    if score < 1:
        return 0
    elif score == 3:
        return 4
    elif score == 2:
        return 2
    elif score == 1:
        return 1


    return getWays(score-1) + getWays(score-2) + getWays(score-3)

# print(getWays(5))
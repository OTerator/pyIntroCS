# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 15:09:38 2025

@author: Ori
"""


def flat(lst):
    
    # if type(lst[0]) != list:
    #     return lst
    
    if not isinstance(lst[0], list):
        return lst
    
    
    return flat(lst[0]) + lst[1:]
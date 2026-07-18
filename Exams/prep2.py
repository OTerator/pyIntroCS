# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 10:41:46 2025

@author: Ori
"""


def get_one_number(lst):
    
    if len(lst) == 1:
        return f"{lst[0]}"
    
    return get_one_number(lst[:-1]) + f"{lst[-1]}"

# print(get_one_number([123, 45, 1111]))
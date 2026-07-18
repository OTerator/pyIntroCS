# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 18:25:00 2025

@author: Ori
"""

# 1
def zero_distance(s):

    return ord(min(s)) - ord('a')

# print(zero_distance('cat'))


def sort_by_zero(strings, d):  # ["cat", "dog", "zebra", "apple", "bat"], 0
    
    for i in range(len(strings)):
        if zero_distance(strings[i]) == d:
            strings.insert(0, strings.pop(i))

            
l1 =["cat", "dog", "zebra","apple", "bat", "doggo", "drago"]
# l2 = ["hello", "world", "zebra", "dog"]
sort_by_zero(l1, 0)
print(l1)
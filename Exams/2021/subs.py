# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 22:11:27 2025

@author: Ori
"""

#2
def count_subs_comprehension(s, subs):
    
    return sum([1 for c in s if c == subs])


def count_subs(s, subs):
    
    if len(s) < len(subs):
        return 0
    
    return (1 if s.startswith(subs) else 0) + count_subs(s[1:], subs)

print(count_subs("Goooood", 'o'))


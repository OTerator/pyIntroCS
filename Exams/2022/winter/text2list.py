# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 23:22:28 2025

@author: Ori
"""


def text2list(txt):
    
    file = open(txt, mode='r')
    text = file.readlines()
    file.close()
    
    return [set(s.split()) for s in [line.strip("\n") for line in text]]

# print(text2list("text.txt"))



def text2dict(txt):
    
    set_lst = text2list(txt)
    # words = {w for w in st for st in set_lst}  # Union of all sets.
    
    words = set()
    for st in set_lst:
        for w in st:
            words.add(w)
    
    # words = {w for st in set_lst for w in st}
    
    # return {[1 for word in st for st in text_lst if w in st else 0] for w in words}
    
    d = dict()
    for w in words:
        for i, st in enumerate(set_lst):
            
            if w in st:
                
                if w not in d:
                    d[w] = {i}
                else:
                    d[w].add(i)    
    return d
    # return {w:{i for word in st for i, s in enumerate(set_lst) if w in s} for w in words}

    
    
print(text2dict("text.txt"))
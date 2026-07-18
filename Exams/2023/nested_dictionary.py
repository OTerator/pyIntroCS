# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 21:30:58 2025

@author: Ori
"""


def nested_dictionary_lookup(data, keys):
    
    temp = data     #  {'a':{'b':{'c':5}, 'd':{'e':{'f':'hello'}}},'g':10}
    
    for k in keys:  # ['a', 'b', 'c']
        
        try:
            if k in temp:
                temp = temp[k]
            else:
                return
        except:
            print("Type error, keys list has redundant indexes.")
            return
    
    return temp

    
def main():
    
    da = {'a':{'b':{'c':5}, 'd':{'e':{'f':'hello'}}},'g':10}
    ks = ['a', 'b']
    
    print(nested_dictionary_lookup(da, ks))

main()
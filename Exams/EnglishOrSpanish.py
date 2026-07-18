# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 14:45:59 2025

@author: Ori
"""


def language(d, s):
    
    lst = s.split()
    cnt = [0, 0, 0]
    for word in lst:
        word = word.lower().strip('.,')
        
        if word.isalpha():
                
            if word in d:
                cnt[0] += 1
            elif word in d.values():
                cnt[1] += 1
            else:
                cnt[2] += 1
            
        if cnt[0]/sum(cnt) > 0.5:
            return "English"
        
        if cnt[1]/sum(cnt) > 0.5:
            return "Spanish"
        
        return "Other"


def main():
    
    while True:
        
        name = input("Enter file name: ")
        
        try:
            file = open(name, mode='r')
            text = file.read()
            file.close()
            
            print(language(eng_spa, text))
            
        except:
            print('Goodbye.')
            break
        
        
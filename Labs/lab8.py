# -*- coding: utf-8 -*-
"""
Created on Tue May 27 08:37:14 2025

@author: Ori
"""

#1
def getSqrTuples(nLst):
    return [(n, n**2) for n in nLst]

# print(getSqrTuples([1, 2, 3, 4, 5, 6, 7]))


#2
def getSqrDict(nLst):
    return {n:n**2 for n in nLst}

# print(getSqrDict([1, 2, 3, 4, 5, 6, 7]))


#3
def m(l):
    for e in l:
        for i in range(len(e)):
            e[i] **= 2

def check3():            
    l1 = [[1,2,3], [4,5,6], [7,8,9]]
    t1 = ([1,2,3], [4,5,6], [7,8,9])
    l2 = [(1,2,3), (4,5,6), (7,8,9)]
    
    m(l1)
    print(l1)
    m(t1)
    print(t1)
    # m(l2) tuples are immutable, error was predicted.
    print(l2)

# check3()



#4
def check4():
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    double_dict1 = {k:v*2 for (k,v) in dict1.items()}
    print(double_dict1)
    dict1_keys = {k*2:v for (k,v) in dict1.items()}
    print(dict1_keys)
    dict1_double_cond = \
    {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0}
    print(dict1_double_cond)
    dict1_triple_cond = \
    {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}
    print(dict1_triple_cond)

# check4()



#5
def numDupCnt():
    
    counters =  dict()
    usrInput = input("Enter a number to count, any other char to stop: ")
    try:
        usrInput = int(usrInput)
    except:
        userInput = "none"
    
    while type(usrInput) == int:
        
        if usrInput not in counters:
            counters[usrInput] = 1
        else:
            counters[usrInput] += 1
            
        usrInput = input("Enter a number to count, any other char to stop: ")
        try:
            usrInput = int(usrInput)
        except:
            userInput = "none"
    
    print(counters)

numDupCnt()



#6
# def swap(c, i, j):
    

def swapTest():    
    lst = [0, 1, 2, 3, 4, 5, 6]
    dic = {0:'a', 1:'b', 3:'c', 4:'d'}
    swap(lst, 1, 4)
    swap(dic, 1, 4)
    
    print(lst, dic, end="\n")
    
# swapTest()



#7
def getWordInf(wordLst):
    dct_res = {}
    vowels = 'aeiou'
    
    for word in wordLst:
        key = word
        # build tuple:
        word_len = len(word)
        vowelCnt = 0
        for c in word:
            if c in vowels:
                vowelCnt += 1
        value = (word_len, vowelCnt)
        dct_res[key] = value
    return dct_res

l = ['apple', 'bannana', 'orange']
# print(getWordInf(l))

def getWordInfV2(wLst):
    vowels = 'aieou'
    return \
        {w:(len(w), sum([1 if c in vowels else 0 for c in w])) for w in wLst}

# print(getWordInfV2(l))
    

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 08:52:44 2025

@author: Ori
"""

#0
def isHidden(s, t, step):
    #checks if t is hidden in s
    
    maxJump = (len(s)-1)/(len(t)-1)
    
    for d in range(1, maxJump+1):
        
        for i in range(d):
            if t in s[i::d]:
                return True
    
    return False;        
    
        

#1
def rotStr(s):
    
    for i in range(len(s)):
        
        print(s)
        
        first = s[0]
        
        remainder = ""
        for j in range(len(s)):
            
            if j == 0: 
                continue
            else:
                remainder += s[j]
                
        s = remainder + first
    


#2
def rotStr2(s):
    
    rLst = []
    
    for i in range(len(s)):
        
        rLst.append(s)
        
        first = s[0]
        
        remainder = ""
        for j in range(len(s)):
            
            if j == 0: 
                continue
            else:
                remainder += s[j]
                
        s = remainder + first
    
    return rLst



#3
def breakCode(string, step):
    
    for i in range(len(string)):
        if(i % step == 0):
            print(string[i], end='')



#4
def reverseSentence_0(string):
    
    subStrings = string.split()
    reversedSub = subStrings[::-1]
    newS = " ".join(reversedSub)
    
    return newS
    

def reverseSentence(string):
    
    subStrings = string.split()    
    
    return " ".join(subStrings[::-1])


def reverseSentence_2(string):
    
    return " ".join(string.split()[::-1])



#5
def finder(strs, splitter='#'):
    
    parts = strs.split(splitter)

    # for .א    
    # ['ATT', 'ATAATAG', 'ATGC', 'GGT', 'GAATT', 'ATTATTGCATGG']
    #    0        1         2      3       4            5
    #    ^        F         F      F       T            T
    
    found = []
    if len(parts) > 1:  # 6>1
        
        for i in range(1, len(parts)):   # 1 -> 6
            if parts[0] in parts[i]:  # {(1,x)E(parts)| is string 1 in x} = 
                                      # (1,6), (2,6), (3,6), (4,6), (5,6)
                found.append(i) # [4] ... [4, 5]
    return found   # [4, 5]



#6
def clean(s):
    
    sClean = ''
    for c in s:
        if c.isalpha():
            sClean += c.lower()
    print(sClean)
    
    return sClean
    
def isPalindrome(s):
    
    s = clean(s) #returns the lowercase latin letters of string, no 
    sFlipped = ''
    
    for i in range(len(s)-1, -1, -1):
        sFlipped += s[i]
        
    return s == sFlipped
    

def isPalindrome2(s):
    #scan
    s = clean(s)
    i = 0
    j = len(s) - 1
    
    while(i < j):
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
        
    return True
        

def isPalindrome3(s):
    s = clean(s)
    return s == s[::-1]
    

#7
def compressStr(s):
    
    try:
        prevChar = s[0] #first char
        
    except:
        return ""
    
    
    cnt = 1
    compS = ""
    
    for char in s: #iterating through the whole string
        
        if(char == prevChar): #char comprehension
            cnt += 1
            
        else:
            compS += prevChar + str(cnt)
            prevChar = char
            cnt = 1
    
    compS += f"{prevChar}{cnt}" #last char
    return compS
        

#8
def longestCommonPrefix(lst):
    
    try:
        f = lst[0] #first string
    except:
        return  ''
        
    cmnPrefix = '' #common prefix
        
    for i in range(len(f)):
            
        
        for s in lst: #iterating thorugh strings in the list
                
            try:
                if s[i] != f[i]:
                    return cmnPrefix
            except:
            # loop breakout in case the common prefix is already equal to the first string;
            # hence there are no more possible char values.
                return cmnPrefix
            
        cmnPrefix += f[i]
        
        
            
    return cmnPrefix



def main():
    
#1
    # rotStr("abc3")

#2
    # print(rotStr2("abc3"))
    
    
#3
    # breakCode("Wf3a93trpe9_r", 3)
    
#4      
    # print(reverseSentence("Hello World Python"))
    # print(reverseSentence("public static void main(String[] args)"))

#5
    
    print(finder('ATT#ATAATAG#ATGC#GGT#GAATT#ATTATTGCATGG')) # = [4, 5] .א
    print(finder('att#at#gata#attattatt#attack'))  # [3, 3, 4] is not a possible output of the function
                                                    # as it essentially returns a boolean for wether it appears or not, and no maatter how many times it appears within one string - we've already indicated it is in 3, so that index is always either printed only once or not at all.  .ב # 
    # never because the for loop only detects for the other parts, compared to part of i=0  .ג
    
    print(finder("wiki#ikiw#wikipedia#encyclopedia#naknik#information#globalization"))

    
#6    
    # print(isPalindrome3("Madam I'm Adam!"))
    # print(isPalindrome3("#%&!(  2+$ Madam I'm Adam!"))
    # print(isPalindrome3("#% xcx 2+$ Madam I'm Adam!"))
    
#7
    # print(compressStr("aaabccdddda"))
    
#8
    print("")
    print(longestCommonPrefix(["flower", "flow", "flight"]))
    print(longestCommonPrefix(["Wiki", "Wikipage", "Wikipedia"]))
    print(longestCommonPrefix(["Wikipedia", "Wikipage", "Wiki"]))
    print(longestCommonPrefix(["Wikipages", "Wikipage", "Wiki"]))
    print(longestCommonPrefix(["Weakipedia", "Wikipage", "Wiki"]))
    print(longestCommonPrefix(["dog", "racecar", "car"]))
    
    return;
    
main() 
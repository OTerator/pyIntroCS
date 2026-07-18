# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 08:59:01 2025

@author: Ori
"""

#1
def printForward(n):
    if n <= 0:  
        return
    
    printForward(n-1)
    print(n)
    
# printForward(10)


#2
def printBackwards(n):
    if n<= 0:
        return
    
    print(n)
    printBackwards(n-1)
    
# printBackwards(10)


#3
def mult(a, b):
    
    if a == 1:
        return b
    
    return b + mult(a-1, b)

# print(mult(6, 7))


#4
def strLen(s):
    
    if s == '':
        return 0
    
    return strLen(s[1:]) + 1

# print(strLen("123456789"))


#5
def reverseStr(s):
    
    if s == s[-1]:
        return s
    
    return reverseStr(s[1:]) + s[0]

# print(reverseStr("abcdef"))



#6
def removeChar(s, c):
    
    if s[0] == s:
        if s.lower() != c:
            return s[0]
        else:
            return ""
    
    if s[-1].lower() != c:
        return removeChar(s[:-1], c) + s[-1]
    else:
        return removeChar(s[:-1], c)

# print(removeChar("abc12cxyc", 'c'))
# print(removeChar("In British we say: 'Bottle of water', ain't that better mate?", 't'))


#7
'''this recursive function is going to return the greatest (maxiumum) number of that group.
    function is splitting the list by halves until it is left with comparable discrete partitions to compare and return the greater of.
    this is a recursive version of the max() function in python.'''
    
def mi_ani(lst):
    n = len(lst)
    if n == 1:
        return lst[0]
    a = mi_ani(lst[:n//2])
    b = mi_ani(lst[n//2:])
    if a > b:
        return a
    return b

def mi_main():
    lst = [4,8,1,7,0]
    print(lst)
    print(mi_ani(lst))
    
# mi_main()



#8
'''after a thorough analysis: this recursive funtion recieves an integer and returns its reversed version via
    modular and arithmetic calculations: a modular calculation of mod 10 (essentially, powers of 10) is used to determine
    the length of our integers within each iteration. after the appropriate i is found it is used to multiply the last digit
    to create the next part of the final number. for example:
        1234 would be converted into: 4000+300+20+1 to get 4321. '''
def ma_ani(n):
    
    if n < 10:
        return n
    else:
        i = 10
        while n % i != n:
            i *= 10
        return ((n % 10) * (i // 10)) + ma_ani(n // 10)

def ma_main():
    n = 23456
    print(ma_ani(n))
    
# ma_main()



#9
def printOdd(lst):
    
    if not lst: # empty list 
        return 

    if lst[0]%2 == 1:
        print(lst[0])    
    
    printOdd(lst[1:])
    

# printOdd([1,2,3,4,5,6,7,8,9,10,11])



#10
def sumList(lst):
    
    if not lst:
        return 0
    
    return sumList(lst[:-1]) + lst[-1]


# print(sumList([1,2,3,4,5,6,7,8,9,10]))



#11
def multEvens(lst):
    
    if not lst:
        return 1
    
    if lst[-1] % 2 == 0:
        return multEvens(lst[:-1])*lst[-1]
    else:
        return multEvens(lst[:-1])


# print(multEvens([1,2,3,4,5,2,7,8,4,7,9976543,2,453,2]))



#12
def isPalindrome(s):
    
    if s == "":
        return True
    
    if not s[-1].isalpha():
        return isPalindrome(s[:-1])
    if not s[0].isalpha():
        return isPalindrome(s[1:])
    
    if isPalindrome(s[1:-1]):
        if s[0].lower() == s[-1].lower():
            return True
    return False

# print(isPalindrome("Madam, I'm Adam!"))



#13
def isInList(a, lst):
    
    if not lst:
        return False
    
    return a == lst[0] or isInList(a, lst[1:])

# print(isInList(7, [1, 2, 4, 7, 5, 3]))


def hasCommon(lst1, lst2):
    
    if not lst1:
        return False
    
    return isInList(lst1[0], lst2) or hasCommon(lst1[1:], lst2)
    
    
# print(hasCommon([1, 2, 76], [3, 4 ,5, 76]))
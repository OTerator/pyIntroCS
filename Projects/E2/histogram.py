# -*- coding: utf-8 -*-
"""
Student: Ori Almog
ID: [redacted]
Assignment no. 2
Program: histogram.py

"""

def count_letters(s): 
    #This function recieves a string and counts in how many of its words (sub-strings seperated by whitespace)
    #each of the English alphabetic letters appeared.
    
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cntLst = [0]*26
    # a  b  c  d  e  f  g  h  i  j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z
    # 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26
    
    lwrcseS = s.lower()
    words = lwrcseS.split() #Split the sentence into seperate words.
    
    for word in words:
        
        for i in range(26):
            if word.__contains__(abc[i]):
                cntLst[i] += 1
                
    return cntLst #the list that holds the counting for each and every letter for the histogram, 
                  #used like a DNA code for its construction.



def draw_histogram(lst):
    #This function recieves a list, (supossedly of len 26 for each letter) and prints a histogram accordingly.
    
    h = max(lst)
    for i in range(h):
        
        for j in range(26):
            
            if lst[j] >= (h-i):
                print("^", end=' ')
            else:
                print(" ", end=' ')
        print('')
    print("a b c d e f g h i j k l m n o p q r s t u v w x y z")



def main(): #recieves a file name input from the user to analyze.
    fName = input("please enter a file name (path) for an alphabetic Histogram: ")
    file = open(fName, mode='r')
    text = file.read()
    file.close()
    
    # text = 'this is a test for counting letters in words and drawing a histogram'
    draw_histogram(count_letters(text))
    
main()

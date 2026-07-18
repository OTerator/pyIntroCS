# -*- coding: utf-8 -*-
"""
Student: Ori Almog
ID: [redacted]
Assignment no. 2
Program: triangle.py

"""
   

def get_string_triangle(s, h):
    #recieves a string and height from the user and prints a triangle of that height,
    #filled inside with characters from the given string.
    
    triStr = ''
    
    triArea = (h-2)**3 #how many character can fit inside the requested triangle
                        #4 -> 2**2, 5 -> 3**2, 6 --> 4**2, ..., n --> (n-2)**2 ...
    base = 2*h - 1
    newS = ''
    
    while(len(newS) < triArea): #build up a string to fill up the triangle with.
        for char in s:
            newS += char
    
    c = 0
    for i in range(h-1):
        
        
        triStr += (" ")*(h-(i+1))
        triStr += '*'
        # filled up h-i chars with spaces and a '*'
        
        for j in range(2*i - 1):
            
            triStr += newS[c]
            c += 1
            
        if(i != 0):
            triStr += '*'
        triStr += "\n"
        
    triStr += '*'*base
            
    return triStr



def main():
    
    string = ""
    while(True): #loop calling the function in each iteration, passing arguements from the user.
                 #looping until the string "stop" is given by the user.
        
        string = str(input("Please enter a string, (stop to end): "))
        if(string == "stop"):
            return
        print(get_string_triangle(string, int(input("Enter triangle height: "))))
    
    
main()


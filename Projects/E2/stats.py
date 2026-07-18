# -*- coding: utf-8 -*-
"""
Student: Ori Almog
ID: [redacted]
Assignment no. 2
Program: stats.py

"""


def scanInts(fileName): #Scans the entire text of a file and extracts all strings seperated by whitespace into a list.
                        #Then, proceeds to filter and analyse the numbers accordingly using sub-functions.
    file = open(fileName, mode='r')
    text = file.read()
    file.close()
    
    strings = text.split()
    #Split all words into seperate strings inside a new list
    
    nList = cleanIntList(strings) #Just integers
    
    print("maximum:", max(nList))
    print("minimum:", min(nList))
    print("average:", sum(nList)/len(nList))
    print(orderCheck(nList))
        
    
def cleanIntList(lst): #recieves a list and return a new one with just whole integers, cleared out commas and dots by the end of a sentence.
    
    newLst = []
    for s in lst:
        
        if s.isdecimal():
            newLst.append(int(s))
            continue
        
        if s.__contains__('.') or s.__contains__(','):
            
            if s.endswith('.'):
                s = s[:-1] #we cut the '.' from the end of a sentence,
                           #but, in the case its a decimal anywhere else, it is left untouched so we don't pick up on that number.
            
            if s.__contains__(','):
                s = s.replace(',', '')
            
            if s.isdecimal():
                newLst.append(int(s))
                
    return newLst
   
    
     
def orderCheck(lst): #recieves a list of integers and checks if its ordered - Increasing, Deceasing or not ordered.
    
    increasing = True
    decreasing = True
        

    for i in range(len(lst)-1):
        
        if(lst[i] < lst[i+1]):
            decreasing = False
        elif(lst[i] > lst[i+1]):
            increasing = False
            
    if increasing:
        return "Increasing"
    elif decreasing:
        return "Decreasing"
    else:
        return "Not ordered"
    

def main():
    scanInts("numbers.txt")
    
main()
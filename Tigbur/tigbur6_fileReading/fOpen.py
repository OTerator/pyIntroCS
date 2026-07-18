# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 15:14:09 2025

@author: Ori
"""
import random


def scanChars(fName, n):
    file = open(fName, mode='r')
    text = file.read(n)
    file.close()
    return text
    
def scanLines(fName, n):
    file = open(fName, mode='r')
    textLines = file.readlines()
    file.close()
    return textLines[:n]

def read(fName):
    file = open(fName)
    txt = file.read()
    file.close()
    return txt


def cntLines(fName):
    file = open(fName)
    fLines = file.readlines()
    file.close()
    return len(fLines)

def cntTxtLines(fName):
    file = open(fName)
    fLines = file.readlines()
    file.close()
    
    txtLines = 0
    for l in fLines:
        if l.isspace():
            continue;
        txtLines += 1
    
    return txtLines

# print("Total:", cntLines("song.txt"))
# print("Contains text:", cntTxtLines("song.txt"))

def randLine(fName):
    file = open(fName, mode='r')
    txtLines = file.readlines()
    rLine = random.choice(txtLines)
    file.close()
    
    while rLine.isspace():
        rLine = random.choice(txtLines)

    return rLine
    
# print(randLine("song.txt"))
  
def q6(fName):
    file = open(fName, mode='r')
    txt = file.read()
    file.close()
    
    txtWords = txt.split()
    longest = max(txtWords, key=len)
    return longest
             
#print(q6("song.txt"))


def fWrite(fName):
    file = open(fName, mode='w')
    file.write("Hello World!")
    file.close()
    
#print(scanChars("hello.txt", 20))


def usrWrite(fName):
    file = open(fName, mode='w')
    file.write(input("Writing input: "))
    file.close()

def main():    
    file = input("Lets give the the file a name ending with .txt: ")
    usrWrite(file)
    print(read(file))
    
main()
    
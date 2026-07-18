# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 16:34:38 2025

@author: Ori
"""
import random


def wordCounter():    
    word = ""
    
    while (word != "stop"):
        
        word = input("Enter a new word please: ")
        counter = 0
        
        for char in word:
            counter += 1
            
        print(word, "has", counter, "characters")
    
    
def getNums():
    
    number = random.randint(1,20)
    guess = -1
    attempts = 0
    
    while guess != number:
        attempts += 1
        guess = int(input("Guess a number between 1-20: "))
        
        if guess > number:
            print("Too high")
        
        elif guess < number:
            print("Too low")
            
    print("Yes indeed!", number, "is the correct answer.")
    print("You took", attempts, "attempts to guess correctly.")

def charPrint(word):
    
    for char in word:
        print(char, "", end = "")


def sevenBoom():

    
    for i in range (1, 101):
        
        if i % 7 == 0:
            print("BOOM!")
       ################################ 
        # iString = str(i)
        
        # for digit in iString:
        #     if digit == 7:
        #         isBoom = True
                   
        #         if isBoom:
        #             print("Boom!")
                ############################
        
        else:
            print(i)
            
    

def main():
    
    #wordCounter()
    #getNums()
    #charPrint("Ori")
    sevenBoom()
    
    
main()
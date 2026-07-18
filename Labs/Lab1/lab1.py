# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 12:14:31 2025

@author: Ori
"""
    
def greeting():
    
    name = input("Please enter your name: ");
    print("It is a pleasure to meet you, " + name + "!\n");
    
    # print("let me show you a little of my capabilities-")
  
    
def next_year():
    age = int(input("Say, how old are you? "));
    # print(age + "Years old. so, you were born by", 2025 + age, "right?";
    age_next_year = age + 1;
    print("next_year:", age_next_year);


def main():
    next_year();
    
main();
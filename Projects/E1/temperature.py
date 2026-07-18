# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 16:47:04 2025

@author: Ori

Student: Ori Almog
ID: [redacted]
Assignment no. 1
Program: temperature.py

"""

#א#
def fahr2Celcius(fTemp):
    
    """
    Recieves a temperature value in Fahrenheit and calculates its equivalent in Celsius, proceeds
    to validate it isn't under the range of the Celsius scale and finally, returns the value.    

    """
    
    cTemp = 5*(fTemp-32)/9
    
    if (cTemp < -273.15):
        return "Wrong temperature"
    
    return cTemp;


#ב#
def f2cTable(lowT, highT, lines):
    
    """
    This function recieves a requested amount of lines for a table of values, alongside low and high 
    temperatures in Fahrenheit. Then, proceeds to convert them into Celsius via fahr2Celcius() and prints
    all in a table.
    
    The Fahrenheit values in between are split accordingly to the number of lines so, the differences
    are propotional.
    
    """
    
    d = (highT - lowT)/(lines - 1)
    
    print("")
    print("Fahrenheit	    Celsius")
    print("-----------------------------------")
    for i in range(lines):
        
        fTemp = lowT + d*i
        cTemp = fahr2Celcius(fTemp)
        
        print(fTemp, "\t\t\t", cTemp)


def main():

    #print(fahr2Celcius(float(input("Input Farenheit Temperature: "))))
    
    f2cTable(float(input("Enter low temperature in Farenheit: ")), 
             float(input("Enter high temperature in Farenheit: ")), 
             int(input("Enter number of lines: ")))
    
main()

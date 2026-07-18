# -*- coding: utf-8 -*-
"""
Student: Ori Almog
ID: [redacted]
Assignment no. 2
Program: calendar.py

"""

def monthCalendar(month, year):
    # this function recieves a month and year and prints a calendar accordingly.
    
    monthInDays = monthLength(month, year) # for instance, January would always return 31
    if monthInDays == -1:
        print("Given month is Invalid.")
        return;
    
    print(month, year)
    print("Su  Mo  Tu  We  Th  Fr  Sa")
    
    determinant = firstDayOfMonth(month, year)
    #determines how many spaces should be taken from the start of the table until the 1st of the month.
    
    date = 1 #starting with one, incrementing by one after each print until monthInDays, including.
    
    for w in range(1,6): #week in month
        
        if (w == 1):
            print("    "*determinant, end = '')
        
        
        for d in range(1,8): #day in week
            
        
            if date > monthInDays:
                break
            
            print(date, end = "  ")
            
            if date < 10:
                print(" ", end = "")
                
            if d == 7-determinant:
                print("") #end of a week: moving down a line.
                
            date += 1
            


def isLeap(year): # Checks for wether the given year is leap.
    
    if year%4 != 0:
        return False
    elif year%100 == 0:
        return (year%400 == 0)



def monthLength(month, year): #recieves the month and its year and returns its length in days.
    
    months = [["January", 31], ["February", 28], ["March", 31], ["April", 30], 
              ["May", 31], ["June", 30], ["July", 31], ["August", 31], 
              ["September", 30], ["October", 31], ["November", 30], ["December", 31]]
    
    if isLeap(year): #Adjusting February for leap years.
        months[1][1] = 29
        
    for a in months:
        if(a[0] == month.capitalize()):
            return a[1] #value returned in days.
        
    return -1 #In case the string given is not a valid month.


def firstDayOfMonth(month, year):
    #This function recieves a month and year and returns a value between 0 and 6
    #corresponding the day of the week for the 1st of the month.
    
    months = [["January", 13], ["February", 14], ["March", 3], ["April", 4], 
              ["May", 5], ["June", 6], ["July", 7], ["August", 8], 
              ["September", 9], ["October", 10], ["November", 11], ["December", 12]]
    
    try:
        
        for a in months:
            
            if(a[0] == month.capitalize()):
                monthInt = a[1]
                #convert given string into the required calculation integer
                
        if(monthInt > 12):
            year -= 1
                
    except: # In case the string given is not a valid month, 
            # in which case monthInt would never get defined.
        return -1
    
    cen = year // 100 #century ex: 20 (20th) for 2025
    yoCen = year % 100 #year of century ex: 25 for 2025
    
    
    calculation = (1 + (13*(monthInt + 1))//5) + yoCen + (yoCen//4) + (cen//4) + (5*cen)
                                          
    return ((calculation % 7)-1) % 7
    #Based on the algorithm: Zeller's Congruence - for the Gregorian Calendar.
    #Returned value is a modulo of 7, hence, between 0-6, and such that stands for the following:
    #(6 = Saturday, 0 = Sunday, 1 = Monday, ..., 5 = Friday).
    


def main():
    
    monthCalendar("June", 2002)
    
main()
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 09:07:09 2025

@author: Ori
"""
import random


#2
def helloYouVer2(name):
    
    print("Hello,", name + "! it is nice to meet you!")



#3
def starsPhrase(phrase, starCount):
    
    print(starCount * "*" + phrase + starCount * "*")



#4
def calculateSumOfThree(n1, n2, n3):
    
    nSum = n1 + n2 + n3
    
    return nSum;



#5
def avgThreeNums(n1, n2, n3):
    
    nSum = n1 + n2 + n3
    
    return (nSum / 3)

# better version of the function; making use of an already existing previous function
def connectingAverage(n1, n2, n3):
    
    average = calculateSumOfThree(n1, n2, n3) / 3
   
    return average
  
  

#6
def futureAge(age, currentYear, futureYear):
    
    futureAge = futureYear - currentYear + age
    print("In", futureYear, "you'll be", futureAge, "years old.")


#7
def digitSum(num):
    
    n1 = num % 10
    n2 =  (num // 10) % 10
    n3 = (num // 100)
    
    nSum = n1 + n2 + n3
    return nSum



#8
def determineGreatestNum(n1, n2, n3):
    
    # if (n1 > n2) & (n1 > n3):
    #     return(n1+1)
    
    # elif (n2 > n1) & (n2 > n3):
    #     return(n2+2)
    
    # else:
    #     return (n3+3)
    
    
    if (n1 >= n2 & n1 >= n3):
        
        return n1
    
    elif (n1 <= n2 >= n3):
        return n2
    
    else :
        return n3



#9
def lucky():
    
    number = random.randint(1, 6)
    
    print(number)
    
    if (number % 2 == 0):
        print ("The number is even.")
        
    else:
        print ("The number is odd.")
        
    
    if (number % 3 == 0):
        print("The number is divisible by 3.")
        
    else:
        print("The number is not divisible by 3.")
        
            
    if (number > 4):
        print("(:")
        
    elif (number < 3):
        print("):")
            
    else:
        print("|:")
    


#10
def digitAnalysis(num):
    
    digitCount = 0
    evenSum = 0
    
    while (num > 0):
        digitCount += 1     
        
        digit = num % 10
        
        if (digit % 2 == 0):
            evenSum += digit
        
        num //= 10
        #end of iteration
        
    
    print("digit count =", digitCount, "even's sum =", evenSum)
    


#11
def diceGuess(nGuess):
    
    number = random.randint(1, 6);
    attemptCount = 1
    
    while(nGuess != number):
        
        nGuess = int(input("Guess a number between 1 and 6: "))
        attemptCount += 1
        
    
    print("You guess it in", attemptCount, "attempts!")



#12
def symmetric(integer):
    
    intChanged = integer
    intFlipped = 0
    
    while (intChanged > 0):
        
        #print(intFlipped)
        intFlipped *= 10
        #print(intFlipped)
        intFlipped += intChanged % 10
        #print(intFlipped)
        intChanged //= 10
        #print(integer, intChanged, intFlipped)
    
    
    return (integer == intFlipped)


    #246 -> "2", "4", "6"


def main():

   # #2
   # helloYouVer2((input("What is your name? ")))
   # helloYouVer2("Popeye")
   
   # #3
   # starsPhrase("I had a great time in my Introduction to CS class today", 9)
   
   # #4
   # print("Sum of these three =", calculateSumOfThree(5, 1, 8))
   # print("Sum of these three =", calculateSumOfThree(int(input("Enter your first Number: ")), int(input("second: ")), int(input("third: ")) ))
   
   # #5
   # print(avgThreeNums(4, 8, 15))
   # print(connectingAverage(5, 12, 10))
   
   
   # #6
   # futureAge(22, 2025, 2030)
   # futureAge(float(input("Please enter your age: ")), 
   #           int(input("Current year: ")), 
   #           int(input("Future year: ")))
   
   
   # #8
   # print(determineGreatestNum(1, 2, 3))
   
   
   # #9
   # lucky()
   
      
   # #10
   # digitAnalysis(1234)
   
   
   # #11
   # diceGuess(int(input("Guess a number between 1 and 6: ")))
   
   
   #12
   
   print(symmetric(int(input("Enter a number of choice: "))))
   
   
   if (symmetric(int(input("Enter a number of choice: ")))):
       
       print("Your number is symetric!")
       
   else:
       print("Your number is not Symmertric.")
        
     

main()



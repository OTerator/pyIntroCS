# -*- coding: utf-8 -*-
"""
Student: Ori Almog
ID: [redacted]
Assignment no. 3
Program: lifeGame.py

"""

def neighborCounter(mtrx, row, col): # calculates how many living cells surround a certain matrix's cell.
                                     # used to determine the status of that very cell in the next generation.
    
    cnt = 0 - mtrx[row][col]
    
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            cnt += mtrx[i][j]
    
    return cnt




def calculateNextGen(mtrx):    # recieves the current generation's matrix and calculates the next one to display.
    
    nextGen = [[0 for col in mtrx] for row in mtrx] # new gen matrix to build up on
    
    for i in range(1, len(mtrx)-1):
        for j in range(1, len(mtrx)-1):
            
            neighbors = neighborCounter(mtrx, i, j)
            
            if mtrx[i][j] == 0 and neighbors == 3: # new cell
                    nextGen[i][j] = 1
                    
            elif mtrx[i][j] == 1 and neighbors >= 2 and neighbors <= 3: # cell survival
                    nextGen[i][j] = 1
    
    return nextGen




def displayBoard(mtrx):     # revieves a matrix of 0s and 1s and prints a board for the user to view.
    
    print()
    for i in range(1, len(mtrx)-1):
        for j in range(1, len(mtrx)-1):
            if mtrx[i][j] == 0:
                print("- ", end='')
            else:
                print("X ", end='')
        print()
    
    


def padding(mtrx): # adds layers of zeros around the matrix as a border, 
# while not being displayed visually, it is used to simplify calculations.
    
    padlst = [0 for i in mtrx[0]]
    
    mtrx.insert(0, padlst)   # top
    
    for row in mtrx:         # sides
        row.insert(0, 0)
        row.append(0)
    
    mtrx.append(padlst)      # bottom
    
    return mtrx




def scan(board): # recieves a board's file name, scans its text and turns it into a matrix of bits.
    
    file = open(board, mode = 'r')
    text = file.readlines()
    file.close()
    
    # print(text)
    numLst = [nums.split() for nums in [s.strip() for s in text]]
    bitLst = [[int(bit) for bit in line] for line in numLst]
    
    return bitLst
    



def main():
    
    while True:
        
        try:
            fileName = input("type a file's name for a starting game board: ")
            if fileName.lower() == "cancel":
                print("Program has been shut down successfully. Goodbye!")
                return
            
            data = padding(scan(fileName))
            displayBoard(data)
            break;
            
        except FileNotFoundError:
            print(f"'{fileName}' was not found.")
            print("You can type 'cancel' to shut the program.", end = "\n\n")
        except ValueError:
            print(f"'{fileName}' is Invalid.")
            print("You can type 'cancel' to shut the program.", end = "\n\n")
    
    
    while True:
        
        print()
        answer = input("Display next generation? (y/n): ").lower()
        
        if answer == "yes" or answer == 'y' or answer == '':
            data = calculateNextGen(data)
            displayBoard(data)
            
        elif answer == "no" or answer == 'n':
            print()
            print("Program has been shut down successfully. Goodbye!")
            break;
            
        else:
            print("Please type 'y' to continue or 'n' to pause the program.")
        
        
main()

# -*- coding: utf-8 -*-
"""
Student: Ori Almog
ID: [redacted]
Assignment no. 3
Program: grades.py

"""


def readStudents(): # organizes the text into a clean list consisting of each line, then based on that list-
                    # comprehends the desired dictionary to return.
    
    file = open("students.txt", mode = 'r')
    text = file.readlines()
    file.close()
    
    students = [line.strip() for line in text]
    studentItems = [string.split(' ', 1) for string in students]
    
    return {item[0]:item[1] for item in studentItems}



def readGrades(): # organizes the text into a clean list consisting of each line, then based on that list-
                  # comprehends the desired dictionary to return.
    
    file = open("grades.txt", mode = 'r')
    text = file.readlines()
    file.close
    
    grades = [line.strip() for line in text]
    grItems = [string.split() for string in grades]
    
    return {item[0]:item[1] for item in grItems}



def averageGrades(gradeDct): # recieves a dictionary of numeric values and returns their average (intentionally grades).
    
    try:
        grades = [int(grade) for grade in gradeDct.values()]
    except TypeError:
        print("Function variable is not a dictionary.")
    except ValueError:
        print("Grade values must be integers.")
    
    
    return sum(grades)/len(grades)



def findMax(studentDct, gradeDct): # finds the student/s that scored the highest grades and returns their name/s in a list.
    
    maxIds = [k for k,v in gradeDct.items() if v == max(gradeDct.values())]
    
    return [studentDct[k] for k in maxIds]




def verifyIds(studentDct, gradeDct): # checks if there are IDs in grades.txt that don't appear in students.txt, if there are any they're discarded.
    
    for k in list(gradeDct):
        
        try:
            test = studentDct[k]
        except KeyError:
            gradeDct.pop(k)
            print(f'id "{k}" does not appear in students.txt and therefore, has been discarded from the dictionary.')



def main(): # little testing of the functions
    
    print('-----')
    students = readStudents()
    grades = readGrades()
    print("Grade average =", averageGrades(grades))
    print("Highest scoring students:", findMax(students, grades))
    verifyIds(students, grades)
    
    print('', '-----', "Fake ID test:", sep = '\n')
    
    gradesFakeIds = {'176790066': '95', '151629085': '89', '100172244': '73', '339091273': '71', '592236988': '86'}
    verifyIds(students, gradesFakeIds)
    
    print('-----', end = '\n\n')
    
    fakeGrades = {'076790066': '95', '651629085': '89', '200172244': '99', '339091273': '99', '592236988': '99'}
    print("Fake average =", averageGrades(fakeGrades))
    print("Fake top-grade students:", findMax(students, fakeGrades))
main()        
        
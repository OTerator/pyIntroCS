# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 13:38:15 2025

@author: Ori
"""          


def isMailLegal(mail):
    return True

class mailAddr:
    
    def __init__(self, name = ''):
        self.__name = name
        self.__mail = ''
        
    
    def isMailLegal2(mail):
        return True
    
    def setName(self, name):
        self.__name = name
        
    def setMail(self, mail):
        if isMailLegal(mail) and mailAddr.isMailLegal2(mail):
            self.__mail = mail
            
    def getName(self):
        return self.__name
    
    def getMail(self):
        return self.__mail
    

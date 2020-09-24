#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:51:06 2019

@author: tikilia
"""

class Person:
    def __init__(self):
        pass
    def gerGender(self):
        return 'Unknown'
    
class Male(Person):
    def getGender(self):
        return 'Male'
        
class Female(Person):
    def getGender(self):
        return'Female'
        
M=Male()
F=Female()

print(M.getGender())
print(F.getGender())

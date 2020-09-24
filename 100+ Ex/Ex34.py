#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:54:49 2019

@author: tikilia
"""
def squareList():
    lst=[]
    for i in range(1,21):
        lst.append(i*i)
    return lst        
    
print(squareList()[0:5])
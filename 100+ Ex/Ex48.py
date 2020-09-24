#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:49:29 2019

@author: tikilia
"""

class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width

rec=Rectangle(3,4)
print(rec.area())    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 12:30:08 2019

@author: tikilia
"""

class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length=0):
        #Shape.__init__(self)
        self.length=length
    def area(self):
        return self.length*self.length
    
print(Square(5).area())

        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:54:29 2019

@author: tikilia
"""

class Circle():
    def __init__(self,r):
        self.radius=r
    def compute(self):
        return (self.radius**2)*3.14
    

cir=Circle(int(input()))
print(cir.compute())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:16:00 2019

@author: tikilia
"""

class IOstring():
    def _init_(self):
        pass
    def getString(self):
        self.get = input()
    def printString(self):
        print(self.get.upper())
        
ex5=IOstring()
ex5.getString()
ex5.printString()

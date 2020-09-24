#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:49:29 2019

@author: tikilia
"""

class American:
    species='mammal'
    
class NewYork(American):
    pass

a=American
print(a.species)

b=NewYork
print(b.species)
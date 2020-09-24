#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 11:20:01 2019

@author: tikilia
"""

x = list(input().split())
x.sort()

for i in x:
    if x.count(i) > 1:
        x.remove(i) 
        
print(' '.join(x))
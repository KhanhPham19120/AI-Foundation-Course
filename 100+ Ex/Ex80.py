#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:20:13 2019

@author: tikilia
"""

lst=[5, 6, 77, 45, 22, 12, 24]

for i in lst:
    if i%2==0:
        lst.remove(i)
        
print(lst)
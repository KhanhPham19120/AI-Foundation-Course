#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:48:47 2019

@author: tikilia
"""

lst=[12,24,35,24,88,120,155,88,120,155]

for i in lst:
    if lst.count(i)>1:
        lst.remove(i)

print(lst)
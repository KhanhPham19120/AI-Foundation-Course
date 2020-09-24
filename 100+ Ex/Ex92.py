#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:08:43 2019

@author: tikilia
"""

n=list(input())

for i in n:
    if '0'<=i<='9':
        n.remove(i)
        
print(''.join(n))
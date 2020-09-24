#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:59:24 2019

@author: tikilia
"""
result = []
for i in range(1000,3001):
    test = 1
    for j in str(i):
        if int(j) % 2 !=0:
            test = 0
    if test == 1:
        result.append(str(i))
print(','.join(result))
            
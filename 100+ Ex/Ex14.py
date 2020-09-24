#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:34:26 2019

@author: tikilia
"""
s=input()

up = 0
low = 0
for i in s:
    for j in str(i):
        if 'a'<j<'z':
            low += 1
        if 'A'<j<'Z':
            up += 1
print('UPPER: {}'.format(up))
print('LOWER: {}'.format(low))
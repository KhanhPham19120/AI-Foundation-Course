#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:57:24 2019

@author: tikilia
"""

total = 0
while True:
    n=input().split()
    if len(n) == 0:
        break
    if n[0] == 'D':
        total = total + int(n[1])
    if n[0] == 'W':
        total = total - int(n[1])
print(total)
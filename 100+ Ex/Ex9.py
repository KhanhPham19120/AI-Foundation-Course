#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 11:16:36 2019

@author: tikilia
"""
arr=[]
while True:
    x=input()
    if len(x)==0:
        break
    arr.append(x)

for line in arr:
    print(line.upper())
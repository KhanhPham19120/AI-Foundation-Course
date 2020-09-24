#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 23:48:16 2019

@author: tikilia
"""

n=int(input())

for i in range(n+1):
    if i%5==0 and i%7==0:
        print(i,end=', ')
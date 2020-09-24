#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 23:14:21 2019

@author: tikilia
"""

n=int(input())
sum=0

for i in range(1,n+1):
    sum+=i/(i+1)

print(round(sum, 2))    
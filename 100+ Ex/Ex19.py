#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:06:51 2019

@author: tikilia
"""

xx=[]

while True:
    n=input().split(',')
    if len(n)==0:
        break
    xx.append(tuple(n))

xx.sort(key = lambda x:(x[0],x[1],x[2]))

print(xx)    
    

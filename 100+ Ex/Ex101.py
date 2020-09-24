#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:22:27 2019

@author: tikilia
"""

n=input()
dict1={}

for i in n:
    dict1[i]=dict1.get(i,0)+1
    
dict1 = sorted(dict1.items(),key=lambda x: (-x[1],x[0]))
for i in dict1[:3]:
    print(i[0],i[1])
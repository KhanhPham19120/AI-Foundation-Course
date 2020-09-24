#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:29:27 2019

@author: tikilia
"""

tup1=(1,2,3,4,5,6,7,8,9,10)
tup2=[]


for i in tup1:
    if i % 2 == 1:
        tup2.append(i)

print(tuple(tup2))        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:06:25 2019

@author: tikilia
"""
for i in range(2000,3201):
    if i % 5 != 0 and i % 7 == 0:
        print(i,end=', ')
print('\b')
        
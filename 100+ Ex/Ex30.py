#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:34:20 2019

@author: tikilia
"""

a,b=input(),input()

if len(a) != len(b):
    if len(a)>len(b):
        print(a)
    else:
        print(b)
else:
    print(a,end='\n')
    print(b)
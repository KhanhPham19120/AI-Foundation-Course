#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:43:50 2019

@author: tikilia
"""

def compute(a):
    return a +int(str(a)*2)+int(str(a)*3)+int(str(a)*4)
n=int(input())
print(compute(n))
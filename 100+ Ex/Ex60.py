#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 23:30:41 2019

@author: tikilia
"""

def f(n):
    if n==0:
        return 0
    if n>0:
        return f(n-1)+100

n=int(input())

print(f(n))
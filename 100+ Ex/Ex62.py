#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 23:44:37 2019

@author: tikilia
"""

def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return f(n-1)+f(n-2)

n=int(input())
for i in range(n+1):
    print(f(i),end=', ')
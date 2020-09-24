#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:03:40 2019

@author: tikilia
"""

n=set(map(int,input().split()))
m=set(map(int,input().split()))

lst=list(n^m)
lst.sort()

for i in lst:
    print(i)
    



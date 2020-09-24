#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:19:48 2019

@author: tikilia
"""

n=input().split()
lst=[]

for i in range(len(n)):
    m=list(set(n[i]))
    for j in range(len(m)):
        if 'a'<=m[j]<='z' or 'A'<=m[j]<='Z':
            pass
        else:
            lst.append(m[j])
        
print(lst)
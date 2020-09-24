#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:27:19 2019

@author: tikilia
"""

st=set(map(int,input().split()))
lst=list(st)
lst.sort(reverse=True)

print(lst[1])


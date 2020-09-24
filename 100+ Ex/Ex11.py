#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:38:11 2019

@author: tikilia
"""

num = input().split(',')

for i in range(len(num)):
    if int(num[i],2) % 5 == 0:
        print(num[i],end = ', ')
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:56:07 2019

@author: tikilia
"""

num1,num2=map(int,input().split(','))

arr=[]

for i in range(num1):
    xx=[]
    for j in range(num2):
        xx.append(i*j)
    arr.append(xx)

print(arr)
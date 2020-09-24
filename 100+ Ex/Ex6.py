#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:38:03 2019

@author: tikilia
"""
from math import sqrt
c=50
h=30

def result(d):
    d=int(d)
    return str(int(sqrt(((2*c*d))/h)))

num=input().split(',')
print(','.join(list(map(result,num)))) 
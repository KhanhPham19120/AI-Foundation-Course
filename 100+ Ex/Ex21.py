#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:57:43 2019

@author: tikilia
"""
from math import sqrt

up=0
down=0
right=0
left=0

while True:
    n=input().split()
    if len(n)==0:
        break
    if n[0]=='UP':
        up+=int(n[1])
    if n[0]=='DOWN':
        down+=int(n[1])
    if n[0]=='RIGHT':
        right+=int(n[1])
    if n[0]=='LEFT':
        left+=int(n[1])

result = sqrt((up-down)**2+(right-left)**2)

print(int(result))
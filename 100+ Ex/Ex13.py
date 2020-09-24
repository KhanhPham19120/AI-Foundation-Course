#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:19:58 2019

@author: tikilia
"""

def countLetter(i):
    count = 0
    for j in str(i):
        if ('a'<j<'z') or ('A'<j<'Z'):
            count += 1
    return count

def countNum(i):
    count = 0
    for j in str(i):
            if '0'<j<'9':
                count += 1 
    return count

strings = input().split()
countL=0
countN=0
for i in strings:
    countL += countLetter(i)
    countN += countNum(i)

print(countL)
print(countN)
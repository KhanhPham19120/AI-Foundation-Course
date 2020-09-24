#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:31:02 2019

@author: tikilia
"""
xx = input().split(',')
result = []

def is_lower(i):
    for j in i:
        if 'a'<j<'z':
            return True
    return False

def is_upper(i):
    for j in i:
        if 'A'<j<'Z':
            return True
    return False

def is_num(i):
    for j in i:
        if '0'<=j<='9':
            return True
    return False

def is_speckey(i):
    for j in i:
        if j == '$' or j == '#' or j == '@':
            return True
    return False

def is_range(i):
    if 6<=len(i)<=12:
        return True
    return False


for i in xx:
    if is_lower(i) and is_upper(i) and is_num(i) and is_speckey(i) and is_range(i):
        result.append(i)
        
print(','.join(result))
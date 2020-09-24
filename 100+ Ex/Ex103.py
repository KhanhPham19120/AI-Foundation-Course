#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:16:59 2019

@author: tikilia
"""

def sum(n):
    if n==0:
        return n
    return n+sum(n-1)

print(sum(5))
        
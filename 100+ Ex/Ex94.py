#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:13:45 2019

@author: tikilia
"""
def solve(numhead,numleg):
    ns='No Solution'
    for i in range(1,numhead+1):
        j=numhead-i
        if (2*i)+(4*j)==numleg:
            return i,j
    return ns,ns

solution=solve(35,94)
print(solution)
    
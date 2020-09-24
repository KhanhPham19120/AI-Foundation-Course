#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 11:51:12 2019

@author: tikilia
"""
sum= lambda s1,s2: s1+s2

n=list(map(int,input().split()))
print('{}'.format(sum(n[0],n[1])))
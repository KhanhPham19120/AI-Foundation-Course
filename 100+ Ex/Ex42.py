#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:43:43 2019

@author: tikilia
"""

lst=[1,2,3,4,5,6,7,8,9,10]

lst1=list(map(lambda i:i*i,filter(lambda x: x%2==0,lst)))

print(lst1)
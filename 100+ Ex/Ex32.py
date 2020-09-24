#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:43:50 2019

@author: tikilia
"""
lst=[]

dict1={i:i**2 for i in range(1,21)}

for keys in dict1:
    lst.append(keys)
    
print(lst)
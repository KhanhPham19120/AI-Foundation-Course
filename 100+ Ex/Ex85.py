#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:39:20 2019

@author: tikilia
"""

lst=[12, 24, 35, 70, 88, 120, 155]

print([lst[i] for i in range(1,len(lst)) if i<4 or i>5])
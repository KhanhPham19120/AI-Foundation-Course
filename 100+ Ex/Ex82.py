#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:26:44 2019

@author: tikilia
"""

lst=[12, 24, 35, 70, 88, 120, 155]

print([lst[i] for i in range(len(lst)) if i%2!=0])
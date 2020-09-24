#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:47:19 2019

@author: tikilia
"""

lst=[12, 24, 35, 24, 88, 120, 155]

print([lst[i] for i in range(len(lst)) if lst[i]!=24])
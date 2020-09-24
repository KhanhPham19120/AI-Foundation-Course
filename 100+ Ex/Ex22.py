#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 00:23:22 2019

@author: tikilia
"""

xx=input().split()

xxx=sorted((set(xx)))

for i in xxx:
    print('{0}:{1}'.format(i,xxx.count(i)))